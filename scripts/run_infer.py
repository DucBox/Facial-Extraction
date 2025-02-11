import sys
import os

# Thêm thư mục gốc của project vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import cv2
import argparse
from src.detection import HeadDetector
from src.extraction import FaceFeatureExtractor
from src.config import LABELS

# Khởi tạo model
detector = HeadDetector()
extractor = FaceFeatureExtractor()

def run_inference(image_path):
    """
    Chạy inference: phát hiện đầu + trích xuất đặc trưng khuôn mặt.
    """
    # Đọc ảnh input
    image = cv2.imread(image_path)
    print('Detecting Head ...')
    # Phát hiện đầu người
    bboxes = detector.detect_heads(image_path)
    print('Finishing Detecting Head')
    print('Extracting Face Attributes ...')
    # Chạy model ResNet trên từng vùng đầu nhận diện
    for bbox in bboxes:
        predictions = extractor.crop_and_classify(image, bbox)

        # In kết quả dự đoán
        print(f"Dự đoán cho khu vực [{bbox[0]}, {bbox[1]}, {bbox[2]}, {bbox[3]}]:")
        for label, prob in zip(LABELS, predictions[0]):
            if prob > 0.5:  # Chỉ in ra nếu xác suất > 50%
                print(f"{label}: {prob:.4f}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run face feature extraction")
    parser.add_argument("image_path", type=str, help="Path to input image")
    args = parser.parse_args()
    
    run_inference(args.image_path)
