# 🚀 AI-Powered Visual Quality Inspection System

An AI-powered industrial quality inspection application that uses **YOLO11, Google Agent Development Kit (ADK), FastAPI, and React** to automatically identify and localize damaged packages through computer vision.

The system analyzes uploaded product images, detects packaging defects using a custom-trained YOLO11 model, and generates AI-assisted inspection reports with defect categories, confidence scores, bounding-box coordinates, and quality recommendations.

## 🎯 Project Highlights

- **Automated Defect Detection:** Identifies package-related defects using a custom-trained YOLO11 object detection model.
- **Visual Localization:** Highlights detected defects using bounding boxes and annotated images.
- **AI Inspection Assistant:** Integrates Google ADK with Gemini to generate human-readable quality inspection reports.
- **REST API Integration:** Uses FastAPI to handle image uploads, model inference, and inspection responses.
- **Interactive Dashboard:** Provides a React-based interface for uploading images and reviewing inspection results.
- **Containerized Application:** Uses Docker and Docker Compose to simplify application setup and execution.

## 🧠 System Architecture & Technology

The application follows a modular architecture where computer vision handles defect detection and the AI agent provides inspection explanations.

```text
                 User
                  |
                  ▼
           React Dashboard
                  |
                  ▼
             FastAPI
                  |
                  ▼
             YOLO11 Model
               best.pt
                  |
          Defect Detection
                  |
                  ▼
          Structured Results
                  |
                  ▼
          Google ADK Agent
                  |
                  ▼
           Gemini API
                  |
                  ▼
         AI Inspection Report
```

**Technology Stack**

| Component | Technologies |
|---|---|
| Frontend | React, Vite, JavaScript, CSS |
| Backend | Python, FastAPI, Uvicorn |
| Computer Vision | YOLO11, Ultralytics, OpenCV |
| AI Agent | Google ADK, Gemini |
| Model Training | Kaggle, PyTorch, YOLO11 |
| Dataset | Roboflow Package Detection |
| Containerization | Docker, Docker Compose |
| Version Control | Git, GitHub, Git LFS |

## 🔍 Inspection Workflow & Results

1. Upload a package image through the React dashboard.
2. FastAPI receives and validates the uploaded image.
3. The trained YOLO11 model processes the image and detects objects belonging to its trained classes.
4. Detection results include class labels, confidence scores, and bounding-box coordinates.
5. Google ADK uses the structured detection results to generate an AI-assisted inspection explanation.
6. The dashboard displays the annotated image, detection details, and inspection report.

**Sample Inspection Screenshots**

> 📸 Screenshots will be added here.

<!-- Add your application screenshots below -->

<!--
![Application Dashboard](screenshots/dashboard.png)
![Defect Detection](screenshots/defect-detection.png)
![Inspection Report](screenshots/inspection-report.png)
-->

## ⚙️ Project Setup & Execution

**Prerequisites**

- Python 3.11+
- Node.js 22+
- Docker Desktop
- Git and Git LFS
- Gemini API key

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd visual-quality-inspection
```

**2. Retrieve the trained YOLO model**

The trained `best.pt` model is maintained using Git LFS.

```bash
git lfs install
git lfs pull
```

Ensure the model exists at:

```text
backend/best.pt
```

**3. Configure environment variables**

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

**4. Start the application using Docker**

```bash
docker compose up --build -d
```

**5. Access the application**

| Service | URL |
|---|---|
| React Dashboard | http://localhost:5173 |
| FastAPI Backend | http://localhost:8000 |
| API Documentation | http://localhost:8000/docs |

**Useful Docker Commands**

```bash
# View running containers
docker compose ps

# View application logs
docker compose logs -f

# Stop application
docker compose down

# Rebuild application
docker compose up --build -d
```

## 🛠️ Engineering Learnings & Future Scope

**Key Learnings**

- Training and evaluating custom YOLO11 object detection models.
- Integrating computer vision models into FastAPI applications.
- Building AI agents with Google ADK and custom Python tools.
- Designing image-processing and inference pipelines.
- Containerizing full-stack applications with Docker Compose.
- Managing large machine learning model files using Git LFS.
- Integrating React frontend applications with REST APIs.

**Future Enhancements**

- Real-time camera-based quality inspection.
- Defect severity classification and quality scoring.
- Inspection history and analytics dashboard.
- Database integration for inspection records.
- PDF inspection report generation.
- Authentication and role-based access control.
- AWS deployment with GitHub Actions CI/CD.
- Production monitoring and model performance tracking.

---

**👨‍💻 Author**
Satish Kandepally (https://github.com/kandepallysatish)

Python Developer | Machine Learning | Deep Learning | Computer Vision | FastAPI | Generative AI | Docker

If this project was helpful, drop a ⭐.