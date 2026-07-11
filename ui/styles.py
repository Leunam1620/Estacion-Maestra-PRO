import streamlit as st

def aplicar_estilo():

    st.markdown("""
    <style>

    .stApp{
    background: linear-gradient(180deg,#0B0F19,#101826,#0B0F19);
    color:white;
}

    div[data-testid="metric-container"]{
    background:#161B22;
    border:1px solid #30363D;
    border-radius:18px;
    padding:22px;
    box-shadow:0px 8px 25px rgba(0,0,0,.45);
    transition:0.3s;
}
div[data-testid="metric-container"]:hover{
    border:1px solid #FFD700;
    transform:translateY(-3px);
}
    h1{
        color:white;
    }

    h2,h3{
        color:white;
    }

    </style>
    """, unsafe_allow_html=True)