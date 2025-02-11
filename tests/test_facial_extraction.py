import sys
import os
import cv2
# Thêm thư mục gốc của project vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.extraction import FaceFeatureExtractor

# Định nghĩa ảnh và bbox
img_path = "/Users/ngoquangduc/Desktop/AI_Project/Facial_Extraction/data/test/img_2.jpeg"
bboxes = [[453, 762, 639, 980], [294, 642, 470, 855]]

# Load ảnh
image = cv2.imread(img_path)

# Khởi tạo model
extractor = FaceFeatureExtractor()

# Chạy inference trên từng khuôn mặt
for bbox in bboxes:
    extractor.crop_and_classify(image, bbox)
