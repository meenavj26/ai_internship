import streamlit as st
import requests

st.title("Mini Dictionary App")

# Input box
word = st.text_input("Enter a word")

if st.button("Search"):
    if word:
        url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            st.subheader(f"Word: {data[0]['word']}")

            meaning = data[0]["meanings"][0]["definitions"][0]["definition"]
            st.write("Meaning:", meaning)

        else:
            st.error("Word not found ❌")
    else:
        st.warning("Please enter a word")
