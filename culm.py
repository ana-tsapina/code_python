import streamlit as st 
import pandas as pd 
import numpy as np 
import sqlite3


st.set_page_config(
    page_title = "Calendar", 

)

st.title("Aplify your potential")


switch = st.button("Log")

if switch: 
    culm = pages[log]
    st.switchpage(log)