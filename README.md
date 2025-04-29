# Giggle: AI-Powered Search Reflection Engine

![Lint](https://github.com/software-students-spring2025/5-final-nofinal/actions/workflows/lint.yml/badge.svg)
![Flask CI](https://github.com/software-students-spring2025/5-final-nofinal/actions/workflows/app_ci.yml/badge.svg)
![Database CI](https://github.com/software-students-spring2025/5-final-nofinal/actions/workflows/ci_db.yml/badge.svg)
![CD](https://github.com/software-students-spring2025/5-final-nofinal/actions/workflows/deploy.yml/badge.svg)

## Project Overview
**Giggle** is a playful yet thought-provoking replica of the familiar Google search experience —
but with a twist:
**All search results and page summaries are generated entirely by AI** (via GPT models and crafted prompts).
No real web crawling or indexing occurs — **everything is imagined**.
- **Our Purpose:** This project serves as a reflection on how easy it can be to accept AI-generated content without any check.
We aim to highlight the risks of over-dependence on AI, and the gradual erosion of self-consciousness and independent thinking when facing daily questions, big or small.

Through Giggle, we encourage users to not lose their ability to reason, question, and decide for themselves.

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
MONGO_URI=mongodb://database:27017/fake_google
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
