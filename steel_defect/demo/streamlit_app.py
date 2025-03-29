import streamlit as st
from steel_defect.inference import Predictor

def launch_streamlit(model_path):
    st.title("Steel Defect Detection")
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])
    
    if uploaded_file is not None:
        predictor = Predictor(model_path)
        prediction = predictor.predict(uploaded_file.getvalue())
        st.image(prediction, caption="Prediction", use_column_width=True)