print ('Задание 1')
# Определите, какому фильму было выставлено больше всего оценок 5.0.

import pandas as pd
movies=pd.read_csv (r"C:\Users\Elena\Desktop\ДЗ_Библиотека pandas\Файлы к заданию №1\movies.csv")
print (movies[['movieId','title']].head())

ratings=pd.read_csv(r"C:\Users\Elena\Desktop\ДЗ_Библиотека pandas\Файлы к заданию №1\ratings.csv")
ratings=ratings[['movieId','rating']]
print (ratings)
joined = ratings.merge(movies, on='movieId', how='left')
print(joined[['movieId','rating','title']].head())

max_rating=ratings['rating'].max()
filtered_joined=joined[(joined ['rating']==max_rating)]
result=filtered_joined.groupby(['movieId' , 'title'])['movieId'].count()
print (result.sort_values(ascending=False).head(1))


print ('Задание 2')
#Посчитайте суммарное потребление стран Прибалтики (Латвия, Литва и Эстония) категорий 4, 12 и 21 за период с 2005 по 2010 год. Не учитывайте в расчётах отрицательные значения quantity.

import pandas as pd
energy=pd.read_csv(r"C:\Users\Elena\Desktop\ДЗ_Библиотека pandas\Файлы к заданию №2\power.csv")
energy.head()

countries_filtered = energy[(energy['country']=='Estonia') | (energy['country']=='Lithuania') | (energy['country']=='Latvia') ]
countries_filtered.head()

result=countries_filtered[(countries_filtered['category']==4) | (countries_filtered['category']==12) | (countries_filtered['category']==21) & (countries_filtered['year']<2010) & (countries_filtered['year']>2005)]
print('Cуммарное потребление стран Прибалтики (Латвия, Литва и Эстония) категорий 4, 12 и 21 за период с 2005 по 2010 год составляет {} КВт'.format(result['quantity'].sum()))

print ('Задание 3')
# Выберите страницу любого сайта с табличными данными. 
# Импортируйте таблицы в pandas DataFrame. 
# Вы можете взять любые страницы.

import pandas as pd
data=pd.read_html('https://fortraders.org/quotes')[1]
print (data.head())