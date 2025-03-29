 
<<<<<<< HEAD
=======
import google.generativeai as genai

genai.configure(api_key="AIzaSyB76L5mvSDPmG6W5pAFC5s5B-b49oVpucY")

# List available models
models = genai.list_models()
for model in models:
    print(model.name)
>>>>>>> 9c09285269c4bc97d3d7f6e26f5008d06be67bd1
