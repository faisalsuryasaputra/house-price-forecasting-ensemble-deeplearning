# 🏠 ProdigiEstate: House Price Prediction App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://handsondigistarda.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.0%2B-orange)](https://www.tensorflow.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-v1.0-yellow)](https://scikit-learn.org/)

> **🔴 LIVE DEMO:** [Click here to try ProdigiEstate](https://handsondigistarda.streamlit.app/)

## 📌 Project Overview
**ProdigiEstate** is an interactive web application designed to predict housing prices (Property Valuation) based on physical building features. This project represents an **End-to-End Data Science** implementation, covering everything from *Exploratory Data Analysis* (EDA) and *Data Preprocessing* to modeling using **Deep Learning (ANN)** & **Ensemble Methods**, and finally deploying to the web.

The application features a user-friendly interface customized with the **Telkom University (School of Computing)** color theme.

## ✨ Key Features
* **Real-time Prediction:** Instant house price estimation using trained Machine Learning models.
* **Custom UI Theme:** Modern interface designed with Telkom University's signature colors (Maroon, Yellow, White).
* **Advanced Modeling:** Utilizes a combination of advanced regression techniques and Artificial Neural Networks.
* **Interactive Input:** Users can input specific parameters such as Lot Area, Living Area, Overall Quality, and Neighborhood location.

## 🛠️ Tech Stack
* **Frontend:** [Streamlit](https://streamlit.io/) (Python Web Framework)
* **Machine Learning:** Scikit-Learn (Random Forest, Lasso, Ridge)
* **Deep Learning:** TensorFlow / Keras (Artificial Neural Network)
* **Data Processing:** Pandas, NumPy
* **Deployment:** Streamlit Community Cloud

## 📊 Model Performance
This project compares several algorithms to achieve the best prediction accuracy. The models were evaluated based on R2 Score and RMSE:

| Model | R2 Score | RMSE |
| :--- | :---: | :---: |
| **Artificial Neural Network (ANN)** | **0.89** | **Low** |
| Random Forest Regressor | 0.87 | Low |
| Linear Regression (Baseline) | 0.84 | High |

## 🚀 How to Run Locally
If you want to run this application on your local machine:

1.  **Clone Repository**
    ```bash
    git clone [https://github.com/faisalsuryasaputra/house-price-forecasting-ensemble-deeplearning.git](https://github.com/faisalsuryasaputra/house-price-forecasting-ensemble-deeplearning.git)
    cd house-price-forecasting-ensemble-deeplearning
    ```

2.  **Install Dependencies**
    Ensure you have Python 3 installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run Application**
    ```bash
    streamlit run app.py
    ```

---
**Created by:** [Faisal Surya Saputra](https://github.com/faisalsuryasaputra)
*Informatics Engineering Student at Telkom University*
