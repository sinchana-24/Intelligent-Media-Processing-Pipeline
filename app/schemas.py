from pydantic import BaseModel


class ImageRecordCreate(BaseModel):
    filename: str
    image_hash: str