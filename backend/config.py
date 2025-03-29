<<<<<<< HEAD
=======
# import os
# from dotenv import load_dotenv

# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
>>>>>>> 9c09285269c4bc97d3d7f6e26f5008d06be67bd1

