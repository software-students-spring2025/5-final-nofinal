FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install flask flask_cors pymongo openai python-dotenv

EXPOSE 5000

CMD ["python", "app.py"]
