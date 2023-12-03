import streamlit as st

st.set_page_config(page_title="Perpustakaan", page_icon=":books:", layout="centered")

st.header("Pengembalian")

with st.container():
    st.text_input("Nama peminjam")