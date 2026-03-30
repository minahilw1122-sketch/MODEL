# FastAPI XGBoost Prediction API

## Project Overview
This project is a **FastAPI web API** for predicting `Total Spent` using a trained XGBoost regression model.  
It exposes endpoints for testing and making predictions with JSON inputs.

---

## Folder Structure
```
model_api/
├── main.py           # FastAPI app with endpoints
├── xgb_model.pkl     # Trained XGBoost model
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

---

## Setup / Installation

1. **Clone the repository**
```bash
git clone <your-repo-link>
cd model_api
```

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the API locally**
```bash
uvicorn main:app --reload
```

By default, it runs on:
```
http://127.0.0.1:8000/
```

---

## API Endpoints

### 1. Root Endpoint
- **URL:** `/`
- **Method:** `GET`
- **Description:** Check if API is alive

**Example:**
```bash
curl http://127.0.0.1:8000/
```

**Response:**
```json
{"message": "API is working"}
```

---

### 2. Predict Endpoint
- **URL:** `/predict`
- **Method:** `POST`
- **Description:** Predict `Total Spent` from input features

**Input JSON:**
```json
{
  "Category": 7,
  "Item": 7,
  "Price_Per_Unit": 18.5,
  "Quantity": 10,
  "Discount_Applied": 1,
  "Payment_Method_Cash": 0,
  "Payment_Method_Credit_Card": 0,
  "Payment_Method_Digital_Wallet": 1,
  "Location_In_store": 0,
  "Location_Online": 1
}
```

**Response:**
```json
{
  "predicted_total_spent": 185.0
}
```

---

## Swagger / Interactive Docs

Visit in your browser:
```
http://127.0.0.1:8000/docs
```

Test all endpoints interactively.

---

## Dependencies

- Python 3.9+
- FastAPI
- Uvicorn
- Pandas
- Scikit-learn
- XGBoost
- Pydantic

All listed in `requirements.txt` for easy installation.

---

## Notes

- Ensure `xgb_model.pkl` is in the same folder as `main.py`.
- For testing across devices, run Uvicorn with:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

- Use your PC's local IP to access from another device:
```
http://<your_PC_IP>:8000/
```