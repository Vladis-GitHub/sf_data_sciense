# Приложение анализа текста как позитивного или негативного
# Предварительно следует выполнить установку: 
# pip install torch
# pip install streamlit
# pip install transformers
# Разобраться позже: https://www.youtube.com/shorts/8ElveRgbROw
import torch
import streamlit as st
from transformers import pipeline

st.title("Analyzing reviews") # - заголовок для приложения
def main():
    review = [
        "Ужасная погода",
    ]
    sentiments = pipeline("sentiment-analysis")
    (review)
    
    st.write(sentiments)
    
if __name__ == "__main__":
    main()