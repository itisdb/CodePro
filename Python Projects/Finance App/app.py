from tracemalloc import start
import yfinance
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

tickerSymbol = "GOOGL"
tickerData=yfinance.Ticker(tickerSymbol)
tickerDf= tickerData.history(period='1d', start="2010-5-31", end="2021-7-31")

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)