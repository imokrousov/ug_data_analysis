1
Переименование столбцов осуществляется методом rename
Пример:
url = 'https://tinyurl.com/titanic-csv'
dataframe = pd.read_csv(url)
print(dataframe.rename(columns={'PClass': 'Passenger Class'}).head(2))
Замечание:
rename может принимать словарь из более чем одного элемента
print(dataframe.rename (columns={'PClass': 'Passenger Class', 'Sex': 'Gender'}).head(2))
