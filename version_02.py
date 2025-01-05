# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



st.set_page_config(page_title="Python Titanic Passenger Search Engine", page_icon="🐍", layout="wide")
st.title("Datos Titanic Passenger")

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


# Buscador
text_search = st.text_input("Ingrese el Nombre o la Cedula ", value="")
   # Test: Moran, Mr. James

#    st.write(df)  --> imprime todo el dataframe

to_numeric = 0
if text_search.isnumeric():
   to_numeric =  pd.to_numeric(text_search, downcast='integer')
   st.write(df.loc[df.PassengerId == to_numeric])
   # Test: 543


df_search = df[df["Name"].str.contains(text_search)]
if text_search.__contains__(" "):
   st.write(df_search)


#  Metricas  https://hackernoon.com/lang/es/15-conjuntos-de-datos-de-excel-para-principiantes-en-analisis-de-datos
# media de edad, supervivencia, promedio tiquete


col1, col2, col3 = st.columns(3)
col1.metric("Total tiquetes vendidos",df['Ticket'].count())


# Grafica supervivencia por genero
gender = df['Sex'].value_counts()
fig, ax = plt.subplots(figsize=(7, 6))
bar_color = ['tab:red', 'tab:blue']
ax = gender.plot(kind='bar', rot=0, color=bar_color)
ax.set_title("Bar Graph of Gender", y = 1)
ax.set_xlabel('Gender')
ax.set_ylabel('Number of People')
ax.set_xticklabels(('Male', 'Female'))
st.pyplot(fig)

# Grafica pasajero por embarcacion
# tabla de contingencia edades vs sexo




