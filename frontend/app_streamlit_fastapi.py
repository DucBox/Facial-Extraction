import streamlit as st
from PIL import Image
import requests
import tempfile

st.title("📷 Facial Feature Extraction")
uploaded_file = st.file_uploader("Chọn ảnh để phân tích", type=["jpg", "png", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh đã tải lên", use_container_width=True)

API_URL = "http://127.0.0.1:8000/predict/"

# API_URL = "https://your-api.railway.app/predict/"

if uploaded_file:
    # Lưu ảnh tạm thời
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        image.save(temp_file.name)

    st.write("🔄 Đang gửi ảnh đến FastAPI để xử lý...")

    # Gửi request đến FastAPI
    with open(temp_file.name, "rb") as f:
        files = {"file": f}
        response = requests.post(API_URL, files=files)

    if response.status_code == 200:
        data = response.json()
        print(data)
        st.success(f"✅ Tìm thấy {data['num_faces_detected']} khuôn mặt!")

        for face in data["faces"]:
            st.write(f"📍 Khuôn mặt tại: {face['bbox']}")
            st.write("📌 Đặc điểm nhận diện:")
            for label, prob in face["features"].items():
                st.write(f"✔ {label}: {prob:.4f}")

    else:
        st.error("❌ Không nhận được kết quả hợp lệ từ API.")
