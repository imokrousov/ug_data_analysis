import numpy as np
import pandas as pd
from sklearn import datasets




'''


# Загрузить набор изображений рукописных цифр


#digits1, digits2, digits3 = datasets.load_digits(),datasets.load_boston(),datasets.load_iris()

url1 = 'https://tinyurl.com/simulated-data'
df1 = pd.read_csv(url1)
print(df1.head(3))

url2 = 'https://tinyurl.com/simulated-excel'
df2 = pd.read_excel(url2, sheet_name=0)
print(df2.head(3))

url3 = 'https://tinyurl.com/simulated-json'
df3 = pd.read_json(url3, orient='columns')#split, records, index, columns и values
print(df3.head(3))


from sqlalchemy import  create_engine
db_collection = create_engine('sqlite:///sample.db')
df4 = pd.read_sql_query('SELECT * From data', db_collection)
'''
url = 'https://raw.githubusercontent.com/chrisalbon/simulated_datasets/master/titanic.csv'
titDf = pd.read_csv(url)
print(titDf.head(5))
print(titDf.shape)
print(titDf.describe())
print(titDf.iloc[:5:2])

dataframe = titDf.set_index(titDf['Name'])
print(dataframe.loc['Allen, Miss Elisabeth Walton'])
print(titDf.iloc[0])

print(titDf[(titDf['Survived'] == 1) & (titDf['Age']>=65)].head(10))
titDf['Sex'].replace('female', 'woman',inplace= True)
print(titDf[['Sex','Name']].head(6))