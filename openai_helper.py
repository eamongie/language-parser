import openai

# Set your OpenAI API key
openai.api_key = "your-openai-api-key"

def analyze_chunks(chunks):
    analyzed_chunks = []
    for chunk in chunks:
        prompt = f"Explain the role and meaning of '{chunk['text']}' in a sentence. Provide details on its grammatical role, meaning, and any relevant context."
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
