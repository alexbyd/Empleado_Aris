import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


dataframe = pd.read_csv('Titanic.csv')

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
x3= dataframe["SibSp"].astype(int).count()
plt.pie(x=x3, labels=dataframe.Parch )
plt.show()