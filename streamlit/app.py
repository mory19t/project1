import streamlit as st

import api
from db import init_db, insert_list_of_movies

init_db()

st.set_page_config(page_title="Movies App", page_icon="🎬")

st.title("Movies API Project")

option = st.sidebar.selectbox(
    "Enter Your Option",
    [
        "Call Movie List By Page",
        "Insert Movies from API"
    ]
)

page_id = st.number_input(
    "Enter Page Number",
    min_value=1,
    max_value=25,
    value=1,
    step=1
)

if option == "Call Movie List By Page":
    if st.button("Show Movies"):
        movies = api.get_movie_list_by_page(page_id)

        if movies:
            st.write(movies)
        else:
            st.error("Please enter a valid page.")

elif option == "Insert Movies from API":
    if st.button("Add Movies"):
        movies = api.get_movie_list_by_page(page_id)

        if movies:
            message = insert_list_of_movies(movies)
            st.success(message)
        else:
            st.error("Please enter a valid page.")