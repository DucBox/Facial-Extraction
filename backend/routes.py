from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from backend.services import process_image
from logs.loggers import log_inference, log_system
import numpy as np

router = APIRouter()

@router.post("/predict/")
async def predict(file: UploadFile = File(...)):
    
    try:
        contents = await file.read()
        log_system(f"📥 Nhận request từ file: {file.filename}")
        results = process_image(contents)

        # Convert numpy.int64 -> int
        for face in results:
            face["bbox"] = {k: int(v) for k, v in face["bbox"].items()}  # Convert bbox values
        log_inference(f"✅ Đã xử lý 1 ảnh, phát hiện {len(results)} khuôn mặt")

        return JSONResponse(
            content={
                "status": "success",
                "num_faces_detected": int(len(results)),  # Convert len() về int chuẩn
                "faces": results
            }
        )
    except Exception as e:
        log_system(f"❌ Lỗi xử lý API: {str(e)}")
        return JSONResponse(status_code=500, content={"error": str(e)})
