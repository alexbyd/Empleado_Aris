# Import libraries
import streamlit as st
import pandas as pd


st.set_page_config(page_title="Python Titanic Passenger Search Engine", page_icon="🐍", layout="wide")
st.title("Datos Titanic Passenger") #css color #192547

df = pd.read_csv('Titanic.csv').fillna("")

to_drop = ['Unnamed: 12',
           'Unnamed: 13',
           'Unnamed: 14',
           'Unnamed: 15',
           'Unnamed: 16',
           'Unnamed: 17',
           'Unnamed: 18',
           'Unnamed: 19',
           'Unnamed: 20',
           'Unnamed: 21',
           'Unnamed: 22',
           'Unnamed: 23',
           'Unnamed: 24',
           'Unnamed: 25']

df.drop(columns=to_drop, inplace=True, axis=1)

text_search = st.text_input("Ingrese el Nombre o la Cedula ", value="")
   # Test: Moran, Mr. James

#    st.write(df)  --> imprime todo el dataframe

to_numeric = 0
if text_search.isnumeric():
   to_numeric =  pd.to_numeric(text_search, downcast='integer')
   st.write(df.loc[df.PassengerId == to_numeric])
   # Test: 543
 #KeyError: "None of [Index([7], dtype='object')] are in the [columns]"
 # este es el error actual mas cercano que tengo a un buen resultado



df_search = df[df["Name"].str.contains(text_search)]
if text_search.__contains__(" "):# Crear una expresion regular que acepte mayusculas, minusculas y espacios
   st.write(df_search)



