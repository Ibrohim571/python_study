import os
from dotenv import load_dotenv


api_key = os.environ.get("API_KEY")
database = os.environ.get("DATABASE_URL")

print(f"Using api_key: {api_key}")
