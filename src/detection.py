from ultralytics import YOLO
import cv2
import numpy as np
from src.config import MODEL_YOLO_PATH

class HeadDetector:
    def __init__(self):
        self.model = YOLO(MODEL_YOLO_PATH)

    def detect_heads(self, image_path):
        """
        Nhận diện đầu người từ ảnh input.
        """
        results = self.model(image_path)
        bboxes = []
        for r in results:
            for bbox_tensor in r.boxes.xyxy:
                bbox = bbox_tensor.numpy().astype(int)
                bboxes.append(bbox)
        return bboxes

# class HeadDetector:
#     def __init__(self):
#         self.model = YOLO(MODEL_YOLO_PATH)

#     def detect_heads(self, image_path):
#         """
#         Nhận diện đầu người từ ảnh input và debug output.
#         """
#         results = self.model(image_path)

#         # Print toàn bộ thông tin YOLO trả về
#         print("🔍 YOLO Output Type:", type(results))  # Kiểu dữ liệu của kết quả
#         print("🔍 YOLO Output Length:", len(results))  # Số lượng objects detect được

#         for i, r in enumerate(results):
#             print(f"\n📌 Kết quả {i+1}:")
            
#             # Nếu r có boxes
#             if hasattr(r, "boxes"):
#                 print("🔹 Bounding Boxes (raw tensor):", r.boxes)
#                 print("🔹 Bounding Boxes (numpy):", r.boxes.xyxy.numpy())  # Bbox dạng numpy
#                 print("🔹 Bounding Boxes Confidence:", r.boxes.conf.numpy())  # Độ tin cậy

#         # Trả về bounding boxes như trước
#         bboxes = []
#         for r in results:
#             print("R: ", len(r))
#             for bbox_tensor in r.boxes.xyxy:
#                 bbox = bbox_tensor.numpy().astype(int)
#                 bboxes.append(bbox)
#         print("Return: ", bboxes)
#         return bboxes
