# Intelligent Vehicle Image Processing Pipeline

Vehicle AI Inspector is an AI-powered backend application built using **FastAPI**, **OpenCV**, **SQLAlchemy**, **SQLite**, and **ImageHash**. The application accepts vehicle image uploads, processes them asynchronously, performs image quality analysis, detects vehicle number plates, identifies duplicate images using Perceptual Hash (pHash), and returns structured analysis results through REST APIs.

This project was developed as part of the **Backend + AI Engineering Take-Home Assignment**.

---

## 🌐 Live Demo

**Application:**  
https://intelligent-media-processing-pipeline-yl2m.onrender.com

---

## 📂 GitHub Repository

https://github.com/sinchana-24/Intelligent-Media-Processing-Pipeline

---

# ✨ Features

- 📤 Upload vehicle images
- ⚙️ Background image processing
- 🚘 Vehicle number plate detection
- 🔍 OCR-based vehicle number extraction
- 🌞 Brightness analysis
- 🌫️ Blur detection
- 🧠 Duplicate image detection using Perceptual Hash (pHash)
- 📊 Processing status tracking
- 🌐 REST APIs for upload, status, and result retrieval
- 💾 SQLite database integration
- 🎨 Responsive web interface

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
- EasyOCR / Tesseract (depending on configuration)

## Frontend

- HTML
- CSS
- JavaScript
- Jinja2 Templates

---

# 📁 Project Structure

```text
Intelligent-Media-Processing-Pipeline/
│
├── app/
│   ├── analysis/
│   │   ├── __init__.py
│   │   ├── heuristics.py
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
      ┌──────────────────┼──────────────────┐
      ▼                  ▼                  ▼
 Brightness         Blur Detection    Duplicate Check
      │
      ▼
Vehicle Number Plate Detection
      │
      ▼
 OCR Text Extraction
      │
      ▼
 Store Analysis Results
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
4. Start background processing.
5. Analyze image brightness.
6. Detect image blur.
7. Generate the perceptual hash (pHash).
8. Compare with previously processed images.
9. Detect the vehicle number plate.
10. Extract the vehicle registration number using OCR.
11. Store the analysis results.
12. Return the processing status and final analysis.

---

# 🔍 Image Analysis

## 🌞 Brightness Detection

The application calculates the average grayscale intensity of the uploaded image.

Possible outputs:

- Dark
- Normal
- Bright

---

## 🌫️ Blur Detection

Blur detection is performed using the **Variance of Laplacian** method.

Possible outputs:

- Blurry
- Not Blurry

---

## 🧠 Duplicate Detection

Duplicate images are detected using **Perceptual Hash (pHash)** by comparing the uploaded image hash with hashes stored in the database.

---

## 🚘 Vehicle Number Plate Detection

The application detects the vehicle number plate from the uploaded image and extracts the registration number using OCR.

---

# 💾 Database

SQLite stores:

- Processing ID
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

```http
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

```http
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

```http
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

## Clone the Repository

```bash
git clone https://github.com/sinchana-24/Intelligent-Media-Processing-Pipeline.git
```

## Navigate to the Project

```bash
cd Intelligent-Media-Processing-Pipeline
```

## Create a Virtual Environment

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

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn app.main:app --reload
```

Open your browser:

```text
http://127.0.0.1:8000
```

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

AI-assisted tools were used during development for:

- Project planning
- Backend development
- UI improvements
- Debugging and troubleshooting
- Documentation assistance
- Code refactoring

All AI-generated code was manually reviewed, tested, and integrated into the final application.

---

# ⚙️ Design Decisions

- FastAPI for high-performance REST APIs.
- SQLAlchemy for ORM-based database management.
- SQLite for lightweight local storage.
- OpenCV for image preprocessing and computer vision.
- ImageHash for duplicate image detection.
- Background image processing using a lightweight in-memory worker.

---

# ⚖️ Trade-offs

- SQLite was selected instead of PostgreSQL to keep the project lightweight.
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
- OCR failures
- Processing exceptions

Failed requests are marked as **failed**, and the corresponding error message is stored in the database.

---

# 🚀 Future Improvements

- PostgreSQL integration
- Docker containerization
- Redis or RabbitMQ integration
- Cloud storage support
- Vehicle make and model recognition
- Vehicle damage detection
- Multiple vehicle detection
- Authentication and authorization
- Logging and monitoring
- Unit and integration testing

---

# 📌 Assumptions

- Uploaded images contain a visible vehicle.
- Supported image formats are **JPEG**, **PNG**, and **WEBP**.
- Duplicate detection is based on perceptual image hashing.
- OCR accuracy depends on image quality and plate visibility.

---

# 👩‍💻 Author

**Sinchana P**

B.E. Computer Science and Engineering

Vivekananda College of Engineering and Technology, Puttur

---

# 📄 License

This project was developed for educational and evaluation purposes as part of the **Backend + AI Engineering Take-Home Assignment**.
