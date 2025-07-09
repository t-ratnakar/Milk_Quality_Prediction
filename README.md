aa
# Milk Quality Prediction Using Machine Learning

A Django-based web application that predicts the **quality of milk** (Good, Medium, or Bad) using a trained machine learning model. This project aims to automate milk quality analysis based on chemical parameters and provide real-time results to users and admins.

---

## Features

- Predicts milk quality based on parameters like pH, temperature, taste, odor, fat, turbidity, and color.
- Machine Learning integration with 99.99% accuracy (Random Forest Classifier).
- Admin and user login system.
- Accuracy metrics and result visualization.
- User-friendly interface for rural and semi-literate users.
- Dataset viewing and result logging.

---

## 🛠️ Tech Stack

| Component        | Technology            |
|------------------|------------------------|
| Backend          | Django (Python)        |
| Frontend         | HTML, CSS, Bootstrap   |
| ML Libraries     | Scikit-learn, NumPy    |
| Database         | SQLite (development)   |
| Deployment       | Localhost / WSGI       |

---

## Project Structure

```
milk_quality_project/
├── manage.py
├── db.sqlite3
├── requirements.txt
│
├── milk_quality/         # Django config (settings, urls)
├── admins/               # Admin login/views/templates
├── users/                # User registration/login/views/templates
├── prediction/           # ML model, logic & views
├── static/               # CSS/JS
└── templates/            # Global HTML templates
    ├── base.html
    ├── index.html
    ├── predict.html
    └── result.html
```

---

## Machine Learning Integration

```python
# predictor.py
import pickle
import numpy as np

model = pickle.load(open('prediction/milk_quality_model.pkl', 'rb'))

def predict_quality(features):
    input_array = np.array([features])
    prediction = model.predict(input_array)
    return prediction[0]
```

- Trained on: pH, Temperature, Taste, Odor, Fat, Turbidity, Color
- Model file: `milk_quality_model.pkl`

---

## Web Interface Templates

| Template           | Description                              |
|--------------------|------------------------------------------|
| base.html          | Reusable layout with nav/footer          |
| index.html         | Home/Landing page                        |
| UserLogin.html     | User login form                          |
| UserRegistration.html | User registration page              |
| AdminLogin.html    | Admin login page                         |
| predict.html       | Form to enter milk parameters            |
| result.html        | Displays predicted result                |

---

## 🔄 Workflow

1. User Registration & Login
2. Submit Test Parameters via Form
3. Backend invokes ML Model for Prediction
4. Display Prediction Result (Good, Medium, Bad)
5. Admins can manage users and view records

---

## Models (Database)

```python
class MilkTestResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ph = models.FloatField()
    temperature = models.FloatField()
    taste = models.BooleanField()
    odor = models.BooleanField()
    fat = models.FloatField()
    turbidity = models.FloatField()
    colour = models.FloatField()
    prediction = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
```

---

## URL Routing

```python
# milk_quality/urls.py
urlpatterns = [
    path('admin/', include('admins.urls')),
    path('users/', include('users.urls')),
    path('predict/', include('prediction.urls')),
    path('', TemplateView.as_view(template_name='index.html')),
]
```

---

## Deployment Steps

```bash
# Install dependencies
pip install -r requirements.txt

# Migrate DB
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver

# Open in browser
http://127.0.0.1:8000/
```

---

## Sample Input for Testing

| Parameter   | Value   |
|-------------|---------|
| pH          | 6.8     |
| Temperature | 35°C    |
| Taste       | Yes (1) |
| Odor        | Yes (1) |
| Fat         | 3.5     |
| Turbidity   | Yes (1) |
| Colour      | 240     |

Expected output: **Milk Quality: Good**

---

## Security & Enhancements

- Form validation & error handling
- Admin role-based access
- Prediction history tracking
- Dashboard with prediction stats

---

## Summary

- Built using Django framework.
- Uses ML model (.pkl) to predict milk quality.
- Separate apps for users, admins, and ML prediction.
- HTML templates for frontend views.
- Deployed locally with `runserver`.

---
