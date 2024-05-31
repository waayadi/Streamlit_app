import streamlit as st
import pandas as pd
import duckdb
st.write('SQL Pratice')
options = ["GROUPBY", "JOIN", "WINDOW FUNCTION"]

# Utilisez st.selectbox pour afficher la liste déroulante
selected_option = st.selectbox("SELECT THE THEME", options)

# Affichez l'option sélectionnée
st.write("THE SELECTED THEME :", selected_option)
data={"a":[1,2,3], "b":[4,5,6]}
dt=pd.DataFrame(data)
sql_query=st.text_area(label='Entrer votre input')
st.write(sql_query)
result=duckdb.query(sql_query).df()
st.dataframe(result)