import pickle
import numpy as np
import streamlit as st

# load save model
model = pickle.load(open("penyakit_jantung.sav", "rb"))

# judul web
st.title("Prediksi Penyakit Jantung")

age = st.text_input("Umur")

sex = st.text_input("Jenis Kelamin")

cp = st.text_input("Jenis Nyeri Dada")

trestbps = st.text_input("Tekanan Darah")

chol = st.text_input("Nilai Kolesterol")

fbs = st.text_input("Gula Darah")

restecg = st.text_input("Hasil Elektrokadrografi")

thalach = st.text_input("Detak Jantung Maksimum")

exang = st.text_input("Induksi Angina")

oldpeak = st.text_input("ST Depresion")

slope = st.text_input("Slope")

ca = st.text_input("Nilai CA")

thal = st.text_input("Nilai Thal")

# code for prediction
heart_diagnosis = ""

# membuat tombol prediksi
if st.button("Prediksi Penyakit Jantung"):
    heart_prediction = model.predict(
        [
            [
                age,
                sex,
                cp,
                trestbps,
                chol,
                fbs,
                restecg,
                thalach,
                exang,
                oldpeak,
                slope,
                ca,
                thal,
            ]
        ]
    )

    if heart_prediction[0] == 1:
        heart_diagnosis = "Pasien Terkena Penyakit Jantung"
    else:
        heart_diagnosis = "Pasien Tidak Terkena Penyakit Jantung"

st.success(heart_diagnosis)
