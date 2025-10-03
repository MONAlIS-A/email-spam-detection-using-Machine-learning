# 📧 Email Spam Detection using Machine Learning

This project combines machine learning and web development to classify emails as **spam** or **ham (not spam)**. It includes a trained ML model and a user-friendly web interface for real-time predictions.

## 🖥️ Running Locally

To run this project on your local machine, follow these steps:

### 1. 📦 Clone the Repository

```bash
git clone https://github.com/MONAlIS-A/email-spam-detection-using-Machine-learning.git
cd email-spam-detection-using-Machine-learning
```

### 2. 🧪 Create a Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
cd mlprojects
```

### 3. 📚 Install Dependencies
pip install -r requirements.txt

### 4. 🚀 Start the Web Application
python manage.py runserver

### 5. 🌐 Access the Web Interface
http://127.0.0.1:8000/

## 🔍 Overview

Spam emails are a major nuisance in digital communication. This project automates spam detection using machine learning and presents the results through a clean web dashboard.

### ✅ Key Features

- NLP-based text preprocessing
- Multiple ML classifiers (Naive Bayes, Random Forest, logistic Regression)
- Confusion matrix and performance metrics
- Web interface for live predictions

## 🧠 ML Workflow

1. **Data Preprocessing**
   - Tokenization, stopword removal, stemming
   - Vectorization using CountVectorizer or TF-IDF

2. **Model Training**
   - Algorithms: Naive Bayes, Random Forest, logistic Regression
   - Evaluation: Accuracy, Precision

3. **Model Deployment**
   - Saved as `model.pkl` and `vectorizer.pkl` file for integration with web app


