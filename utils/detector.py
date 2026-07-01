from pathlib import Path

import cv2
from ultralytics import YOLO


class PedestrianDetector:

    def __init__(self, model_path="yolov8n.pt", confidence=0.25):
        self.model = YOLO(model_path)
        self.confidence = confidence
        self.target_classes = {"person"}

    def detect(self, image_path, output_path):
        image_path = Path(image_path)
        output_path = Path(output_path)

        image = cv2.imread(str(image_path))

        if image is None:
            raise ValueError("Не удалось прочитать изображение")

        results = self.model(str(image_path), conf=self.confidence)
        result = results[0]

        detected_objects = []

        for box in result.boxes:
            cls_id = int(box.cls[0])
            class_name = result.names[cls_id].lower()
            conf = float(box.conf[0])

            if class_name not in self.target_classes:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())

            detected_objects.append({
                "class_name": class_name,
                "confidence": round(conf, 3),
                "box": [x1, y1, x2, y2]
            })

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 120, 255),
                3
            )

            label = f"pedestrian {conf:.2f}"
            cv2.putText(
                image,
                label,
                (x1, max(y1 - 10, 20)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 120, 255),
                2
            )

        output_path.parent.mkdir(parents=True, exist_ok=True)
        cv2.imwrite(str(output_path), image)

        return {
            "count": len(detected_objects),
            "objects": detected_objects
        }