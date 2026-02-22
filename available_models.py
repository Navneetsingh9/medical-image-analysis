import google.generativeai as genai
import os

GOOGLE_API_KEY = "AIzaSyDXhKK6gZPiez5eC-HEO-0TDr6ScxB9k28"
genai.configure(api_key=GOOGLE_API_KEY)

print("Models available to you on free tier:")
for model in genai.list_models():
    if 'gemini' in model.name and 'preview' not in model.name:
        print(f"✅ {model.name}")
        print(f"   Supported: {model.supported_generation_methods}")