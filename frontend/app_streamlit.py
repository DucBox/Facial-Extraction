import sys
import os

# Thêm thư mục gốc của project vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import numpy as np
import cv2
import tempfile
from PIL import Image
from src.detection import HeadDetector
from src.extraction import FaceFeatureExtractor
from src.config import LABELS

# Khởi tạo model
detector = HeadDetector()
extractor = FaceFeatureExtractor()

st.title("📷 Facial Feature Extraction")

# Tạo uploader để chọn ảnh
uploaded_file = st.file_uploader("Chọn ảnh để phân tích", type=["jpg", "png", "jpeg"])

if uploaded_file:
    # Hiển thị ảnh gốc
    image = Image.open(uploaded_file)
    st.image(image, caption="Ảnh đã tải lên", use_column_width=True)

    # Lưu ảnh vào file tạm
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as temp_file:
        image.save(temp_file.name)
        temp_path = temp_file.name

    st.write("🔄 Đang xử lý ảnh, vui lòng đợi...")

    # Chạy YOLO để phát hiện đầu người
    bboxes = detector.detect_heads(temp_path)

    if not bboxes:
        st.warning("⚠ Không tìm thấy khuôn mặt nào trong ảnh.")
    else:
        st.success(f"✅ Tìm thấy {len(bboxes)} khuôn mặt!")

        # Chuyển ảnh PIL sang OpenCV format
        image_cv = cv2.imread(temp_path)

        for bbox in bboxes:
            st.write(f"📍 Phát hiện khuôn mặt tại: {bbox}")
            predictions = extractor.crop_and_classify(image_cv, bbox)

            # Hiển thị kết quả dự đoán
            st.subheader("📌 Kết quả phân tích:")
            for label, prob in zip(LABELS, predictions[0]):
                if prob > 0.5:  # Chỉ hiển thị nhãn có xác suất cao
                    st.write(f"✔ {label}: {prob:.4f}")

    st.success("✅ Xử lý hoàn tất!")
