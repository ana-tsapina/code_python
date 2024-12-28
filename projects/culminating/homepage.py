import streamlit as st
import numpy 
from PIL import Image



st.title("Amplify")

col1 = st.page_link("pages/Log.py", label = ":gray-background[Log]", use_container_width = True)

with col2: 
    st.page_link("pages/Settings.py", label = ":gray-background[Settings]")  

with col3: 
    st.page_link("pages/Calendar.py", label = ":gray-background[Calendar]")  


