import os
from dotenv import load_dotenv
import openai

# Load environment variables
load_dotenv()

# Get the OpenAI API key from the environment
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_chunks(chunks):
    analyzed_chunks = []
    for chunk in chunks:
        prompt = f"Explain the role and meaning of '{chunk['text']}' in the sentence. Include grammatical role, meaning, and context."
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        explanation = response['choices'][0]['message']['content'].strip()
        analyzed_chunks.append({
            "text": chunk["text"],
            "role": chunk["role"],
            "color": chunk["color"],
            "explanation": explanation
        })
    return analyzed_chunks
