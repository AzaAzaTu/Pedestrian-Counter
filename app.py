from pathlib import Path
from uuid import uuid4

from flask import Flask, render_template, request, url_for, flash
from werkzeug.utils import secure_filename

from utils.detector import PedestrianDetector
from utils.db import init_db, add_request, get_history


BASE_DIR = Path(__file__).resolve().parent

UPLOAD_DIR = BASE_DIR / "static" / "uploads"
RESULT_DIR = BASE_DIR / "static" / "results"

ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png", "webp"}


app = Flask(__name__)
app.secret_key = "pedestrian-counter-secret-key"

app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
RESULT_DIR.mkdir(parents=True, exist_ok=True)

init_db()

detector = PedestrianDetector(
    model_path="yolov8n.pt",
    confidence=0.25
)


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@app.route("/", methods=["GET", "POST"])
def index():
    result_image = None
    uploaded_image = None
    pedestrian_count = None
    objects = []

    if request.method == "POST":
        if "image" not in request.files:
            flash("Файл не был передан.")
            return render_template("index.html", history=get_history())

        file = request.files["image"]

        if file.filename == "":
            flash("Выберите изображение.")
            return render_template("index.html", history=get_history())

        if not allowed_file(file.filename):
            flash("Разрешены только файлы JPG, JPEG, PNG и WEBP.")
            return render_template("index.html", history=get_history())

        original_filename = secure_filename(file.filename)
        extension = original_filename.rsplit(".", 1)[1].lower()

        unique_name = f"{uuid4().hex}.{extension}"
        upload_path = UPLOAD_DIR / unique_name

        result_name = f"result_{uuid4().hex}.jpg"
        result_path = RESULT_DIR / result_name

        file.save(upload_path)

        try:
            detection_result = detector.detect(upload_path, result_path)

            pedestrian_count = detection_result["count"]
            objects = detection_result["objects"]

            uploaded_image = url_for("static", filename=f"uploads/{unique_name}")
            result_image = url_for("static", filename=f"results/{result_name}")

            add_request(
                original_filename=original_filename,
                upload_path=f"uploads/{unique_name}",
                result_path=f"results/{result_name}",
                pedestrian_count=pedestrian_count,
                confidence=detector.confidence
            )

        except Exception as error:
            flash(f"Ошибка обработки изображения: {error}")

    history = get_history()

    return render_template(
        "index.html",
        uploaded_image=uploaded_image,
        result_image=result_image,
        pedestrian_count=pedestrian_count,
        objects=objects,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)