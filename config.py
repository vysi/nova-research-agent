import os
from dotenv import load_dotenv

load_dotenv()

# AWS Configuration
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

# Nova Model Configuration
NOVA_MODEL_ID = "us.amazon.nova-pro-v1:0"  # Nova Pro model
NOVA_LITE_MODEL_ID = "us.amazon.nova-lite-v1:0"  # Nova Lite for faster responses

# Research Configuration
MAX_SEARCH_RESULTS = 5
MAX_CONTENT_LENGTH = 5000
RESEARCH_CACHE_DIR = "research_cache"
