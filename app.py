"""Giigle web app – a fake AI-powered search engine using Flask and OpenAI."""

import os
import json
import re
from flask import Flask, request, jsonify, send_from_directory
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "x.env"))

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
WATERMARK = "🚨 FAKE CONTENT ! DO NOT TRUST 🚨"


def safe_parse_json(text: str):
    """
    1. Strip Markdown fences and comment lines
    2. Locate the first '['
    3. Locate either the last ']' or, if missing, the last '}', then append ']'
    4. json.loads the slice
    """
    text = re.sub(r"```(?:json)?", "", text)
    lines = [ln for ln in text.splitlines() if not ln.lstrip().startswith("#")]
    cleaned = "\n".join(lines).strip()
    start = cleaned.find("[")
    if start == -1:
        raise ValueError("no JSON array found")
    end = cleaned.rfind("]")
    if end == -1 or end < start:
        last_obj = cleaned.rfind("}")
        if last_obj == -1 or last_obj < start:
            raise ValueError("no JSON object end found")
        json_str = cleaned[start : last_obj + 1] + "]"
    else:
        json_str = cleaned[start : end + 1]
    return json.loads(json_str)


@app.route("/search", methods=["GET"])
def search():
    """Handle search queries by generating fake search results using GPT."""
    query = request.args.get("q", "").strip()
    if not query:
        return jsonify(error="Missing query parameter 'q'"), 400

    prompt = (
        "Generate *exactly* 5 results "
        'and output *only* the JSON array (no extra text). "{query}"\n\n'
        "Respond with *only* a JSON array (no Markdown fences, no comments),\n"
        "where each element has keys: "
        "title (string), snippet (string), url (string). Under 500 tokens"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
    )
    raw = response.choices[0].message.content
    try:
        results = safe_parse_json(raw)
    except ValueError:
        results = [{"title": "Parse Error", "snippet": raw.strip(), "url": "#"}]

    return jsonify(
        {
            "results": results,
            "watermark": WATERMARK,
        }
    )


@app.route("/api/page", methods=["GET"])
def page_api():
    """Return fake HTML content based on a URL string using OpenAI."""
    url = request.args.get("url", "").strip()
    if not url:
        return jsonify(error="Missing `url` parameter"), 400

    prompt = (
        f"Generate a complete HTML page for this URL: {url}\n"
        "- Use <h1> for the title\n"
        "- Wrap each paragraph in <p>\n"
        "- Include a fixed-position watermark banner at the top right\n"
        "- Do NOT output any Markdown fences or code blocks, only raw HTML\n"
    )

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
    )
    # The model will now return pure HTML
    page_html = response.choices[0].message.content.strip()
    return jsonify({"html": page_html})


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_react(path):
    """Serve static React build files from the frontend directory."""
    build_dir = os.path.join(os.path.dirname(__file__), "frontend", "build")
    if path and os.path.exists(os.path.join(build_dir, path)):
        return send_from_directory(build_dir, path)
    return send_from_directory(build_dir, "index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5441)
