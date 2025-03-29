import openai
from backend.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_summary(data):
    prompt = f"Summarize this business data: {data.head(10).to_string()}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

