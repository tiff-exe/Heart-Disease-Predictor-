# Heart Disease Prediction Web App

A clean, interactive web application built with **Python**, **Streamlit**, and **Scikit-Learn** that estimates a patient's risk profile for cardiovascular disease. The app translates clinical observations and stress-testing vitals into an automated logistic regression probability assessment in real time.

---

## 📌 Project Overview

Cardiovascular diseases are among the leading causes of global mortality. Early screening and identification of high-risk indicators allow for timely clinical interventions. 

This repository provides an end-to-end data science and deployment workflow:
1. **Exploratory Data Analysis & Preprocessing:** Handles missing values, performs ordinal mappings, and one-hot encodes nominal multi-class categorical features.
2. **Predictive Modeling:** Trains a calibrated `LogisticRegression` classification model using Scikit-Learn.
3. **Interactive Web Interface:** A lightweight Streamlit frontend that collects clinical patient metrics, reconstructs the required 19-dimensional feature matrix, and returns risk assessments.

---

## 🚀 Key Features

- **Interactive Clinical Form:** Dual-column UI designed for easy input of patient demographics, resting vitals, and cardiac stress tests.
- **Dynamic 19-Feature Vector Reconstitution:** Maps dropdown options (e.g., chest pain classification, ECG categories, thalassemia types) directly into the one-hot encoded matrix required by the model.
- **Instant Risk Probability Output:** Displays the raw predicted probability score alongside risk categories (`High Risk` vs. `Low Risk`).
- **Reproducible Pipeline:** Clean separation between the exploration/training notebook and the production-ready inference script.

---

## 🛠️ Tech Stack & Dependencies

- **Language:** Python 3.9+
- **Frontend / Deployment:** [Streamlit](https://streamlit.io/)
- **Machine Learning:** [Scikit-Learn]
- **Data Manipulation:** [Pandas], [NumPy])
- **Data Visualization:** Matplotlib, Seaborn
- **Serialization:** Pickle

---

## 📋 Evaluated Clinical Parameters

The prediction pipeline evaluates **13 clinical parameters** transformed into **19 input features**:

| Parameter Category | Features / Inputs | Description / Values |
| :--- | :--- | :--- |
| **Demographics** | `age`, `sex` | Age in years; Biological sex (Male / Female) |
| **Vitals & Labs** | `resting_blood_pressure`, `cholesterol`, `fasting_blood_sugar` | Resting BP (mm Hg), Serum Cholesterol (mg/dl), Fasting Blood Sugar (> 120 mg/dl) |
| **Symptom Profile** | `chest_pain_type`, `exercise_induced_angina` | Typical angina, Atypical angina, Non-anginal, or Asymptomatic; Exercise-induced angina (Yes / No) |
| **ECG & Stress Test** | `rest_ecg`, `Max_heart_rate`, `oldpeak`, `slope` | Resting ECG results, Peak HR achieved, ST depression (`oldpeak`), and ST segment slope |
| **Specialized Tests** | `vessels_colored_by_flourosopy`, `thalassemia` | Number of major colored vessels (0–3); Thalassemia defect status |

---

## 📁 Repository Structure

```text
├── Heart_disease_train_test.csv     # Training & testing clinical dataset
├── Heart disease prediction.ipynb  # Jupyter Notebook (EDA, preprocessing & model training)
├── logistic_heart_model.pkl         # Serialized Scikit-Learn Logistic Regression model
├── app.py                           # Streamlit web application script
├── requirements.txt                 # Project dependencies
└── README.md                        # Documentation
