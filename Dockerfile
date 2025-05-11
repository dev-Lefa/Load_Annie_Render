# ใช้ Python 3.11 image
FROM python:3.11-slim

# ตั้ง working directory
WORKDIR /app

# คัดลอกไฟล์ requirements.txt
COPY requirements.txt .

# ติดตั้ง dependencies
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกไฟล์อื่น ๆ ของแอป
COPY . .

# คำสั่งในการรันแอป
CMD ["python", "open-webui serve"]
