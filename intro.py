from cProfile import label
import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

df = pd.read_csv('store_store.csv') # atau bisa lewat link dari file yg disimpan di web

st.title("Ini kita mulai dashboad")
st.write("Satrio adalah nama saya!")
st.subheader("sesi satu")

st.caption('Semua orang bisa bikin dashboard')

st.code('import numpy as np\nimpoer pandas as pd')

"_Hello World!_\nkalau **insert gambar** bagaimana kak?"

st.dataframe(df.head())

'''
Komoditas ini juga ikut naik sebesar 0,29 persen atau Rp 40 menjadi Rp 13.740 per kilogram. 
Di Jambi harga komoditas pada periode 30 Agustus 2022 masih Rp 13.620 kemudian naik menjadi Rp 13.720 per kilogram.
'''

# st.table(df) 
# jika data yang ditampilkan sangat banyak, 
# maka metode ini akan tampil dalam waktu sangat lama

#st.metric("Sales", 100,4)
st.metric("Sales", 100,4)
st.metric("Bawang", 13740,'0.29%')
st.metric("Daging Sapi", 80000,'-4.987%')

''' sepertinya dari kedua daerah ini
harga pangan cukup signifikan, ya?'''


st.line_chart(df['Sales'])
st.caption('grafik jumlah penjualan (_sales_)')

st.bar_chart(df['Quantity'])
