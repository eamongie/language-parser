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
        # Create a prompt specific to Japanese NLP
        prompt = f"Explain the grammatical role and meaning of '{chunk['text']}' in a Japanese sentence. Include details like its part of speech, grammatical usage, and meaning."

        # Use the latest ChatCompletion method
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a helpful assistant specializing in Japanese grammar and language."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract explanation from the response
        explanation = response['choices'][0]['message']['content'].strip()

        # Append the analyzed chunk with its explanation
        analyzed_chunks.append({
            "text": chunk["text"],
            "role": chunk["role"],
            "color": chunk["color"],
            "explanation": explanation
        })
    return analyzed_chunks
