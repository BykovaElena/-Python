print ('Задание 1')
# Напишите функцию, которая классифицирует фильмы из материалов занятия по правилам:

# оценка 2 и ниже — низкий рейтинг;
# оценка 4 и ниже — средний рейтинг;
# оценка 4.5 и 5 — высокий рейтинг.
# Результат классификации запишите в столбец class.


import pandas as pd
rating=pd.read_csv(r"C:\Users\Elena\Desktop\ДЗ_Функции и работа с данными\ml-latest-small\ratings.csv")
rating.head()

def ranking_movies(row):
    if row['rating']<=2.0:
        return 'низкий рейтинг'
    elif 2.0<row['rating']<=4.0:
        return 'средний рейтинг'
    else:
        return 'высокий рейтинг'

rating['class'] = rating.apply(ranking_movies, axis=1)
print (rating.head())

print ('Задание 2')
# Используйте файл keywords.csv.
# Нужно написать гео-классификатор, который каждой строке сможет выставить географическую
# принадлежность определённому региону. Т. е. если поисковый запрос содержит название города региона,
# то в столбце ‘region’ пишется название этого региона. Если поисковый запрос не содержит названия
# города, то ставим ‘undefined’.
# Правила распределения по регионам Центр, Северо-Запад и Дальний Восток:

# geo_data = {

# 'Центр': ['москва', 'тула', 'ярославль'],

# 'Северо-Запад': ['петербург', 'псков', 'мурманск'],

# 'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']}
# Результат классификации запишите в отдельный столбец region.


import pandas as pd
geo_data = {
'Центр':['москва', 'тула', 'ярославль'],
'Северо-Запад':['петербург', 'псков', 'мурманск'],
'Дальний Восток':['владивосток', 'сахалин', 'хабаровск'] 
}
cities=[]
for values in geo_data.values():
    for i in values:
        cities.append(i)
cities
['москва',  'тула',  'ярославль',  'петербург',  'псков',  'мурманск',  'владивосток',  'сахалин',  'хабаровск']

row='полармед мурманск запись на прием'
data=row.split(' ')
def check(a):
    for i in a:
        if i in cities:
            for items in geo_data.items():
                if i in items[1]:
                    print(items[0])
check(data)

df=pd.read_csv(r"C:\Users\Elena\Desktop\ДЗ_Функции и работа с данными\ml-latest-small\keywords.csv")
df.head()

def region_keyword(row):
    data=row['keyword'].split(' ')
    i=0
    for title in data:
        if title in cities:
            for items in geo_data.items():
                if title in items[1]:
                    i+=1
                    return items[0]
    if i==0:
        return 'undefined'       
df['region'] = df.apply(region_keyword, axis=1)
df.head()

print (df[(df['region']!='undefined')])
 
