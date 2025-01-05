import pandas as pd


dataframe = pd.read_csv('Titanic.csv')

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

dataframe.drop(columns=to_drop, inplace=True, axis=1)

print("is nan .sum")
print(dataframe.isna().sum())
dataframe.isna().sum()# plot colunms contains isnan 
# corregir nombres con puntos y carecteres herroneos,

dataframe['Age'] = dataframe["Age"].fillna(dataframe["Age"].mean())
dataframe['Age'].astype(str).str.replace(r"[,\s]", "", regex=True).replace("", None).astype(float)
print(dataframe.Age)