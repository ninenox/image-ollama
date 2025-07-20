import requests
import base64

def ask_qwen_with_image(image_path, prompt, model="qwen2.5vl:3b"):
    # แปลงภาพเป็น base64
    with open(image_path, "rb") as img_file:
        image_b64 = base64.b64encode(img_file.read()).decode("utf-8")

    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "images": [image_b64],  # ✅ Qwen รองรับการส่ง image base64 ตรงนี้ได้
        "stream": False
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()["response"]

# 🧪 เรียกใช้งาน
image_path = "test.jpg"
prompt = "ในภาพนี้มีข้อความว่าอะไรบ้าง แยกบรรทัด"

answer = ask_qwen_with_image(image_path, prompt)
print("✅ คำตอบจาก Qwen:\n", answer)
