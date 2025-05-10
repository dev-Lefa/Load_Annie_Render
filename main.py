import gdown
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Annie-Ai is running!'

def download_model():
    url = "https://drive.google.com/uc?id=1hYYCT5Wec4RhmFx5_NGmRfX-sJxLd93P"
    local_filename = "Annie-Ai.zip"
    if not os.path.exists(local_filename):
        print(f"ดาวน์โหลด {local_filename}...")
        gdown.download(url, local_filename, quiet=False)
        print("ดาวน์โหลดเสร็จเรียบร้อย!")
    else:
        print(f"{local_filename} มีอยู่แล้ว")

if __name__ == "__main__":
    download_model()
    port = int(os.environ.get("PORT", 5000))  # ใช้พอร์ตที่ Render กำหนด
    app.run(host='0.0.0.0', port=port)
