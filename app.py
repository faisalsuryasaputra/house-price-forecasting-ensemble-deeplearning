import streamlit as st
import joblib
import pandas as pd
import numpy as np

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="ProdigiEstate - Telkom University",
    layout="centered"
)

# --- CSS STYLING (THEME: TELKOM UNIVERSITY - WHITE/YELLOW/RED) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Roboto:wght@300;400;700&display=swap');

    /* 1. Background Utama (Putih Bersih) */
    .stApp {
        background-color: #f8f9fa;
        background-image: radial-gradient(#e5e7eb 1px, transparent 1px);
        background-size: 20px 20px;
    }

    /* 2. Container Utama (Kartu Putih dengan Shadow) */
    .main .block-container {
        background: #ffffff;
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        border-top: 8px solid #8f0d1e; /* Merah Marun Telkom */
        border-bottom: 8px solid #f2a900; /* Kuning Telkom */
        max-width: 800px;
    }

    /* 3. Typography (Huruf Hitam/Gelap) */
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        color: #8f0d1e !important; /* Merah Marun */
    }
    
    p, label, .stMarkdown {
        color: #333333 !important; /* Teks Hitam */
        font-family: 'Roboto', sans-serif;
    }

    /* 4. Input Fields (Putih dengan Border Abu) */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select {
        background-color: #ffffff !important;
        color: #333333 !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px;
    }
    
    /* Fokus pada Input */
    .stNumberInput > div > div > input:focus {
        border-color: #f2a900 !important; /* Kuning saat diklik */
        box-shadow: 0 0 5px rgba(242, 169, 0, 0.5);
    }

    /* 5. Sliders */
    .stSlider > div > div > div > div {
        color: #8f0d1e !important;
    }

    /* 6. Kotak Sukses (Hasil Prediksi) */
    .stSuccess {
        background: linear-gradient(135deg, #fffbeb 0%, #fff 100%) !important;
        border: 1px solid #f2a900 !important;
        border-left: 8px solid #f2a900 !important;
        color: #8f0d1e !important;
        padding: 1.5rem !important;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(242, 169, 0, 0.15);
    }

    /* 7. Garis Pemisah */
    hr {
        border-color: #f2a900 !important; /* Kuning */
        opacity: 0.5;
    }

    /* 8. Judul dengan Gradasi */
    .glow-text {
        background: linear-gradient(90deg, #8f0d1e, #d91c2b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3rem;
    }
    
    /* Tombol Utama */
    div.stButton > button {
        background: linear-gradient(90deg, #8f0d1e 0%, #a81124 100%);
        color: white !important;
        border: none;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(143, 13, 30, 0.3);
        background: linear-gradient(90deg, #a81124 0%, #c4182e 100%);
    }
    </style>
""", unsafe_allow_html=True)

# --- HEADER APLIKASI ---
st.markdown("""
    <div style='text-align: center; padding-bottom: 20px;'>
        <h1 style='margin-bottom: -10px;'>
            <span class="glow-text">PRODIGI</span>ESTATE
        </h1>
        <p style='text-align:center; color:#64748b !important; font-size:1rem; margin-top:5px; font-weight: 500;'>
            School of Computing • Telkom University
        </p>
    </div>
""", unsafe_allow_html=True)

# --- LOAD MODEL ---
@st.cache_resource
def load_model():
    # Pastikan file .pkl ada di folder yang sama
    try:
        model = joblib.load("house_price_model.pkl")
        columns = joblib.load("feature_columns.pkl")
        return model, columns
    except FileNotFoundError:
        st.error("File model tidak ditemukan. Pastikan 'house_price_model.pkl' dan 'feature_columns.pkl' ada.")
        return None, None

model, feature_columns = load_model()

if model is not None:
    st.markdown("---")
    st.subheader("📝 Input Data Properti")

    col1, col2 = st.columns([1,1])

    with col1:
        GrLivArea   = st.number_input("Luas Bangunan (sqft)", 0, 6000, 1500, step=10, key="gliv")
        LotArea     = st.number_input("Luas Tanah (sqft)", 1000, 200000, 9000, step=100)
        TotalBsmtSF = st.number_input("Luas Basement (sqft)", 0, 5000, 800, step=10)

        BedroomAbvGr = st.number_input("Jumlah Kamar Tidur", 0, 8, 3)
        FullBath     = st.number_input("Jumlah Kamar Mandi Full", 0, 5, 2)
        TotRmsAbvGrd = st.number_input("Total Ruangan di atas tanah", 2, 15, 7)

    with col2:
        OverallQual = st.slider("Kualitas Rumah Keseluruhan", 1, 10, 6, help="1 = sangat buruk • 10 = luar biasa")
        OverallCond = st.slider("Kondisi Rumah Saat Ini", 1, 10, 5)
        
        KitchenQual = st.slider("Kualitas Dapur", 1, 5, 3, 
                               help="1 = buruk • 5 = sangat baik (Ex = Excellent)")

        GarageCars = st.number_input("Kapasitas Garasi (jumlah mobil)", 0, 4, 2)
        GarageArea = st.number_input("Luas Garasi (sqft)", 0, 1500, 450, step=10)

    neighborhood_mapping = {
        "Blmngtn": 0, "Blueste": 1, "BrDale": 2, "BrkSide": 3, "ClearCr": 4,
        "CollgCr": 5, "Crawfor": 6, "Edwards": 7, "Gilbert": 8, "IDOTRR": 9,
        "MeadowV": 10, "Mitchel": 11, "NAmes": 12, "NPkVill": 13, "NWAmes": 14,
        "NoRidge": 15, "NridgHt": 16, "OldTown": 17, "SWISU": 18, "Sawyer": 19,
        "SawyerW": 20, "Somerst": 21, "StoneBr": 22, "Timber": 23, "Veenker": 24
    }

    selected_neigh = st.selectbox(
        "📍 Neighborhood / Kawasan",
        options=list(neighborhood_mapping.keys()),
        index=5  
    )

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("ANALISA & PREDIKSI HARGA SEKARANG", type="primary", use_container_width=True):
        
        inputs = {
            "GrLivArea": GrLivArea,
            "LotArea": LotArea,
            "TotalBsmtSF": TotalBsmtSF,
            "BedroomAbvGr": BedroomAbvGr,
            "FullBath": FullBath,
            "TotRmsAbvGrd": TotRmsAbvGrd,
            "OverallQual": OverallQual,
            "OverallCond": OverallCond,
            "KitchenQual": KitchenQual,
            "GarageCars": GarageCars,
            "GarageArea": GarageArea,
            "Neighborhood": neighborhood_mapping[selected_neigh]
        }

        df_input = pd.DataFrame([inputs])
        
        df_input = df_input.reindex(columns=feature_columns, fill_value=0)

        with st.spinner("Sistem sedang melakukan valuasi..."):
            prediction = model.predict(df_input)[0]
            prediction_clean = round(prediction / 1000000, 3)  # dalam juta

        st.success(f"""
        ### 🏷️ Hasil Valuasi Properti
        **Estimasi Harga Pasar:**
        # ${prediction:,.0f} 
        *(Sekitar {prediction_clean} Juta USD)*
        """)

        st.balloons()

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.caption("© 2026 PRODIGIESTATE • Informatics Engineering Telkom University")