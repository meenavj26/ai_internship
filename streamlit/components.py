# !pip install streamlit
# !python -m streamlit run main.py

import streamlit as st

# Headings
st.title("Home Page")           # main title
st.header("This is a Header")   # section header
st.write("---")

# Plain Texts
st.text("- **Some text**")     # to display plain text
st.write("- **Some text**")    # more versatile than text, can handle (dataframes, markdowns, etc.)
st.write("---")

# Special Messages, Colorful texts
st.header("Colored messages")
st.success("Success msgs are in Green")
st.error("Error msgs are in Red")
st.warning("Warning msgs are in Yellow")
st.info("Info msgs are in Blue")
st.write("---")

# Text input
st.header("Text input")
name = st.text_input("Enter your name")

# Number input
st.header("Number input")
age = st.number_input("Enter your age", min_value=0, max_value=100, value=50)

# Button, on click events
st.header("Button")
if st.button("Show Details"):
    st.write(f"Your name is {name} and your age is {age}")
st.write("---")

# Slider
st.header("Slider")
value = st.slider("Select a value", min_value=0, max_value=100, value=50)
st.write(f"Slider value: {value}")
st.write("---")
