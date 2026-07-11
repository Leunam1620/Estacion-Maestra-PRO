import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

def mostrar_grafico_oro():
    st.subheader("📈 Evolución del Oro")

    oro_hist = yf.Ticker("GC=F").history(period="1mo")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=oro_hist.index,
            y=oro_hist["Close"],
            mode="lines",
            name="Oro"
        )
    )

    fig.update_layout(
        template="plotly_dark",
        height=450,
        margin=dict(l=20, r=20, t=40, b=20)
    )

    st.plotly_chart(fig, width="stretch")