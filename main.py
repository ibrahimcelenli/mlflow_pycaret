import streamlit as st
from pycaret.classification import load_model, predict_model
import pandas as pd

# PyCaret load modul
model = load_model('sentiment_model')

# Streamlit title
st.title("Sentiment Analysis")

# text login
text_input = st.text_area("You can write... :", "")

# prediction button
if st.button("Sentiment Analysis"):
    if text_input:
        input_df = pd.DataFrame([{'text': text_input}])
        
        # prediction
        predictions = predict_model(model, data=input_df)
        sentiment = predictions['prediction_label'][0]
        
        # Result
        st.write(f"**Prediction Sentiment:** {sentiment}")
    else:
        st.write("You can write...")
