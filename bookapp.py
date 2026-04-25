import streamlit as st
import requests

st.title("Book Finder")

book = st.text_input("Enter book name")

if st.button("Search"):

    url = f"https://openlibrary.org/search.json?q={book}"
    data = requests.get(url).json()

    if data["docs"]:
        first = data["docs"][0]

        st.subheader(first["title"])

        if "author_name" in first:
            st.write("Author:", first["author_name"][0])

        if "first_publish_year" in first:
            st.write("Year:", first["first_publish_year"])

    else:
        st.write("Book not found.")