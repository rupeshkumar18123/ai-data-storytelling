def chatbot_response(query, data):
    prompt = f"Based on this data {data.to_string()}, answer: {query}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

