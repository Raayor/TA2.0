import streamlit as st

st.set_page_config(page_title="Perpustakaan", page_icon=":books:", layout="centered")

# def css(file):
#     with open(file) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# def css(file):
#     with open(file) as f:
#         st.cont(f"<style>{f.read()}</style>", unsafe_allow_html=True)
def redirect_button(url: str, text: str= None, color="#FD504D"):
    st.markdown(
    f"""
    <a href="{url}" target="_self">
        <div style="
            display: inline-block;
            padding: 0.5em 1em;
            color: #FFFFFF;
            background-color: {color};
            border-radius: 3px;
            text-decoration: none;">
            {text}
        </div>
    </a>
    """,
    unsafe_allow_html=True
    )

# css("style/style.css")

with st.container():
    peminjaman= """
    <button type="submit">Peminjaman</button>
    """

    right_column, left_column = st.columns(2)
    with left_column:
        redirect_button("peminjaman.py","Peminjaman")
        # st.button("Peminjaman", type="secondary")     
    with right_column:    
        st.button("Pengembalian", type="secondary" )
