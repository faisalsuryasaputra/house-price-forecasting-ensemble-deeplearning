# 🏠 House Price Prediction: Advanced Regression & Deep Learning

Proyek ini merupakan solusi *end-to-end* untuk kompetisi Kaggle [House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques). Tujuan utamanya adalah memprediksi harga jual rumah berdasarkan berbagai fitur properti menggunakan teknik *Machine Learning* klasik dan *Deep Learning*.

## 📌 Gambaran Proyek

Notebook ini mencakup seluruh *pipeline* data science, mulai dari pembersihan data mentah hingga evaluasi model. Analisis ini membandingkan kinerja model linear sederhana, regularisasi (Lasso/Ridge), *ensemble tree*, hingga Jaringan Syaraf Tiruan (ANN).

### Fitur Utama:
* **Exploratory Data Analysis (EDA):** Analisis distribusi target (`SalePrice`), korelasi fitur, dan visualisasi *missing values*.
* **Data Preprocessing:**
    * Penanganan *missing values* (drop kolom dengan rasio null tinggi & drop baris).
    * Pembersihan data string (parsing kolom `LotArea`).
    * *Encoding* variabel kategorikal menggunakan `LabelEncoder`.
* **Model Building:** Implementasi berbagai algoritma regresi.
* **Evaluasi Metrik:** Menggunakan RMSE, R2 Score, MAE, dan MAPE.

## 🛠️ Teknologi yang Digunakan

* **Python**
* **Data Manipulation:** Pandas, NumPy
* **Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Linear Regression, Lasso, Ridge, Random Forest)
* **Deep Learning:** Keras / TensorFlow (Sequential API untuk ANN)

## 📊 Model yang Diuji

Notebook ini membandingkan performa dari algoritma berikut:

1.  **Linear Regression:** Sebagai *baseline* model.
2.  **Lasso Regression (L1):** Untuk seleksi fitur otomatis dan mengurangi *overfitting*.
3.  **Ridge Regression (L2):** Menangani multikolinearitas.
4.  **Random Forest Regressor:** Model *ensemble* berbasis pohon keputusan.
5.  **Artificial Neural Network (ANN):** Arsitektur *Deep Learning* dengan:
    * Input Layer menyesuaikan dimensi fitur.
    * Hidden Layers (1024, 256, 64, 16 units) dengan aktivasi ReLU.
    * Output Layer (1 unit) untuk regresi.
    * Optimasi menggunakan Adam dan *Early Stopping*.

## 📈 Hasil Evaluasi (Contoh)

Setiap model dievaluasi menggunakan metrik berikut pada data *test split*:

* **R-squared (R2)**
* **Mean Squared Error (MSE)**
* **Root Mean Squared Error (RMSE)**
* **Mean Absolute Error (MAE)**
* **Mean Absolute Percentage Error (MAPE)**

> *Catatan: Random Forest dan ANN umumnya memberikan hasil yang lebih baik dalam menangkap pola non-linear pada data harga rumah dibandingkan model linear biasa.*

## 🚀 Cara Menjalankan

1.  Clone repository ini:
    ```bash
    git clone [https://github.com/faisalsuryasaputra/nama-repo-kamu.git](https://github.com/faisalsuryasaputra/nama-repo-kamu.git)
    ```
2.  Pastikan dataset `train.csv` tersedia di direktori atau sesuaikan *path* di dalam notebook.
3.  Install library yang dibutuhkan:
    ```bash
    pip install pandas numpy matplotlib seaborn scikit-learn tensorflow
    ```
4.  Jalankan notebook menggunakan Jupyter atau Google Colab.

---
**Author:** [Faisal Surya Saputra](https://github.com/faisalsuryasaputra)
