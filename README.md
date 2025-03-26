
# 🧠 CerebriSense – Schizophrenia Support System Based on EEG Data

CerebriSense is a medical web application that supports psychiatrists in analyzing EEG signals to assist in diagnosing schizophrenia.  
It offers a clean interface, patient database, file uploads, and explainable AI output — all tailored for clinical use.

⚠️ *Note: Due to an ongoing scientific publication, the deep learning model and related backend code are not included in this repository.*

<div style="display: flex; align-items: center; gap: 10px; justify-content: center;">

  <div style="display: flex; flex-direction: column;">
    <img src="https://github.com/user-attachments/assets/77b67fc9-9dd7-4c7a-b063-b704e5c3adc7" width="250px"/>
    <img src="https://github.com/user-attachments/assets/3123c063-d9c6-43c0-a374-1d1974ae5b3d" width="250px"/>
  </div>

  <img src="https://github.com/user-attachments/assets/9e346240-d705-41b1-b620-06883338934f" height="500px"/>

</div>



## 🧑‍⚕️ Key Features

- Secure registration and login for medical professionals
- Patient management: add, edit, view medical data
- EEG file upload in `.csv` format
- AI-based classification of EEG signals *(code hidden)*
- Report generation with visualizations (bar charts, predictions, SHAP insights)
- Temporary file analysis (outside database)
- Explainable AI using SHAP to visualize key feature impact
- Access to EEG exam protocols and technical requirements

## 💻 Technologies

- **Frontend:** React, Vite, JavaScript, CSS
- **Backend:** Python, Flask, SQLAlchemy, Alembic
- **Database:** PostgreSQL
- **Model (not included):** TensorFlow, Keras, SHAP, scikit-learn, matplotlib
- **Tools:** GitHub, Postman, pgAdmin, Google Colab

## 📁 Project Structure

- `frontend/` – user interface (React)
- `backend/` – API and app logic (Flask) *(without model endpoints)*
- `docs/` – development documentation and system diagrams
- `database/` – PostgreSQL schema (users, patients, EEG files, analysis results)

## ▶️ Local Setup (Without Model)

```bash
git clone https://github.com/agatoneq/CerebriSense.git
cd CerebriSense

# Backend setup
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
python run.py

# Frontend setup
cd frontend
npm install
npm run dev
```

Open the app at `http://localhost:3000`

> Note: EEG analysis will not function until the model is added.

## 🧠 How It Works (When Model Is Present)

1. Doctor uploads EEG `.csv` file
2. System processes file into ERP format
3. Deep learning model classifies patient (healthy/schizophrenic)
4. SHAP explains prediction with key feature contributions
5. Report is generated and stored in PostgreSQL

*(Steps 2–5 are excluded in this version)*


## 📜 License

Academic engineering thesis.  
Model and publication-involved components excluded to maintain scientific integrity.
