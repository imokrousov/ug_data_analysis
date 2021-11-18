import  pandas as pd
import  numpy as np


url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'
df1 = pd.read_csv(url)
#Переименования столбцов
df2 = df1.rename(columns= {'PClass' : 'Passenger Class'})
print(df2.head(5))
df2 = df2.rename(columns= {'Sex' : 'Gender', 'Name': 'Full Name'})
print(df2[['Full Name', 'Gender']].head(5))
#Запросы к столбцам
print(df2['Age'].max())
print(df2['Age'].min())
print(df2['Age'].mean())
print(df2['Age'].sum())
print(df2['Age'].count())
print(df2.count())
#Нахождение уникальных значений
print(df2['Gender'].value_counts())
print(df2[df2['Age'].isin(df2['Age'].unique())].head(10))
#Работа с отсутсвующими данными
print(df2[df2['Age'].isnull()].head(10))
print(df2.iloc[2])
df2['Gender']  = df2 ['Gender'].replace ('male', np.nan)
print(df2.iloc[2])
#Удаление столбца
df1 = df2.drop(['Age', 'Gender'], axis= 1 )
print(df1.shape)
df1 = df1.drop_duplicates()
print(df1.shape)
df1 = df1.drop_duplicates(subset = ['SexCode'], keep = 'last')
print(df1.shape)
print(df1.head(5))

#Создание
dataframe = pd.DataFrame()
dataframe['A'] = [23,'mama',[1,2]]
dataframe['B'] = [-1,0,np.nan]
new_elem = pd.Series([1,'sem'], index = ['A','B'])
dataframe.append(new_elem, ignore_index=True)
print(dataframe.head(3))
