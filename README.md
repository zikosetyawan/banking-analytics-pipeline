# 🏦 Banking Fraud Analytics Pipeline  
**End-to-End Data Engineering & Fraud Risk Analysis Project**

---

## 📌 Project Overview
Proyek ini membangun **pipeline analitik transaksi perbankan secara end-to-end**,
mulai dari **data mentah (CSV)**, **database & transformasi SQL**,  
hingga **analisis risiko fraud dan dashboard monitoring interaktif berbasis Power BI**.

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
```text
data/
├── raw/
│ └── Bank_Transaction_Fraud_Detection.csv
└── processed/
  └── banking_transactions_clean.csv
```

---

## 🏗️ Arsitektur Pipeline
```text
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
```

Pipeline ini menekankan **alur data yang jelas, modular, dan scalable**.

---

## 🔍 Tahapan Project

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

### 6️⃣ Fraud Risk Monitoring Dashboard (Power BI)

Sebagai tahap akhir dari pipeline analitik, proyek ini dilengkapi dengan  
**dashboard interaktif berbasis Power BI** yang dirancang menyerupai  
**fraud risk monitoring dashboard pada institusi perbankan**.

Dashboard ini berfungsi sebagai **decision-support layer**,  
yang menjembatani hasil analisis eksploratif dengan  
**kebutuhan monitoring operasional dan pengambilan keputusan berbasis risiko**.

#### 🎯 Tujuan Dashboard
Dashboard dirancang untuk:
- Mengidentifikasi **konsentrasi risiko fraud** lintas dimensi transaksi
- Memahami **pola intraday fraud behavior**
- Membantu **prioritisasi area risiko** berdasarkan kombinasi atribut transaksi
- Menyediakan konteks geografis untuk eksplorasi risiko fraud

#### 📌 Komponen Utama Dashboard

**KPI Summary**
- Total Transactions  
- Total Fraud Transactions  
- Overall Fraud Rate (%)

**Risk Breakdown Visuals**
- Fraud Rate by Device Type
- Fraud Rate by Merchant Category
- Fraud Rate by Transaction Hour
- Fraud Rate Pattern by Hour (per Transaction Type)

**Geographic Context**
- Peta digunakan sebagai **contextual indicator**
- Menunjukkan wilayah yang sedang difilter (bukan ranking absolut)

#### 🎛️ Interactive Filters
- Transaction Type
- Gender
- State

Seluruh visual terhubung secara dinamis untuk mendukung eksplorasi risiko
dari berbagai sudut pandang bisnis.

#### 📷 Dashboard & File Power BI

Dashboard disertakan dalam repositori ini dalam bentuk:

- File Power BI:  
  `dashboard/Banking_Fraud_Risk_Analytics.pbix`
- Preview statis:  
  `dashboard/powerbi_dashboard.png`

Reviewer dapat langsung membuka file `.pbix` untuk:
- Mengeksplorasi interaksi filter
- Melihat relasi antar visual
- Memvalidasi metrik dan perhitungan fraud rate

Dashboard dibangun langsung di atas tabel
`transactions_analytics` sebagai **single source of truth**.

---

## 📈 Executive Risk Summary
- Fraud rate relatif stabil di berbagai dimensi transaksi
- Tidak ada satu faktor tunggal yang mendominasi risiko fraud
- Pola fraud muncul sebagai kombinasi perilaku lintas dimensi
- Beberapa wilayah menunjukkan fraud rate lebih tinggi (bersifat indikatif)
- Temuan divisualisasikan kembali dalam bentuk dashboard interaktif
  untuk mendukung monitoring dan eksplorasi risiko fraud

---

## 💼 Business Value
- Menunjukkan keterbatasan pendekatan fraud berbasis satu variabel
- Memberikan dasar untuk pengembangan lanjutan:
  - multi-factor risk scoring
  - anomaly detection
  - fraud classification model
- Pipeline siap dikembangkan ke **machine learning** atau **dashboard monitoring**

---

## 🧰 Tech Stack
- **Python** (pandas, matplotlib, seaborn, psycopg2)
- **PostgreSQL**
- **SQL**
- **Docker**
- **Jupyter Notebook**
- **Power BI**

---

## 📁 Struktur Folder
```text
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
├── dashboard/
│ ├── Banking_Fraud_Risk_Analytics.pbix
│ └── powerbi_dashboard.png
├── LICENSE
└── README.md
```

---

## 📝 Catatan
Proyek ini bersifat **eksploratif dan analitis**.  
Seluruh temuan ditujukan sebagai dasar **pengambilan keputusan bisnis**  
dan **pengembangan sistem fraud detection lanjutan**.

---

## ▶️ How to Run Locally

Untuk menjalankan pipeline ini secara lokal, pastikan Docker dan Python (>=3.9) telah terpasang. 
Jalankan PostgreSQL menggunakan `docker-compose up -d` pada folder `docker/`, lalu muat data hasil cleaning ke database dengan menjalankan script `scripts/03_load_raw_to_postgres.py`. 
Setelah tabel `transactions_raw` terbentuk, jalankan transformasi bisnis menggunakan `scripts/04_transform_transactions.sql` untuk menghasilkan tabel `transactions_analytics`. 
Analisis eksploratif dapat dijalankan melalui notebook `notebooks/05_fraud_analysis.ipynb`, 
dan dashboard Power BI dapat dibuka langsung menggunakan file `.pbix` pada folder `dashboard/` yang terhubung ke database PostgreSQL sebagai sumber data.
