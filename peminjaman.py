import streamlit as st

st.set_page_config(page_title="Perpustakaan", page_icon=":books:", layout="centered")

st.header("Peminjaman")

with st.container():
    kode_buku = st.number_input("Silahkan masukkan kode buku : ")
    nama_peminjam = st.text_input("Nama peminjam : ")
    NIK = st.number_input("NIK peminjam : ")
    tanggal_pinjam = st.date_input("Tanggal peminjaman : ")

st.button("Pinjam")
