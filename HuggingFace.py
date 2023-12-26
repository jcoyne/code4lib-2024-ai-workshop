import requests

MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"
HOST = "https://api-inference.huggingface.co"

class HuggingFace:
  def __init__(self, api_token):
    self.api_token = api_token

  def embedding(self, payload):
    headers = {"Authorization": f"Bearer {self.api_token}"}
    API_URL = f"{HOST}/pipeline/feature-extraction/{MODEL_ID}"
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


