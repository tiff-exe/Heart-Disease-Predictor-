Heart Disease Prediction Web App

A user-friendly, interactive web application that leverages machine learning to predict a patient's risk profile for cardiovascular diseases. Built using Python, Streamlit, and Scikit-Learn, this application translates clinical patient metrics into a granular risk probability scoring model.

🚀 Key Features

• Real-time Predictive Analytics: Evaluates 13 key clinical data parameters to instantly output patient risk metrics.
• Categorical Mapping Layer: Smooth data pipeline processing that maps user-friendly text selections into valid mathematical vectors.
• Interactive UI/UX: Form fields tailored for patient indicators including resting metrics, ECG interpretations, and stress testing variables.

🛠️ Tech Stack & Libraries

• Frontend UI: Streamlit
• Core Language: Python 3.x
• Machine Learning Engine: Scikit-Learn (Logistic Regression Optimization)
• Data Processing: Pandas & NumPy
• Model Persistence: Pickle

📋 Evaluated Clinical Parameters

The app calculates predictions using standard medical features derived from the UCI Heart Disease dataset:
• Demographics: Age, Sex
• Symptomatic Variables: Chest Pain Type (CP), Exercise-Induced Angina (Exang)
• Clinical Vitals: Resting Blood Pressure, Serum Cholesterol, Fasting Blood Sugar
• Cardiogram Markers: Resting ECG Results, Maximum Heart Rate (Thalach), ST Depression (Oldpeak), ST Segment Slope
• Fluoroscopy Findings: Number of Major Colored Vessels (CA), Thalassemia Type (Thal)

🔧 Installation & Setup

1. Clone the Repository:bash
git clone https://github.com
cd heart-disease-prediction
Use code with caution.
2. Install Dependencies:bash
pip install -r requirements.txt
Use code with caution.
3. Run the Streamlit Application:bash
streamlit run app.py
Use code with caution.
Would you like me to add sections for Screenshots / Demo GIFs, Model Performance Evaluation Details, or customize any specific variable names to match your final implementation?
