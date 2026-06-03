# 🌿 AI Plant Disease Detection & Recommendation System

An AI-powered agricultural assistant that combines **Deep Learning (CNN)** and **Large Language Models (LLMs)** to identify plant diseases from leaf images and provide intelligent treatment recommendations.

The system uses a CNN model trained on plant disease datasets to classify diseases from uploaded leaf images. After prediction, an LLM generates disease descriptions, causes, treatment suggestions, and prevention strategies, making the application a complete AI Plant Doctor.

---

## 🚀 Features

### 🔍 Disease Detection

* Upload plant leaf images
* CNN-based disease classification
* Real-time prediction
* Confidence score visualization
* Support for multiple crop categories

### 🤖 AI-Powered Recommendations

* Disease description
* Causes and symptoms
* Treatment recommendations
* Prevention strategies
* LLM-generated agricultural guidance

### 🌐 Modern Full-Stack Application

* FastAPI backend
* Streamlit frontend
* Interactive dashboard
* Real-time image analysis

---

## 🧠 AI Architecture

```text
Leaf Image
     │
     ▼
CNN Model (TensorFlow/Keras)
     │
     ▼
Disease Prediction
     │
     ▼
LLM Recommendation Engine
     │
     ▼
Description + Treatment + Prevention
```

---

## 🛠️ Tech Stack

### Deep Learning

* TensorFlow
* Keras
* NumPy

### Backend

* FastAPI
* Uvicorn
* Python

### Frontend

* Streamlit

### AI / LLM

* Groq API
* Llama 3

### Image Processing

* Pillow (PIL)

### Deployment

* Render

---

## 📂 Project Structure

```text
plant-disease-prediction/
│
├── backend/
│   ├── main.py
│   ├── models/
│   │   ├── plant_disease_prediction_model.keras
│   │   └── class_indices.json
│   │
│   └── services/
│       ├── prediction.py
│       └── llm.py
│
├── frontend/
│   └── app.py
│
├── notebook/
│   └── plant_disease_prediction.ipynb
│
├── screenshots/
│
├── requirements.txt
├── .env
└── README.md
```

---

## 📊 Example Output

### Disease Prediction

```text
Disease: Strawberry - Leaf Scorch
Confidence: 98.7%
```

### AI Recommendation

```text
Description:
Leaf scorch is a fungal disease affecting strawberry plants.

Causes:
• Excess moisture
• Poor air circulation

Treatment:
• Remove infected leaves
• Apply fungicide
• Avoid overhead irrigation

Prevention:
• Maintain proper spacing
• Monitor humidity levels
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/plant-disease-prediction.git
cd plant-disease-prediction
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Run the Backend

```bash
uvicorn backend.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Run the Frontend

```bash
streamlit run frontend/app.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## 🚀 Deployment on Render

### Create a New Web Service

1. Push code to GitHub
2. Login to Render
3. Create a new Web Service
4. Connect your GitHub repository

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

### Environment Variables

```text
GROQ_API_KEY=your_groq_api_key
```

---

## 🌐 Live Demo

### Frontend

```text
https://your-frontend-url
```

### Backend API

```text
https://your-render-backend-url
```

---

## 📦 Model File

If the model file is too large for GitHub:

1. Upload the model to Google Drive
2. Create a shareable link
3. Download and place it inside:

```text
backend/models/
```

Required files:

```text
backend/models/
├── plant_disease_prediction_model.keras
└── class_indices.json
```

---

## ⚠️ Common Error

### Error

```text
Unrecognized keyword arguments passed to Dense:
{'quantization_config': None}
```

### Solution

This occurs because of TensorFlow/Keras version mismatch.

Install compatible versions:

```bash
pip install tensorflow==2.20.0
pip install keras==3.10.0
```

If the issue persists:

* Re-save the model using the latest Keras version
* Export again in `.keras` format

```python
model.save("plant_disease_prediction_model.keras")
```

---

## 🎯 Future Improvements

* Disease severity estimation
* Multi-language support
* Mobile-friendly UI
* Docker deployment
* CI/CD pipeline
* User authentication
* Disease history tracking
* RAG-based agricultural knowledge assistant

---

## 👨‍💻 Author

**Indrapal Singh**

NIT Warangal

Interests:

* Machine Learning
* Deep Learning
* Generative AI
* Full-Stack AI Applications

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
# AI-Plant-Disease-Detection-Recommendation-System
