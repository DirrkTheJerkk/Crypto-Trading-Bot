import streamlit as st
import plotly.graph_objects as go
import pandas as pd
def render():
    st.subheader("Equity Curve")
    try:
        df = pd.read_csv("logs/trades.csv")
        pnl = df[df['signal'] == 'sell']['price'].reset_index(drop=True) - df[df['signal'] == 'buy']['price'].reset_index(drop=True)
        equity = pnl.cumsum()
        fig = go.Figure(go.Scatter(y=equity, mode='lines', name='Cumulative PnL'))
        st.plotly_chart(fig)
    except Exception as e:
        st.error(f"Equity chart error: {e}")
