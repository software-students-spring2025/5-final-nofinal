# Giigle: AI-Powered Search Reflection Engine

![Lint](https://github.com/software-students-spring2025/5-final-nofinal/actions/workflows/lint.yml/badge.svg)
![Flask CI](https://github.com/software-students-spring2025/5-final-nofinal/actions/workflows/app_ci.yml/badge.svg)
![Database CI](https://github.com/software-students-spring2025/5-final-nofinal/actions/workflows/ci_db.yml/badge.svg)
![CD](https://github.com/software-students-spring2025/5-final-nofinal/actions/workflows/deploy.yml/badge.svg)


## Introduction
Today’s generative AI systems are more like elaborate patchworks powered by big data than thinking machines with human-like intelligence. They stitch together layers of statistical tricks and handcrafted fixes to respond to our prompts, and they don’t really understand or check the correctness of the content that they produce. As a result, they can confidently “hallucinate” details that sound plausible but aren’t grounded in reality, but this seems to be enough to fool humans. 


With today’s technological advancements in the field of AI, it’s increasingly difficult to tell whether a paragraph or image is produced by a generative model. We all know that many people say AI is the ‘next generation of search engine”, so how about we just make it looks like one. That’s why we built **Giigle**: a fully AI-powered fake “search engine” that looks and behaves like the real thing—but every result and page is completely invented.


## Project Overview
**Giigle** is a playful yet thought-provoking replica of the familiar Google search experience —
but with a twist:
**All search results and page summaries are generated entirely by AI** (via GPT models and crafted prompts).
No real web crawling or indexing occurs — **everything is imagined**.
- **Our Purpose:** This project serves as a reflection on how easy it can be to accept AI-generated content without any check.
We aim to highlight the risks of over-dependence on AI, and the gradual erosion of self-consciousness and independent thinking when facing daily questions, big or small.

We hope to demonstrate how seamlessly AI can generate plausible-looking results, even when there’s no underlying truth, and prompt users to question the source of their information and to verify before trusting.


Through Giigle, we encourage users to not lose their ability to reason, question, and decide for themselves.

## DockerHub Container Images
| Subsystem | DockerHub Link |
|:---|:---|
| Backend (Flask) | [sophiagu/backend](https://hub.docker.com/r/sophiagu/backend) |
| Frontend | [sophiagu/frontend](https://hub.docker.com/r/sophiagu/frontend) |
| Database (MongoDB) | [mongo](https://hub.docker.com/_/mongo) |

## Team membes: 
[Sophia Gu](https://github.com/Sophbx), 

[Hans Yin](https://github.com/Hans-Yin), 

[Zifan Zhao](https://github.com/Exiam6), 

[Nick Zhu](https://github.com/NickZhuxy)

## How to Configure and Run the Project

### Prerequisites
- Docker installed (any version above 20.10)
- Docker Compose installed (v2+ integrated with Docker)
- Git installed

### Setup Instructions

#### **1. Clone the repository**
```sh
git clone https://github.com/software-students-spring2025/5-final-nofinal.git
cd YOUR_REPO
```

#### **2. Set up environment variables**
```sh
cp .env.example .env
```

#### **3. Build and start all services**
```sh
docker-compose pull
docker-compose up -d
```
This will start:
- Flask backend at http://localhost:5000
- React frontend at http://localhost:3000
- MongoDB database at localhost:27017

### Environment Variables Required
You must create a .env file at the root. Here's what it should contain:
```ini
OPENAI_API_KEY=your-openai-api-key-here
MONGODB_URI=mongodb://database:27017
DB_NAME=fake_google
```

## Secrets and Configuration
- .env file is not tracked by Git.
- An example file .env.example is provided.
- Replace dummy values with your own valid credentials.

## Starter Data Import (Optional)
If needed, you can manually insert starter data into MongoDB:
```sh
docker exec -it YOUR_DATABASE_CONTAINER_NAME mongosh
use fake_google
db.search_queries.insertOne({ query: "example search", results: [] })
db.page_summaries.insertOne({ url: "https://example.com", summary: "This is an example." })
```
