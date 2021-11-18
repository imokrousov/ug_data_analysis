## rename
Переименование столбцов осуществляется методом rename
*  Пример:
```
import pandas as pd
url = 'https://tinyurl.com/titanic-csv'
dataframe = pd.read_csv(url)
print(dataframe.rename(columns={'PClass': 'Passenger Class'}).head(2))
```
*  Замечание:
rename может принимать словарь из более чем одного элемента

```
print(dataframe.rename (columns={'PClass': 'Passenger Class', 'Sex': 'Gender'}).head(2))
```
## Нахождение минимума, максимума, суммы, среднего арифметического и количества
Библиотека pandas поставляется с некоторыми встроенными методами для общепринятых
описательных статистических показателей:
*  Пример:
```
import pandas as pd
url = 'https://tinyurl.com/titanic-csv'
dataframe = pd.read_csv(url)
print('Максимум:', dataframe['Age'].шах())
print('Минимум:', dataframe['Age'].min())
print('Среднее:', dataframe['Age'].meant))
print('Сумма:', dataframe['Age'].sum())
print('Количество:', dataframe['Age'].count())
```
*  Замечание:
Все указанные метод можно вызывать сразу от всего датафрейма, в этом случае они применяются к каждому столбцу
```
print(dataframe.count())
```
