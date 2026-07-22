import os
import uuid
import shutil

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Depends,
    HTTPException,
    BackgroundTasks,
    Request
)
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import Base, engine, get_db
from app.schemas import ImageRecordCreate
from app.crud import (
    create_image,
    get_image,
    get_result
)
from app.worker import process_image


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Vehicle Image Processing API")


app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(directory="app/templates")


UPLOAD_FOLDER = "app/storage/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)



@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )



@app.post("/upload")
async def upload_image(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    if not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Only image files are allowed."
        )

    image_id = str(uuid.uuid4())

    file_path = os.path.join(
        UPLOAD_FOLDER,
        f"{image_id}_{file.filename}"
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    image = ImageRecordCreate(
        filename=file.filename,
        image_hash="pending"
    )

    create_image(
        db,
        image_id,
        image
    )

    background_tasks.add_task(
        process_image,
        image_id,
        file_path
    )

    return {
        "processing_id": image_id,
        "status": "pending",
        "filename": file.filename
    }


@app.get("/status/{image_id}")
def get_status(
    image_id: str,
    db: Session = Depends(get_db)
):

    image = get_image(
        db,
        image_id
    )

    if image is None:
        raise HTTPException(
            status_code=404,
            detail="Image not found"
        )

    return {
        "processing_id": image.image_id,
        "status": image.status
    }



@app.get("/result/{image_id}")
def get_result_api(
    image_id: str,
    db: Session = Depends(get_db)
):

    image = get_result(
        db,
        image_id
    )

    if image is None:
        raise HTTPException(
            status_code=404,
            detail="Image not found"
        )

    return {
        "processing_id": image.image_id,
        "status": image.status,
        "result": image.result_json,
        "failure_reason": image.failure_reason
    }