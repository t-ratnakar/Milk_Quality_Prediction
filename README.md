# 🥛 Milk Quality Prediction Using Machine Learning

A Django-based web application that predicts milk quality (High, Medium, Low) using a trained machine learning model. This project aims to reduce manual milk quality testing and provide real-time, reliable predictions using chemical parameters of milk.

## 🚀 Features

- 🔍 Predicts milk quality based on parameters like pH, temperature, taste, odor, fat, turbidity, and color.
- 🤖 Machine Learning integration with 99.99% accuracy (Random Forest Classifier).
- 🧑‍💼 Admin and user login system.
- 📈 Accuracy metrics and result visualization.
- 💡 User-friendly interface for rural and semi-literate users.
- 📁 Dataset viewing and result logging.

---

## 🧠 Machine Learning Model

- **Algorithm:** Random Forest Classifier
- **Accuracy:** 99.99%
- **Trained using:** Kaggle-based milk quality dataset
- **Features:** pH, temperature, taste, odor, fat, turbidity, color
- **Model file:** `milk_quality_model.pkl`

---

## 🛠️ Tech Stack

| Component        | Technology          |
|------------------|---------------------|
| Backend          | Django (Python)     |
| Frontend         | HTML, CSS, Bootstrap |
| ML Libraries     | Scikit-learn, NumPy, Pandas, Joblib |
| Database         | SQLite (dev)        |
| Deployment       | Localhost / WSGI    |

---

## 🧾 Project Structure

```bash
milk_quality_project/
├── admins/                  # Admin views & templates
├── users/                   # User registration, login
├── prediction/              # ML logic, model loading
├── templates/               # HTML templates
├── static/                  # CSS, JS
├── milk_quality/            # Main Django config
├── db.sqlite3               # Default DB
├── requirements.txt
└── manage.py
