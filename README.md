# Car Price Prediction 🚗

Ford car price prediction using XGBoost with Streamlit deployment.

## Overview
A machine learning web app that predicts the price of Ford cars based on features like year, mileage, fuel type, transmission, and engine size.

## Model Performance
- Algorithm: XGBoost (tuned with GridSearchCV)
- R² Score: 0.927

## Features Used
- Year
- Mileage
- Tax
- MPG
- Engine Size
- Fuel Type (Petrol/Diesel/Electric/Hybrid/Other)
- Transmission (Manual/Semi-Auto/Automatic)
- Car Model

## Tech Stack
- Python
- XGBoost
- Scikit-learn
- Pandas, NumPy, matplotlib,seaborn
- Streamlit

## How to Run
pip install -r requirements.txt
streamlit run deployment.py

## Dataset
Ford car prices dataset with features covering model, year, transmission, mileage, fuel type, tax, mpg, and engine size.
