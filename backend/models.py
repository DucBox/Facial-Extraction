from pydantic import BaseModel
from typing import List, Tuple

class BoundingBox(BaseModel):
    x_min: int
    y_min: int
    x_max: int
    y_max: int

class FaceResult(BaseModel):
    """
    Thông tin về mỗi khuôn mặt nhận diện được.
    """
    bbox: BoundingBox
    features: Dict[str, float]  # Đặc điểm nhận diện được từ model (râu, kính, v.v.)

class PredictionResponse(BaseModel):
    """
    Định nghĩa format response của API /predict/.
    """
    status: str  # Trạng thái API (success hoặc error)
    num_faces_detected: int  # Số khuôn mặt phát hiện được
    faces: List[FaceResult]  # Danh sách khuôn mặt và đặc điểm nhận diện được