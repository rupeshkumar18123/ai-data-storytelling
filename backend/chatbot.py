<<<<<<< HEAD

=======
# def chatbot_response(query, data):
#     prompt = f"Based on this data {data.to_string()}, answer: {query}"
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response["choices"][0]["message"]["content"]


import google.generativeai as genai
from backend.config import GEMINI_API_KEY

def chatbot_response(query, data):
    """Gemini-powered chatbot that answers user queries based on business data."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"Based on this data {data.to_string()}, answer: {query}"

    response = model.generate_content(prompt)
    return response.text if response else "No response from Gemini."
>>>>>>> 9c09285269c4bc97d3d7f6e26f5008d06be67bd1
