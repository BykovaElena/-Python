print('Задание 1')
phrase_1 = 'nhb ckjdf'
phrase_2 = 'lkjlkjnkuh  kjhkj knj'
if len(phrase_1)>len(phrase_2):
   print('Фраза 1 длинее фразы 2')
elif len(phrase_1)== len(phrase_2):
   print('Фраза 1 равна фразе 2')
else:
   print('Фраза 2 длинее фразы 1')

print('Задание 2')
year = int(input())
if (year-int(abs(2000)))%4==0:
   print('Високосныйгод')
else: 
   print('ОБычный год')

print('задание 3')
print ('Введите дату числами от 1 до 31')
date = int(input ())
if (date >31) or (date <=0):
   print ('Введите дату числами от 1 до 31')
else:
   print ('Введите месяц')
month = input().lower() #приведи, чтобы первая буква была большой
if ((date >= 21 and month == 'март') or (date <= 20 and month == 'апрель')):
   print('Ваш знак зодиака:Овен')
elif (date == 29 and month == 'февраль'):
   print ('Рыба')
elif ((date <= 20 and month == 'март') or (date >= 19 and month == 'февраль')):
   print('Ваш знак зодиака:Рыба')
elif ((date >= 21 and month == 'апрель') or (date <= 20 and month == 'май')):
   print('Ваш знак зодиака:Телец')
elif ((date >= 21 and month == 'май') or (date <= 21 and month == 'июнь')):
   print('Ваш знак зодиака:Близнецы')
elif ((date >= 22 and month == 'июнь') or (date <=22 and month == 'июль')):
   print('Ваш знак зодиака:Рак')
elif ((date >= 23 and month == 'июль') or (date <=22 and month == 'август')):
   print('Ваш знак зодиака:Лев')
elif ((date >= 23 and month == 'август') or (date <=22 and month == 'сентябрь')):
   print('Ваш знак зодиака:Дева')
elif ((date >= 23 and month == 'сентябрь') or (date <=22 and month == 'октябрь')):
   print('Ваш знак зодиака:Весы')
elif ((date >= 23 and month == 'октябрь') or (date <=22 and month == 'ноябрь')):
   print('Ваш знак зодиака:Скорпион')
elif ((date >= 23 and month == 'ноябрь') or (date <=22 and month == 'декабрь')):
   print('Ваш знак зодиака:Стрелец')
elif ((date >= 22 and month == 'декабрь') or (date <=19 and month == 'январь')):
   print('Ваш знак зодиака:Козерог')
elif ((date >= 20 and month == 'январь') or (date <=19 and month == 'февраль')):
   print('Ваш знак зодиака:Водолей')
else:
  print('Введите дату числами от 1 до 31, введите месяц кирилицей')


print ('Задание 4')
# если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран “Коробка №1”;
# если хотя бы одно из измерений больше 2 метров, то выводите “Упаковка для лыж”;
# если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите “Коробка №2”;
# во всех остальных случаях выводите “Коробка №3”.
# Пример работы программы:
# 1.

# width = 15
# length = 55
# height = 15
# Результат:
# Коробка №3
list = []
print ('Укажите ширину коробки в см')
width = list.append (int(input ()))
print ('Укажите длину коробки в см')
length = list.append (int(input ()))
print ('Укажите высоту коробки в см')
height = list.append (int(input ()))
sorted_list = sorted (list)
result = sorted_list [-1]
if result <=15:
   print ('“Коробка №1”')
elif result>=200:
   print ('“Упаковка для лыж”')
elif ((result >15) and (result <50)):
   print ('“Коробка №2”')
else:
   print ('“Коробка №3”')

#Домашнее задание «Типы данных и циклы. Часть 1»
   
print ('Задание 1')
print ('Введите слово на латинице')
word = input()
word_1 = (len(word))
if word_1 % 2==0:
   print (word [len(word)//2-1: len(word)//2+1])
else:
   print (word [len(word)//2])





print ('Задание 2')
amount = 0 
while True: 
    number = int(input('Введите число: ')) 
    if number == 0: 
        break  
    amount += number 
print(amount) 


print ('Задание 3')
boys = ['Peter', 'Alex' , 'John' , 'Arthur' , 'Richard' ]
boys.sort()
#print (boys)
girls = ['Kate', 'Liza', 'Kira', 'Emma' , 'Trisha']
girls.sort()
#print (girls)
union = zip (boys, girls)
length_boys = len(boys)
length_girls = len(girls)
if length_boys != length_girls:
   print ('Внимание, кто-то может остаться без пары!')
else:
   print (f'Идеальные пары: {list(union)}')



print ('Задание 4')
countries_temperature = [
 ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
 ['Германия', [57.2, 55.4, 59, 59, 53.6]],
 ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]
countries_temperature_del_country = [row [1] for row in countries_temperature]
print(countries_temperature_del_country)
thailand, germany, russia, poland = countries_temperature_del_country
print(f'Средняя температура в странах: Тайланд  - {round (5/9*(sum(thailand) / len(thailand)-32), 1)} C',
      f' Германия - {round (5/9*(sum(germany) / len(germany)-32), 1)} C',
      f' Россия - {round (5/9*(sum(russia) / len(russia)-32),1)} C',
       f' Польша - {round (5/9*(sum(poland) / len(poland)-32),1)} C')


