import streamlit as st

# -- Get the user input
year_col, continent_col, log_x_col = st.columns([5, 5, 5])
with year_col:
    year_choice = st.slider(
        "What year would you like to examine?",
        min_value=1952,
        max_value=2007,
        step=5,
        value=2007,
    )
with continent_col:
    continent_choice = st.selectbox(
        "What continent would you like to look at?",
        ("All", "Asia", "Europe", "Africa", "Americas", "Oceania"),
    )
with log_x_col:
    log_x_choice = st.checkbox("Log X Axis?")