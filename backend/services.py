import sys
import os

# Thêm thư mục gốc của project vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import cv2
import numpy as np
from src.detection import HeadDetector
from src.extraction import FaceFeatureExtractor
from src.utils import preprocess_image
from src.config import LABELS

detector = HeadDetector()
extractor = FaceFeatureExtractor()

def process_image(image_bytes):
    """
    Nhận ảnh, chạy YOLO & ResNet, trả về danh sách khuôn mặt + đặc điểm nhận diện.
    """
    image_np = np.array(cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR))
    
    # Phát hiện đầu
    bboxes = detector.detect_heads(image_np)
    # print('Head Detection Phase')
    # print(bboxes)

    results = []
    for bbox in bboxes:
        predictions = extractor.crop_and_classify(image_np, bbox)
        # print('Facial Extraction Phase')
        # print(predictions)
        detected_labels = {label: float(prob) for label, prob in zip(LABELS, predictions[0]) if prob > 0.5}

        face_info = {
            "bbox": {"x_min": bbox[0], "y_min": bbox[1], "x_max": bbox[2], "y_max": bbox[3]},
            "features": detected_labels
        }
        results.append(face_info)
    # print(results)
    return results  # Trả về danh sách khuôn mặt + đặc điểm

#Test services.py
# with open("/Users/ngoquangduc/Desktop/AI_Project/Facial_Extraction/data/test/img_1.jpg", "rb") as f:
#     image_bytes = f.read()
#     print(process_image(image_bytes))  # Kiểm tra output có đúng không
