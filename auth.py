import streamlit as st


def login():
    if "auth" not in st.session_state:
        st.session_state.auth = {"name": None, "status": False, "user": None}

    with st.sidebar:
        st.header("Login")
        username = st.text_input("Username", key="auth_username")
        password = st.text_input("Password", type="password", key="auth_password")
        if st.button("Login"):
            if username and password:
                st.session_state.auth = {
                    "name": username,
                    "status": True,
                    "user": {"username": username},
                }
            else:
                st.warning("Please enter username and password")

    a = st.session_state.auth
    return a["name"], a["status"], a["user"]


class _Auth:
    @staticmethod
    def login():
        return login()


auth = _Auth()
