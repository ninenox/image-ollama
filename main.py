import requests
import base64

def ask_ollama_with_image(image_path, prompt, model="moondream:v2"):
    # โหลดรูปและ encode เป็น base64
    with open(image_path, "rb") as img_file:
        image_base64 = base64.b64encode(img_file.read()).decode('utf-8')

    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "images": [image_base64],  # 🔍 ใส่ภาพใน array
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()['response']

# เรียกใช้งาน
prompt = "ในภาพนี้มีข้อความว่าอะไรบ้าง แยกเป็นบรรทัด"
image_path = "test.jpg"

answer = ask_ollama_with_image(image_path, prompt)
print("📝 คำตอบจาก Ollama:\n", answer)
