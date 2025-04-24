import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get MongoDB connection string from environment variable
MONGO_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017')
DB_NAME = os.getenv('DB_NAME', 'giigle')

# Create a MongoDB client
client = MongoClient(MONGO_URI)
db = client[DB_NAME]

# Collections
search_queries = db.search_queries
generated_pages = db.generated_pages

def init_db():
    """Initialize database with indexes"""
    # Create indexes for better query performance
    search_queries.create_index('query')
    search_queries.create_index('timestamp')
    generated_pages.create_index('url', unique=True)
    generated_pages.create_index('generated_at')
