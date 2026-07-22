from sqlalchemy.orm import Session
from app.models import ImageRecord
from app.schemas import ImageRecordCreate


def create_image(db: Session, image_id: str, image: ImageRecordCreate):
    db_image = ImageRecord(
        image_id=image_id,
        filename=image.filename,
        image_hash=image.image_hash,
        status="pending"
    )

    db.add(db_image)
    db.commit()
    db.refresh(db_image)
    return db_image


def get_image(db: Session, image_id: str):
    return db.query(ImageRecord).filter(
        ImageRecord.image_id == image_id
    ).first()


def update_status(db: Session, image_id: str, status: str):
    image = get_image(db, image_id)

    if image:
        image.status = status
        db.commit()
        db.refresh(image)

    return image


def update_result(
    db: Session,
    image_id: str,
    result_json: str,
    failure_reason: str = None
):
    image = get_image(db, image_id)

    if image:
        image.result_json = result_json
        image.failure_reason = failure_reason
        image.status = "completed" if failure_reason is None else "failed"

        db.commit()
        db.refresh(image)

    return image
def get_result(db: Session, image_id: str):
    return db.query(ImageRecord).filter(
        ImageRecord.image_id == image_id
    ).first()