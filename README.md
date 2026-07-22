# 🚗 Vehicle AI Inspector

## Intelligent Vehicle Image Processing Pipeline

Vehicle AI Inspector is an AI-powered backend application built using **FastAPI**, **OpenCV**, **SQLAlchemy**, **SQLite**, and **ImageHash**. The application accepts vehicle image uploads, processes them asynchronously, performs image quality analysis, detects vehicle number plates, identifies duplicate images using perceptual hashing (pHash), and returns structured analysis results through REST APIs.

This project was developed as part of the **Backend + AI Engineering Take-Home Assignment**.

---

# ✨ Features

- Upload vehicle images
- Background image processing
- Vehicle number plate detection
- OCR-based vehicle number extraction
- Brightness analysis
- Blur detection
- Duplicate image detection using Perceptual Hash (pHash)
- Processing status tracking
- REST APIs for upload, status, and result retrieval
- SQLite database integration
- Responsive web interface

---

# 🛠️ Technology Stack

## Backend

- Python 3.10+
- FastAPI
- SQLAlchemy
- SQLite

## Computer Vision

- OpenCV
- ImageHash
- OCR (EasyOCR/Tesseract depending on configuration)

## Frontend

- HTML
- CSS
- JavaScript
- Jinja2 Templates

---

# 📁 Project Structure

```text
vehicle-ai-inspector/
│
├── app/
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── ocr.py
│   │   ├── pipeline.py
│   │   ├── plate_detector.py
│   │   └── test_plate.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── images/
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── storage/
│   │   ├── uploads/
│   │   └── results/
│   │
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── worker.py
│
├── tests/
├── requirements.txt
├── runtime.txt
├── README.md
└── .gitignore
```

---

# 🏗️ System Architecture

```text
                 Vehicle Image
                       │
                       ▼
              Upload API (FastAPI)
                       │
                       ▼
             Store Image Metadata
                       │
                       ▼
          Background Image Processing
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
   Brightness      Blur Check    Duplicate Check
        │
        ▼
 Vehicle Number Plate Detection
        │
        ▼
     OCR Extraction
        │
        ▼
      Store Results
        │
        ▼
    SQLite Database
        │
        ▼
 Status & Result APIs
```

---

# 🔄 Processing Pipeline

1. Upload a vehicle image.
2. Save the uploaded image.
3. Store image metadata in SQLite.
4. Start background image processing.
5. Analyze image brightness.
6. Detect image blur.
7. Generate the perceptual hash (pHash).
8. Compare the image hash with previously processed images.
9. Detect the vehicle number plate.
10. Extract the vehicle registration number.
11. Store the analysis results in the database.
12. Return the processing status and final analysis.

---

# 🔍 Image Analysis

## Brightness Detection

The application calculates the average grayscale intensity of the uploaded image.

Possible results:

- Dark
- Normal
- Bright

---

## Blur Detection

Blur detection is performed using the **Variance of Laplacian** method.

Possible results:

- Blurry
- Not Blurry

---

## Duplicate Detection

Duplicate images are detected using **Perceptual Hash (pHash)** by comparing the uploaded image hash with hashes stored in the database.

---

## Vehicle Number Plate Detection

The application detects the vehicle number plate from the uploaded image and extracts the vehicle registration number using OCR.

---

# 💾 Database

SQLite stores the following information:

- Image ID
- File Name
- Processing Status
- Image Hash
- Vehicle Number
- Brightness Result
- Blur Result
- Duplicate Status
- Error Message
- Timestamp

---

# 🌐 REST API Endpoints

## Upload Image

**POST**

```
/upload
```

Example Response

```json
{
  "processing_id": "123456"
}
```

---

## Processing Status

**GET**

```
/status/{processing_id}
```

Example Response

```json
{
  "status": "processing"
}
```

Possible values:

- pending
- processing
- completed
- failed

---

## Fetch Analysis Result

**GET**

```
/result/{processing_id}
```

Example Response

```json
{
  "brightness": {
    "value": 116.70,
    "status": "Normal"
  },
  "blur": {
    "score": 1554.11,
    "status": "Not Blurry"
  },
  "vehicle_number": "MH12AB1234",
  "valid_plate": true,
  "duplicate": false
}
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/sinchana-24/vehicle-ai-inspector.git
```

Move into the project

```bash
cd vehicle-ai-inspector
```

Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
uvicorn app.main:app --reload
```

Open your browser

```
http://127.0.0.1:8000
```

---

# 🌐 Live Demo

**Render Deployment**

https://vehicle-ai-inspector.onrender.com

---

# 📊 Sample Output

| Parameter | Result |
|-----------|--------|
| Vehicle Number | MH12AB1234 |
| Plate Status | Valid |
| Brightness | Normal |
| Blur Detection | Not Blurry |
| Duplicate Image | No |

---

# 🤖 AI Usage Disclosure

AI tools were used during development for:

- Project planning
- Backend development
- UI improvements
- Debugging and troubleshooting
- Documentation assistance
- Code refactoring

All AI-assisted code was manually reviewed, tested, and integrated into the final application.

---

# ⚙️ Design Decisions

- FastAPI was selected for building REST APIs.
- SQLAlchemy was used for ORM-based database operations.
- SQLite was chosen for lightweight local storage.
- OpenCV was used for image preprocessing and analysis.
- ImageHash was used for duplicate image detection.
- Background processing is handled using a lightweight in-memory worker.

---

# ⚖️ Trade-offs

- SQLite was used instead of PostgreSQL to keep the project lightweight.
- Images are stored locally instead of cloud storage.
- Background processing uses an in-memory worker instead of Redis or RabbitMQ.
- OCR accuracy depends on image quality and number plate visibility.

---

# ❗ Error Handling

The application handles:

- Invalid image uploads
- Unsupported file formats
- Corrupted image files
- Missing vehicle number plates
- Duplicate image detection
- Processing exceptions

Failed requests are marked as **failed**, and the corresponding error message is stored in the database.

---

# 🚀 Future Improvements

- PostgreSQL integration
- Docker containerization
- Redis or RabbitMQ support
- Cloud storage integration
- Vehicle make and model recognition
- Vehicle damage detection
- Multiple vehicle detection
- Logging and monitoring

---

# 📌 Assumptions

- Uploaded images contain a visible vehicle.
- Images are uploaded in JPEG, PNG, or WEBP format.
- Duplicate detection is based on perceptual image hashing.

---

# 👩‍💻 Author

**Sinchana P**

B.E. Computer Science and Engineering

Vivekananda College of Engineering and Technology, Puttur