import cv2
import imagehash
from PIL import Image

from app.analysis.plate_detector import detect_plate


def analyze_image(image_path: str):

    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    brightness = gray.mean()

    if brightness < 80:
        brightness_status = "Dark"
    elif brightness < 180:
        brightness_status = "Normal"
    else:
        brightness_status = "Bright"


    blur_score = cv2.Laplacian(
        gray,
        cv2.CV_64F
    ).var()

    if blur_score < 100:
        blur_status = "Blurry"
    else:
        blur_status = "Not Blurry"


    img_hash = str(
        imagehash.phash(
            Image.open(image_path)
        )
    )



    vehicle_number, valid_plate = detect_plate(image_path)

    return {

        "brightness": {
            "value": round(float(brightness), 2),
            "status": brightness_status
        },

        "blur": {
            "score": round(float(blur_score), 2),
            "status": blur_status
        },

        "image_hash": img_hash,

        "duplicate": False,

        "vehicle_number": vehicle_number,

        "valid_plate": valid_plate
    }