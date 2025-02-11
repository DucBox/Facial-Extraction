import requests

# Địa chỉ API FastAPI (đảm bảo FastAPI đã chạy trên đúng host)
API_URL = "http://127.0.0.1:8000/predict/"

# Đọc file ảnh cần test
image_path = "/Users/ngoquangduc/Desktop/AI_Project/Facial_Extraction/data/test/img_1.jpg"  # Đổi thành ảnh cần test
files = {"file": open(image_path, "rb")}

# Gửi request đến API
response = requests.post(API_URL, files=files)

# Kiểm tra phản hồi từ API
if response.status_code == 200:
    print("✅ API hoạt động tốt!")
    print("📌 Response từ API:")
    print(response.json())
else:
    print("❌ API gặp lỗi!")
    print("🔴 Status Code:", response.status_code)
    print("📝 Nội dung lỗi:", response.text)
