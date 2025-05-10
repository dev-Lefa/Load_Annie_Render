import gdown
import os

def download_model():
    url = "https://drive.google.com/uc?id=1hYYCT5Wec4RhmFx5_NGmRfX-sJxLd93P"  # ลิงก์ดาวน์โหลด
    local_filename = "Annie-Ai.zip"
    
    # ตรวจสอบว่าไฟล์ยังไม่มี
    if not os.path.exists(local_filename):
        print(f"ดาวน์โหลด {local_filename}...")
        gdown.download(url, local_filename, quiet=False)
        print("ดาวน์โหลดเสร็จเรียบร้อย!")
    else:
        print(f"{local_filename} มีอยู่แล้ว")
        
# เรียกใช้งานฟังก์ชัน
download_model()
