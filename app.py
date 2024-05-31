import streamlit as st
import pandas as pd
import duckdb
st.write('Hello !')
data={"a":[1,2,3], "b":[4,5,6]}
dt=pd.DataFrame(data)
sql_query=st.text_area(label='Entrer votre input')
st.write(sql_query)
result=duckdb.query(sql_query).df()
st.dataframe(result)