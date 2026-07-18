import os
import requests
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-mnli"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}"
}


def rule_based_classifier(description):
    description = description.lower()

    if "payment" in description or "server down" in description:
        return "Urgent"

    elif "login" in description or "password" in description:
        return "High"

    elif "bug" in description or "slow" in description:
        return "Medium"

    return "Low"


def ai_classifier(description):

    try:
        payload = {
            "inputs": description,
            "parameters": {
                "candidate_labels": [
                    "Urgent",
                    "High",
                    "Medium",
                    "Low"
                ]
            }
        }

        response = requests.post(
            API_URL,
            headers=HEADERS,
            json=payload,
            timeout=15
        )

        result = response.json()

        if "labels" in result:
            return result["labels"][0]

    except Exception:
        pass

    # If the API fails, use the rule-based classifier
    return rule_based_classifier(description)