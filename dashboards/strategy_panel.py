import streamlit as st
def render():
    st.sidebar.title("Strategy Controls")
    st.sidebar.button("Pause Bot")
    st.sidebar.button("Resume Bot")
    st.sidebar.button("Optimize Strategy")
