# Search engine Datos Titanic Passenger

```
streamlit run version_02.py 
```

Descripción: Este proyecto trata acerca de un buscador interno para una base de datos. Su función es mostrar en pantalla los datos especificos de una persona, con el objetivo de brindar informacion actualizada de los empleados.
Como ejemplo use un archivo con los daatos del titanic

![imagen del buscador](path/to/image.png)
![imagen del buscador con # de documento](path/to/image.png)
![imagen del buscador con nombre de la persona](path/to/image.png)


Uno de los retos fue implementar Streamlit para renderizar solo el objeto encontrado con **loc[ # de documento ]** ya que el streamlit-searchbox text solo permitia la busqueda de texto y no de numeros, entonces con python analice la cadena de caracateres y...

```
to_numeric = 0
if text_search.isnumeric():
   to_numeric =  pd.to_numeric(text_search, downcast='integer')
   st.write(df.loc[df.PassengerId == to_numeric])
```
De esta manera resolvi para poder buscar un numero en una caja de texto.


***PD***:
para instalar un paquete especifico en un entorno de pyton se hace con 
```
python -m pip install SomePackage==1.0.4    # specific version
```
porque los paquetes instalados de forma global no funcionan en un entorno especifico como por ejemplo el creado para este proyecto

# Data Clean

El archivo [Data_clean.ipynb](empleado-aris/Data_clean.ipynb) Trata de como se Trataron los datos para este proyecto