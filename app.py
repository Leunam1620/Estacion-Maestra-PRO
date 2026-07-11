import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from ui.styles import aplicar_estilo
from graficos.oro import mostrar_grafico_oro
from mercados.dxy import obtener_dxy
from mercados.bonos import obtener_bono
# ==================================================
# CONFIGURACIÓN
# ==================================================

st.set_page_config(
    page_title="Estación Maestra PRO",
    page_icon="📈",
    layout="wide"
)
aplicar_estilo()
AJUSTE_PRECIO = 10.0

# ==================================================
# FUNCIONES
# ==================================================

@st.cache_data(ttl=60)
def obtener_datos():
    oro = yf.Ticker("GC=F")
    bono = yf.Ticker("^TNX")
    dxy = yf.Ticker("DX-Y.NYB")

    precio = round(float(oro.history(period="1d")["Close"].iloc[-1]), 2)
    precio -= AJUSTE_PRECIO

    bono_info = bono.fast_info
    dxy_info = dxy.fast_info

    return {
        "oro": precio,
        "bono": bono_info["last_price"],
        "dxy": dxy_info["last_price"],
        "hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

# ==================================================
# INTERFAZ
# ==================================================

st.title("🚀 ESTACIÓN MAESTRA PRO")

st.caption("Versión 0.1")

datos = obtener_datos()

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("🟡 ORO", f"${datos['oro']:.2f}")

with c2:
    st.metric("🏦 US10Y", f"{datos['bono']:.2f}")

with c3:
    st.metric("💵 DXY", f"{datos['dxy']:.2f}")

st.divider()

st.info(f"Última actualización: {datos['hora']}")

st.caption("Actualización automática cada 60 segundos.")
st.divider()

st.subheader("🤖 Señal del Mercado")

if datos["oro"] > 4100 and datos["dxy"] < 101:
    st.success("🟢 SESGO ALCISTA")
elif datos["oro"] < 4050 and datos["dxy"] > 102:
    st.error("🔴 SESGO BAJISTA")
else:
    st.warning("🟡 MERCADO NEUTRAL")
    st.write("### Factores analizados")

st.write(f"🟡 Oro: ${datos['oro']:.2f}")
st.write(f"🏦 Bono US10Y: {datos['bono']:.2f}")
st.write(f"💵 DXY: {datos['dxy']:.2f}")
mostrar_grafico_oro()