import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CLOCKIFY_API_KEY")
WORKSPACE_ID = os.getenv("CLOCKIFY_WORKSPACE_ID")

HEADERS = {"X-Api-Key": API_KEY, "Content-Type": "application/json"}

url = f"https://api.clockify.me/api/v1/workspaces/{WORKSPACE_ID}/projects"

response = requests.get(url, headers=HEADERS)

for project in response.json():
    if not project.get("archived", False):
        print(f"{project['name']} → {project['id']}")
