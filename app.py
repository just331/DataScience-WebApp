import yfinance as yf
import streamlit as st

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

tickSymbol = 'GOOGL'
# get data on this ticker
tickData = yf.Ticker(tickSymbol)
# get the historical prices for this ticker
tickDf = tickData.history(period='1d', start='2010-7-31', end='2020-7-29')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

st.write("""
## Closing Price
""")
st.line_chart(tickDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickDf.Volume)
