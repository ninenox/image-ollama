import requests
import base64

# STEP 1: encode image to embedding
def encode_image_to_embedding(image_path, model="moondream:v2"):
    with open(image_path, "rb") as img:
        image_b64 = base64.b64encode(img.read()).decode("utf-8")

    url = "http://localhost:11434/api/embeddings"
    payload = {
        "model": model,
        "image": image_b64
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["embedding"]

# STEP 2: generate answer with prompt and embedding
def ask_ollama_with_embedding(prompt, embedding, model="moondream:v2"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "embedding": embedding,
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["response"]

# RUN
image_path = "test.jpg"
prompt = "ในภาพนี้มีข้อความอะไรบ้าง แยกเป็นบรรทัด"

embedding = encode_image_to_embedding(image_path)
answer = ask_ollama_with_embedding(prompt, embedding)

print("✅ คำตอบจาก Ollama:\n", answer)
