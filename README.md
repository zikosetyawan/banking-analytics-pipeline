# 🏦 Banking Fraud Analytics Pipeline  
**End-to-End Data Engineering & Fraud Risk Analysis Project**

---

## 📌 Ringkasan Proyek
Proyek ini membangun **pipeline analitik transaksi perbankan** secara end-to-end,  
mulai dari **data mentah (CSV)** hingga **analisis risiko fraud berbasis visualisasi**.

Pipeline dirancang untuk menunjukkan integrasi yang solid antara:

- ⚙️ **Data Engineering**  
  (data ingestion, database design, SQL transformation)
- 📊 **Data Analytics**  
  (exploratory analysis, visualisasi, dan interpretasi bisnis)

Fokus utama proyek adalah mengevaluasi apakah **fraud dapat dijelaskan oleh atribut transaksi tertentu**,  
atau justru muncul sebagai **kombinasi pola lintas dimensi**.

---

## 🗂️ Dataset
- **Sumber data**: File CSV transaksi perbankan  
- **Total data**: ±200.000 transaksi  
- **Periode transaksi**: Januari 2025  
- **Label fraud**: tersedia pada kolom `is_fraud`

Struktur folder data:
data/
├── raw/
│ └── Bank_Transaction_Fraud_Detection.csv
└── processed/
└── banking_transactions_clean.csv


---

## 🏗️ Arsitektur Pipeline
Raw CSV
↓
01_explore_raw_data.ipynb
↓
02_technical_cleaning.ipynb
↓
Processed CSV
↓
03_load_raw_to_postgres.py
↓
PostgreSQL (transactions_raw)
↓
04_transform_transactions.sql
↓
PostgreSQL (transactions_analytics)
↓
05_fraud_analysis.ipynb


Pipeline ini menekankan **alur data yang jelas, modular, dan scalable**.

---

## 🔍 Tahapan Proyek

### 1️⃣ Exploratory Data Analysis – Raw Data
📓 Notebook:  
`notebooks/01_explore_raw_data.ipynb`

**Tujuan:**
- Memahami struktur awal dataset
- Mengevaluasi distribusi variabel
- Mengidentifikasi potensi masalah data  
  (missing value, format, anomali)

---

### 2️⃣ Technical Data Cleaning
📓 Notebook:  
`notebooks/02_technical_cleaning.ipynb`

**Proses utama:**
- Standarisasi nama kolom
- Konversi tipe data (tanggal & numerik)
- Validasi nilai ekstrem dan inkonsistensi
- Menyiapkan data siap ingest ke database

**Output:**
data/processed/banking_transactions_clean.csv


---

### 3️⃣ Data Ingestion ke PostgreSQL
📜 Script:  
`scripts/03_load_raw_to_postgres.py`

**Proses:**
- Membuat tabel `transactions_raw`
- Bulk insert menggunakan `psycopg2`
- Database dijalankan melalui **Docker**

---

### 4️⃣ Business Transformation (SQL Layer)
📜 Script:  
`scripts/04_transform_transactions.sql`

**Transformasi utama:**
- Membentuk tabel `transactions_analytics`
- Menyederhanakan struktur kolom untuk analisis fraud
- Menambahkan atribut analitik:
  - `transaction_month`
  - `transaction_hour`

Pendekatan ini menempatkan **business logic langsung di layer database**,  
sehingga analisis menjadi lebih konsisten dan reusable.

---

### 5️⃣ Fraud Risk Analysis
📓 Notebook:  
`notebooks/05_fraud_analysis.ipynb`

Analisis difokuskan untuk menjawab **8 pertanyaan bisnis utama**:

1. Fraud berdasarkan device type  
2. Fraud berdasarkan merchant category  
3. Hubungan nilai transaksi dan fraud  
4. Pola fraud berdasarkan jam transaksi  
5. Fraud berdasarkan jenis akun  
6. Fraud berdasarkan kelompok usia  
7. Fraud berdasarkan jenis transaksi  
8. Konsentrasi fraud berdasarkan wilayah (state & city)

**Pendekatan analisis:**
- Agregasi data
- Visualisasi eksploratif
- Interpretasi berbasis konteks risiko bisnis

---

## 📈 Temuan Utama (Ringkas)
- Fraud rate relatif stabil di berbagai dimensi transaksi
- Tidak ada satu faktor tunggal yang mendominasi risiko fraud
- Pola fraud muncul sebagai kombinasi perilaku lintas dimensi
- Beberapa wilayah menunjukkan fraud rate lebih tinggi (bersifat indikatif)

---

## 💼 Nilai Bisnis
- Menunjukkan keterbatasan pendekatan fraud berbasis satu variabel
- Memberikan dasar untuk pengembangan lanjutan:
  - multi-factor risk scoring
  - anomaly detection
  - fraud classification model
- Pipeline siap dikembangkan ke **machine learning** atau **dashboard monitoring**

---

## 🧰 Teknologi yang Digunakan
- **Python** (pandas, matplotlib, seaborn, psycopg2)
- **PostgreSQL**
- **SQL**
- **Docker**
- **Jupyter Notebook**

---

## 📁 Struktur Folder Final
banking-analytics-pipeline/
├── data/
│ ├── raw/
│ └── processed/
├── docker/
│ └── docker-compose.yml
├── notebooks/
│ ├── 01_explore_raw_data.ipynb
│ ├── 02_technical_cleaning.ipynb
│ └── 05_fraud_analysis.ipynb
├── scripts/
│ ├── 03_load_raw_to_postgres.py
│ └── 04_transform_transactions.sql
├── LICENSE
└── README.md


---

## 📝 Catatan
Proyek ini bersifat **eksploratif dan analitis**.  
Seluruh temuan ditujukan sebagai dasar **pengambilan keputusan bisnis**  
dan **pengembangan sistem fraud detection lanjutan**.