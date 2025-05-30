import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

st.title("Spam Message Detector")

data = pd.read_csv("spam_data.csv")
st.write(data)

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(data['Message'])
y = data['Is_Spam'].map({'No': 0, 'Yes': 1})

model = MultinomialNB()
model.fit(x, y)

user_input = st.text_input("Enter your message:")
if user_input:
    test = vectorizer.transform([user_input])
    prediction = model.predict(test)[0]
    result = "Spam" if prediction == 1 else "Not Spam"
    st.write("Prediction:", result)