# Печатные газеты использовали свой формат дат для каждого выпуска. 
# Для каждой газеты из списка напишите формат указанной даты для перевода в объект datetime:
# The Moscow Times — Wednesday, October 2, 2002
# The Guardian — Friday, 11.10.13
# Daily News — Thursday, 18 August 1977
from datetime import timedelta
from datetime import datetime
The_Moscow_Times = datetime.strptime("Wednesday, October 2, 2002", "%A, %B %d, %Y")
print (The_Moscow_Times)
The_Guardian = datetime.strptime('Friday, 11.10.13', '%A, %d.%m.%y')
print (The_Guardian) 
Daily_News = datetime.strptime('Thursday, 18 August 1977', '%A, %d %B %Y')
print (Daily_News)

# Дан поток дат в формате YYYY-MM-DD, в которых встречаются некорректные значения:
# stream = [‘2018-04-02’, ‘2018-02-29’, ‘2018-19-02’]
# Напишите функцию, которая проверяет эти даты на корректность. То есть для каждой даты возвращает True — дата корректна или False — некорректная.

information_about_date = ['2018-04-02', '2018-02-29', '2018-19-02']

def datecheck(dates):
    for date in dates:
        try:
            date_1 = datetime.strptime(date, '%Y-%m-%d')
            print(date, 'True')
        except:
            print(date, 'False')
#         else:
#             print()
            
datecheck(information_about_date)

# Напишите функцию date_range, которая возвращает 
# список дат за период от start_date до end_date. 
# Даты должны вводиться в формате YYYY-MM-DD. 
# В случае неверного формата или при start_date > end_date должен возвращаться пустой список.

start_date = '1993-05-03'
end_date = '1993-05-31'
def date_range(start_date, end_date):
    list_date = []
    try:
        start_date1 = datetime.strptime(start_date, '%Y-%m-%d')
        end_date1 = datetime.strptime(end_date, '%Y-%m-%d')
        if start_date1 > end_date1:
            print(list_date)
        else:
            while start_date1 <= end_date1:
                list_date.append(start_date1.strftime('%Y-%m-%d'))
                start_date1 += timedelta(days=1)
        print(list_date)
    except:
        print([])
        
date_range(start_date, end_date)