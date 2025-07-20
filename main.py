import requests
import base64

# STEP 1: Encode image เป็น embedding
def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read()).decode('utf-8')

    response = requests.post(
        "http://localhost:11434/api/embeddings",
        json={"model": "moondream:v2", "image": image_base64}
    )
    response.raise_for_status()
    return response.json()["embedding"]

# STEP 2: ส่ง prompt พร้อม embedding
def ask_with_image_embedding(embedding, prompt, model="moondream:v2"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "embedding": embedding,
            "stream": False
        }
    )
    response.raise_for_status()
    return response.json()["response"]

# RUN
image_path = "test.jpg"
prompt = "ในภาพนี้มีข้อความว่าอะไรบ้าง แยกบรรทัด"

embedding = encode_image(image_path)
answer = ask_with_image_embedding(embedding, prompt)
print("✅ คำตอบจาก Ollama:\n", answer)
