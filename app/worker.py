import json

from app.analysis.pipeline import analyze_image
from app.crud import update_status, update_result
from app.database import SessionLocal
from app.models import ImageRecord


def process_image(image_id: str, image_path: str):

    db = SessionLocal()

    try:

        update_status(db, image_id, "processing")

        result = analyze_image(image_path)

      
        existing = (
            db.query(ImageRecord)
            .filter(
                ImageRecord.image_hash == result["image_hash"],
                ImageRecord.image_id != image_id
            )
            .first()
        )

        result["duplicate"] = existing is not None

      
        image = (
            db.query(ImageRecord)
            .filter(ImageRecord.image_id == image_id)
            .first()
        )

        image.image_hash = result["image_hash"]

        db.commit()

        update_result(
            db,
            image_id,
            json.dumps(result)
        )

    except Exception as e:

        print("\n========== ERROR ==========")
        print(type(e).__name__)
        print(e)
        print("===========================\n")

        update_result(
            db,
            image_id,
            "",
            str(e)
        )

    finally:
        db.close()