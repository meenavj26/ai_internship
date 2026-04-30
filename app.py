import streamlit as st
import json

with open("recipes.json", "r", encoding="utf-8") as file:
    recipes = json.load(file)

st.title("BBC Good Food Recipes")

for recipe in recipes:
    st.header(recipe["title"])
    st.subheader("Ingredients")

    for item in recipe["ingredients"]:
        st.write("- " + item)

    st.write("---")