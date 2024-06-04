import io

import duckdb
import pandas as pd
import streamlit as st

st.write('SQL Pratice')
with st.sidebar:
    
    options = ["GROUPBY", "JOIN", "WINDOW FUNCTION"]
    selected_option = st.selectbox("SELECT THE THEME", options)
    st.write("THE SELECTED THEME :", selected_option)

data={"a":[1,2,3], "b":[4,5,6]}
dt=pd.DataFrame(data)
sql_query=st.text_area(label='Entrer votre input')
st.write(sql_query)
result=duckdb.query(sql_query).df()
st.dataframe(result)