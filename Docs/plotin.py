import matplotlib.pyplot as plt
import pandas as pd



dataframe = pd.read_csv('Titanic.csv', usecols=[
'PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
       'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked'
], index_col='PassengerId')
print(dataframe.dtypes)
ejex = ["a", "b", "c", "d", "e"]
datos = [1,2,3,4,5]

plt.plot(ejex, datos)
plt.show()
#print(dataframe)

#print(dataframe.head())

#gender = dataframe['Sex'].value_counts()
#fig, ax = plt.subplots(figsize=(7, 6))
#bar_color = ['tab:red', 'tab:blue']
#ax = gender.plot(kind='bar', rot=0, color=bar_color)
#ax.set_title("Bar Graph of Gender", y = 1)
#ax.set_xlabel('Gender')
#ax.set_ylabel('Number of People')
#ax.set_xticklabels(('Male', 'Female'))
#plt.show()


#fig2, axe = plt.subplots()
#axe = dataframe.Age.plot(kind="hist")
#plt.show()
#x3= dataframe["SibSp"].astype(int).count()
#plt.pie(x=x3, labels=dataframe.Parch )
#plt.show()


# los ejes son las etiquetas de los datos a graficar

