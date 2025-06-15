import os
import requests
from datetime import datetime, timezone
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("CLOCKIFY_API_KEY")
WORKSPACE_ID = os.getenv("CLOCKIFY_WORKSPACE_ID")
PROJECT_ID = os.getenv("CLOCKIFY_PROJECT_ID")
USER_ID = os.getenv("CLOCKIFY_USER_ID")

HEADERS = {"X-Api-Key": API_KEY, "Content-Type": "application/json"}


def start_time_entry(description="Focus session"):
    url = f"https://api.clockify.me/api/v1/workspaces/{WORKSPACE_ID}/time-entries"

    payload = {
        "start": datetime.now(timezone.utc).isoformat(),
        "description": description,
        "projectId": PROJECT_ID,
        "billable": False,
        "createdWith": "Lofybox",
    }

    try:
        response = requests.post(url, headers=HEADERS, json=payload)
        response.raise_for_status()
        print("✅ Entrada iniciada no Clockify.")
    except requests.RequestException as e:
        print(f"[✖] Erro ao iniciar entrada: {response.status_code} - {response.text}")


def stop_time_entry():
    url = f"https://api.clockify.me/api/v1/workspaces/{WORKSPACE_ID}/user/{USER_ID}/time-entries"
    end_time = datetime.now(timezone.utc).isoformat()

    payload = {"end": end_time}

    try:
        response = requests.patch(url, headers=HEADERS, json=payload)
        response.raise_for_status()
        print("🛑 Entrada de tempo finalizada no Clockify.")
    except requests.RequestException as e:
        print(
            f"[✖] Erro ao finalizar entrada: {response.status_code} - {response.text}-{e}"
        )
