import streamlit as st
import pandas as pd
import yfinance as yf
#import datetime as dt

st.set_page_config(layout='wide')

#end_date = dt.now()
#start_date = today - 30

tickerAAPL = yf.Ticker('AAPL')
tickerDfAAPL = tickerAAPL.history(periode='1mo')

tickerGOOGL = yf.Ticker('GOOGL')
tickerDfGOOGL = tickerGOOGL.history(periode='1mo')

with st.sidebar:
    st.title("Stock Price")
    
    title1 = st.radio("Pick Stock1",['GOOGL','AAPL','TSLA'])
    title2 = st.radio("Pick Stock2",['GOOGL','AAPL','TSLA'])
    
    #tickerSymbol_radio = st.radio("Pick Stock",['GOOGL','AAPL','TSLA'])
    #tickerSymbol_text = st.text_input("Enter Name") 
    #select_period = st.select_slider("Select Period",['1d','5d','1mo'])
    
    #tickerData = yf.Ticker(tickerSymbol_text)
    ticker1 = yf.Ticker(title1)
    tickerDf1 = ticker1.history(period='1mo')
    
    ticker2 = yf.Ticker(title2)
    tickerDf2 = ticker1.history(period='1mo')
    
    
    
#tickerSymbol = st.radio("Pick Stock",['GOOGL','AAPL','TSLA'])
#tickerSymbol = "AAPL" #AAPL GOOG

#tickerSymbol_radio = st.radio("Pick Stock",['GOOGL','AAPL','TSLA'])
# untuk saham di indonesia, kodenya tambahkan .JK


#tickerDf = tickerData.history(period=select_period) # 'ytd' dt.now() select_period, start="2022-01-01", end="2022-08-01"

c1, c2 = st.columns(2)

with c1:
    st.header(ticker1) #"Jenis Saham : AAPL"
    st.line_chart(tickerDfAAPL['Close','Open'])
with c2:
    st.header(ticker2)
    st.line_chart(tickerDfGOOGL['Close'])



#st.line_chart(tickerDf['Close'])
#st.dataframe(tickerDf)

# jika filenya disimpan di sheet online, File >> Pulbish to web >> format .csv >> share linknya
