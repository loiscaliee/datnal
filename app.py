import streamlit as st
import joblib
import numpy as np

st.title("📈 IDX Forecasting — Moving Average Model (BBCA)")

# ================================
# LOAD MODEL .joblib
# ================================
model_data = joblib.load("best_model_bbca.joblib")

st.subheader("🔍 Model Loaded dari .joblib")
st.json(model_data)

# ================================
# INPUT: Harga Close Hari Ini
# ================================
harga_hari_ini = st.number_input("Harga Close Hari Ini", value=0.0)

# Tombol Prediksi
if st.button("PREDIKSI HARGA BESOK"):
    
    model_type = model_data["model_type"]

    # ================================
    #        MODEL MOVING AVERAGE
    # ================================
    if model_type == "moving_average":
        
        window_size = model_data["window_size"]
        last_values = np.array(model_data["last_values"])  # array harga terakhir dalam model

        # Tambahkan harga hari ini ke window
        updated_window = np.append(last_values, harga_hari_ini)

        # Ambil window_size terakhir saja
        updated_window = updated_window[-window_size:]

        # Moving average → prediksi harga besok
        prediksi = updated_window.mean()

        st.success("📌 Model: Moving Average (MA)")
        st.write(f"Window Size: {window_size}")
        st.write(f"Data Window terbaru: {updated_window}")
        st.write(f"📊 Prediksi harga besok: **{prediksi:.2f}**")

    else:
        st.error("Model tidak dikenali.")
