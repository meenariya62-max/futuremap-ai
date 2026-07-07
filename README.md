# 🗺️ FutureMap AI – Career Recommendation Platform

> An AI-powered full-stack web application that analyzes your skills and recommends ideal tech careers using Machine Learning.

---

## 🚀 Features

- ⚡ **AI Career Prediction** – Random Forest ML model trained on skills → career mapping
- 📊 **Skill Gap Analysis** – Visual charts showing missing skills and readiness score
- 🗺️ **Learning Roadmap** – Step-by-step career path for each recommendation
- 💰 **Salary Estimation** – Real salary ranges for each tech career
- 📚 **Learning Resources** – Curated courses, YouTube channels, and docs
- 🕓 **Prediction History** – Stores and displays past predictions
- 👤 **User Authentication** – Register/Login with persistent profile
- 📈 **Modern Dashboard** – Charts, stats, and sidebar navigation

---

## 🛠️ Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Backend   | Python, Flask, Flask-CORS         |
| ML Model  | Scikit-learn (Random Forest + TF-IDF) |
| Data      | Pandas, NumPy, Joblib             |
| Frontend  | HTML5, CSS3, JavaScript (Vanilla) |
| Charts    | Chart.js                          |
| Fonts     | Google Fonts (Syne + DM Sans)     |

---

## 📁 Project Structure

```
FutureMap_AI/
├── backend/
│   ├── routes/
│   │   └── predict.py          # Flask API routes
│   ├── services/
│   │   └── model_service.py    # ML model & career data
│   ├── app.py                  # Main Flask app
│   ├── config.py               # Configuration
│   └── career_model.pkl        # Trained ML model (generated)
│
├── frontend/
│   ├── css/
│   │   └── style.css           # Full design system
│   ├── js/
│   │   ├── auth.js             # Auth logic
│   │   ├── dashboard.js        # Dashboard charts
│   │   ├── predict.js          # Prediction logic
│   │   ├── analysis.js         # Skill gap analysis
│   │   └── sidebar.js          # Shared sidebar component
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── predict.html
│   ├── analysis.html
│   ├── history.html
│   ├── profile.html
│   └── resources.html
│
├── dataset/
│   └── careers_dataset.csv     # Training data
│
├── model_training/
│   └── train_model.py          # ML training script
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Installation

### Step 1: Install Python Dependencies

```bash
cd FutureMap_AI
pip install -r requirements.txt
```

### Step 2: Train the ML Model

```bash
cd model_training
python train_model.py
```

This creates `backend/career_model.pkl`.

### Step 3: Start the Flask Backend

```bash
cd backend
python app.py
```

Backend runs at: `http://localhost:5000`

### Step 4: Open the Frontend

Open `frontend/login.html` in your browser — or use **Live Server** in VS Code.

> ✅ Click "Try Demo" on the login page to skip registration.

---

## 🔌 API Endpoints

| Method | Endpoint        | Description              |
|--------|-----------------|--------------------------|
| POST   | `/api/predict`  | Predict career from skills |
| GET    | `/api/history`  | Get prediction history   |
| GET    | `/api/careers`  | Get all career tracks    |
| POST   | `/api/register` | Register new user        |
| POST   | `/api/login`    | Login user               |
| GET    | `/api/profile`  | Get user profile         |
| GET    | `/api/health`   | API health check         |

### Example Request

```json
POST /api/predict
{
  "name": "Riya",
  "skills": "python, machine learning, tensorflow, deep learning"
}
```

### Example Response

```json
{
  "name": "Riya",
  "recommended_career": "AI Engineer",
  "confidence": "87.0%",
  "top_matches": [
    { "career": "AI Engineer", "confidence": 87.0 },
    { "career": "Data Scientist", "confidence": 72.5 },
    { "career": "NLP Engineer", "confidence": 61.0 }
  ],
  "missing_skills": ["keras", "data analysis"],
  "readiness_score": 71.4,
  "roadmap": ["Learn Python", "Master Statistics...", ...],
  "salary": "₹8 LPA – ₹25 LPA",
  "resources": [...]
}
```

---

## 🎨 Pages Overview

| Page              | Description                                  |
|-------------------|----------------------------------------------|
| `login.html`      | Sign in with email/password or demo access   |
| `register.html`   | Create new account                           |
| `dashboard.html`  | Overview with charts and recent predictions  |
| `predict.html`    | Enter skills → get AI career prediction      |
| `analysis.html`   | Deep skill gap analysis with charts          |
| `history.html`    | View all past predictions with pie chart     |
| `profile.html`    | User profile and activity stats              |
| `resources.html`  | Curated learning resources (filterable)      |

---

## 👨‍💻 Built With

- **ML Algorithm**: Random Forest Classifier + TF-IDF Vectorizer
- **16 Career Tracks**: AI Engineer, Data Scientist, Full Stack, DevOps, Cloud Architect, Blockchain, NLP, Computer Vision, and more
- **24+ Resources**: Courses, YouTube channels, documentation

---

## 📌 Notes for Interview

- Model is trained on a custom dataset mapping skills → careers
- Falls back to rule-based matching if model file not found
- All prediction history is stored in `backend/prediction_history.json`
- Frontend uses vanilla JS — no framework needed
- Charts powered by Chart.js (CDN)

---

*Made with ❤️ as a major portfolio project*
