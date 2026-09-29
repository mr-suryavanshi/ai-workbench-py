import time
from dotenv import load_dotenv
from google import genai
from google.genai import errors

load_dotenv()
client = genai.Client()

MODELS = ["gemini-3.8-flash", "gemini-3.7-flash", "gemini-3.5-flash-lite"]

def ask_llm(prompt):
    for model in MODELS:
        for attempt in range(3):
            try:
                response = client.models.generate_content(
                    model=model,
                    contents=prompt,
                )
                return response.text
            except errors.ServerError:
                print(f"{model} is busy (attempt {attempt + 1}/3), retrying...")
                time.sleep(2 ** attempt) 
    raise RuntimeError("All models are busy. Please try again later.")

print(ask_llm("Write a poem about the beauty of nature."))