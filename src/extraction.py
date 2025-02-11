import cv2
import numpy as np
from tensorflow.keras.models import load_model
from src.utils import preprocess_image
from src.config import MODEL_RESNET_PATH, LABELS

class FaceFeatureExtractor:
    def __init__(self):
        self.model = load_model(MODEL_RESNET_PATH, compile = False)

    def crop_and_classify(self, image, bbox):
        """
        Cắt vùng đầu từ ảnh và chạy model ResNet để trích xuất đặc trưng khuôn mặt.
        """
        x_min, y_min, x_max, y_max = bbox
        cropped_image = image[y_min:y_max, x_min:x_max]
        input_data = preprocess_image(cropped_image)
        predictions = self.model.predict(input_data)
        return predictions

# class FaceFeatureExtractor:
#     def __init__(self):
#         print("🚀 Loading model from:", MODEL_RESNET_PATH)
#         self.model = load_model(MODEL_RESNET_PATH, compile=False)
#         print("✅ Model Loaded Successfully!")

#     def crop_and_classify(self, image, bbox):
#         """
#         Cắt vùng đầu từ ảnh và chạy model ResNet để trích xuất đặc trưng khuôn mặt.
#         """
#         print("\n📌 Processing Bounding Box:", bbox)
#         x_min, y_min, x_max, y_max = bbox
#         cropped_image = image[y_min:y_max, x_min:x_max]

#         # Kiểm tra kích thước ảnh sau khi crop
#         print("🔍 Cropped Image Shape:", cropped_image.shape)

#         # Tiền xử lý ảnh
#         input_data = preprocess_image(cropped_image)
#         print("🔍 Processed Image Shape:", input_data.shape)

#         # Kiểm tra model trước khi dự đoán
#         print("🚀 Running Prediction...")
#         predictions = self.model.predict(input_data)
#         print("✅ Prediction Done!")

#         # Print kết quả dự đoán
#         print("📌 Raw Predictions:", predictions)

#         # Nếu LABELS là danh sách tên class, ánh xạ giá trị dự đoán
#         if LABELS:
#             prediction_dict = {LABELS[i]: float(predictions[0][i]) for i in range(len(LABELS))}
#             print("🔍 Mapped Predictions:", prediction_dict)

#         return predictions
