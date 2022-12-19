# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
# import pickle
# from pathlib import Path
# import streamlit_authenticator as stauth


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    # # --- USER AUTHENTICATION ---
    # names = ["Efendi Lim", "Simin Liew"]
    # usernames = ["elim", "syliew"]

    # # load hashed passwords
    # file_path = Path(__file__).parent / "hashed_pw.pkl"
    # with file_path.open("rb") as file:
    #   hashed_passwords = pickle.load(file)

    # authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    #   "ts_demo", "ampolts", cookie_expiry_days=30)

    # name, authentication_status, username = authenticator.login("Login", "main")

    # if authentication_status == False:
    #   st.error("Username/password is incorrect")

    # if authentication_status == None:
    #   st.warning("Please enter your username and password")

    # if authentication_status:
    #   st.write("# Welcome to Streamlit! 👋")

    # ---- SIDEBAR ----
    # st.sidebar.title(f"Welcome {name}")
    st.write("# Welcome to Streamlit! 👋")
    
    st.sidebar.success("Select a demo above.")
    # authenticator.logout("Logout", "sidebar")
    
    st.markdown(
        """
        Streamlit is an open-source app framework built specifically for
        Machine Learning and Data Science projects.
        **👈 Select a demo from the sidebar** to see some examples
        of what Streamlit can do!
        ### Want to learn more?
        - Check out [streamlit.io](https://streamlit.io)
        - Jump into our [documentation](https://docs.streamlit.io)
        - Ask a question in our [community
          forums](https://discuss.streamlit.io)
        ### Exploratory Analysis of Time Series data - by tslumen
        - Check out [tslumen](https://hsbc.github.io/tslumen)
    """
    )


if __name__ == "__main__":
    run()
