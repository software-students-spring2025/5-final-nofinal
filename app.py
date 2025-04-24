"""Giigle web app – a fake AI-powered search engine using Flask and OpenAI."""

import os
import json
import re
from flask import Flask, request, jsonify, send_from_directory, render_template
from openai import OpenAI
from dotenv import load_dotenv
from database.operations import (
    save_search_query,
    get_recent_search_results,
    save_generated_page,
    get_generated_page
)

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

    # Check cache first
    cached_results = get_recent_search_results(query)
    if cached_results:
        return jsonify({
            "results": cached_results,
            "watermark": WATERMARK,
        })

    # Generate new results if not in cache
    prompt = (
        f"Generate *exactly* 5 results "
        f'and output *only* the JSON array (no extra text). "{query}"\n\n'
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
        # Save to database
        save_search_query(query, results)
    except Exception as e:
        results = [{
            "title": "Parse Error",
            "snippet": raw.strip(),
            "url": "#"
        }]

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

    # Check if page already exists
    existing_content = get_generated_page(url)
    if existing_content:
        return render_template(
            "page.html",
            content=existing_content,
            watermark=WATERMARK
        )

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
    page_content = response.choices[0].message.content.strip()

    return render_template(
        "page.html",
        content=page_content,
        watermark=WATERMARK
    )


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5441)
