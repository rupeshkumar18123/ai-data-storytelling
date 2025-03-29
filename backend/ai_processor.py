# import openai
# from backend.config import OPENAI_API_KEY

# openai.api_key = OPENAI_API_KEY

# def generate_summary(data):
#     prompt = f"Summarize this business data: {data.head(10).to_string()}"
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response["choices"][0]["message"]["content"]
import google.generativeai as genai
from backend.config import GEMINI_API_KEY

def generate_summary(data):
    """Generates AI-powered business summary from given data using Gemini AI."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"Summarize this business data: {data.head(10).to_string()}"

    response = model.generate_content(prompt)
    return response.text if response else "No response from Gemini."

