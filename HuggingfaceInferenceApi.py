import requests
import os

def query(payload):
    api_token = os.environ["HUGGING_FACE_API_TOKEN"]
    headers = {"Authorization": f"Bearer {api_token}"}
    API_URL = "https://api-inference.huggingface.co/pipeline/feature-extraction/sentence-transformers/all-MiniLM-L6-v2"
    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()
    if isinstance(data, dict):
      raise SystemExit("ERROR: " + data['error'])
    return data
