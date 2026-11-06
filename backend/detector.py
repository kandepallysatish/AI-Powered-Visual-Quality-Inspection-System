from ultralytics import YOLO
import uuid
import os

model = YOLO("best.pt")

def detect_defects(image_path):
    results = model.predict(
        source=image_path,
        conf=0.35,
        imgsz=640,
        verbose=False
    )

    detections = []

    for result in results:
        for box in result.boxes:
            detections.append({
                "class": model.names[int(box.cls[0])],
                "confidence": round(float(box.conf[0]), 4),
                "bbox": [
                    round(float(x), 2)
                    for x in box.xyxy[0].tolist()
                ]
            })

        os.makedirs("uploads", exist_ok=True)

        output_path = f"uploads/{uuid.uuid4().hex}.jpg"
        result.save(filename=output_path)

    return {
        "status": "DEFECT_DETECTED" if detections else "NO_DEFECT_DETECTED",
        "total_detections": len(detections),
        "detections": detections,
        "annotated_image": "/" + output_path.replace("\\", "/")
    }