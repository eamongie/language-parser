import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Instantiate the OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def analyze_chunks(chunks):
    analyzed_chunks = []
    for chunk in chunks:
        # Create a prompt for the Japanese language explanation
        prompt = f"Explain the grammatical role and meaning of '{chunk['text']}' in a Japanese sentence. Include details like its part of speech, grammatical usage, and meaning."

        # Use the latest ChatCompletion API through the client
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are a helpful assistant specializing in Japanese grammar and language."},
                {"role": "user", "content": prompt}
            ],
            model="gpt-3.5-turbo",  # Replace with "gpt-3.5-turbo" if needed
        )

        # Extract the explanation from the response
        explanation = response.choices[0].message.content.strip()

        # Append the chunk with its explanation
        analyzed_chunks.append({
            "text": chunk["text"],
            "role": chunk["role"],
            "color": chunk["color"],
            "explanation": explanation,
        })
    return analyzed_chunks
