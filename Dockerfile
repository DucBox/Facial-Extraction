# Sử dụng Python 3.9 làm base image
FROM python:3.9-slim

# Thiết lập thư mục làm việc trong container
WORKDIR /app

# Cài đặt các dependencies cần thiết cho OpenCV, GLIBC và hệ thống
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    ffmpeg\
    libsm6\
    libxext\
    && rm -rf /var/lib/apt/lists/*


# Copy toàn bộ mã nguồn vào container
COPY . /app

# Tạo và kích hoạt môi trường ảo (venv)
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Cài đặt các thư viện từ requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Mở cổng mặc định của FastAPI
EXPOSE 8000

# Thiết lập lệnh chạy API FastAPI khi container khởi động
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
