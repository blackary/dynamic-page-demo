import streamlit as st
from st_pages import add_page_title, hide_pages, show_pages_from_config

show_pages_from_config()

add_page_title()

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if not st.session_state["logged_in"]:
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if username and password:
        st.session_state["logged_in"] = True
        st.experimental_rerun()

if st.session_state["logged_in"]:
    # hide_pages([])
    hide_pages(
        ["Back", "User settings", "Billing settings", "Cool page 1", "Cool page 2"]
    )
else:
    # hide_pages(["Secret Stuff 1", "Secret Stuff 2"])
    hide_pages(
        [
            "Settings",
            "Favorites",
            "Back",
            "User settings",
            "Billing settings",
            "Cool page 1",
            "Cool page 2",
        ]
    )

if st.session_state["logged_in"] and st.button("Log out"):
    st.session_state["logged_in"] = False
    st.experimental_rerun()

# hide_pages(["Back", "User settings", "Billing settings", "Cool page 1", "Cool page 2"])
