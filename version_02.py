# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import cufflinks as cf
cf.set_config_file(offline=True)



st.set_page_config(page_title="Python Titanic Passenger Search Engine", page_icon="🐍", layout="wide")
st.title("Datos. Titanic Passenger")

df = pd.read_csv('Titanic.csv', usecols=[
'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'
]).fillna("")

fit = df.groupby('Sex')
#plt.bar(fit, df['Age'])
#st.pyplot(plt)


dataframe = pd.read_csv('adidas.csv', usecols=[
    'Retailer', 'Invoice Date', 'Region', 'Product', 'Price per Unit', 'Units Sold'
])
#print(dataframe.dtypes)
grupo = dataframe.groupby('Region').sum()
st.write(grupo)
#plt.barh(dataframe['Product'], dataframe['Price per Unit'])


#plt.barh(dataframe['Region'], dataframe['Units Sold'])
#st.pyplot(plt)

# Buscador
text_search = st.text_input("Ingrese el Nombre o la Cedula ", value="")
   # Test: Moran, Mr. James

#    st.write(df)  --> imprime todo el dataframe

to_numeric = 0
if text_search.isnumeric():
   to_numeric =  pd.to_numeric(text_search, downcast='integer')
   st.write(df.loc[df.PassengerId == to_numeric])
   # Test: 543


df_search = df[df["Name"].str.contains(text_search)]  # https://docs.streamlit.io/develop/concepts/design/dataframes
if text_search.__contains__(" "):
   st.write(df_search)


#  Metricas  https://hackrnoon.com/lang/es/15-conjuntos-de-datos-de-excel-para-principiantes-en-analisis-de-datos
# media de edad, supervivencia, promedio tiquete
# add css https://dev.to/barrisam/how-to-style-streamlit-metrics-in-custom-css-4h14
# para editar las metricas y su estilo

col1, col2, col3 = st.columns(3)
col1.metric("Total tiquetes vendidos: ",df['Ticket'].count(), border=True)
col2.metric("Media edad supervivientes", df['Age'].astype(str).str.replace(r"[,\s]", "", regex=True)
       .replace("", None).astype(float).mean().astype(int), border=True)
col3.metric("Promedio valor tiquete $:", df["Fare"].mean().astype(int), border=True)
# recuento = dataframe.groupby('Pclass')['Survived'].count()



# Grafica supervivencia por genero
gender = df['Sex'].value_counts()
fig, ax = plt.subplots()
bar_color = ['tab:red', 'tab:blue']
ax = gender.plot(kind='bar', rot=0, color=bar_color)
ax.set_title("Bar Graph of Gender", y = 1)
ax.set_xlabel('Gender')
ax.set_ylabel('Number of People')
ax.set_xticklabels(('Male', 'Female'))
#st.pyplot(fig)

# Grafica edad sosbrevivientes

fig2, axe = plt.subplots()
edad= (df['Age'].astype(str).str.replace(r"[,\s]", "", regex=True)
       .replace("", None).astype(float))
axe = edad.plot(kind="hist")

#st.pyplot(fig2)


# tabla de contingencia edades vs sexo

N = len(df.Age)
k = int(1 + np.log2(N))

intervalos = pd.cut(df["Age"].astype(str).str.replace(r"[,\s]", "", regex=True)
       .replace("", None).astype(float), bins=k, include_lowest=True)
tabla = pd.crosstab(intervalos, df.Sex)

#st.table(tabla)


# Grafico circular



