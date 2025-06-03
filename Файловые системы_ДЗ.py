import json
f = open(r'C:\Users\Elena\Desktop\test\purchase_log.txt', encoding ='utf-8')
i = 0
dic = {}
for line in f:
        line = line.strip() 
        
        dict_ = json.loads(line) 
        key_ = dict_['user_id']
        value_ = dict_['category']
        dic[key_] = value_
                  
        
print(dic)


#Задание 2

dict_1 = {}

with open(r'C:\Users\Elena\Desktop\test\purchase_log.txt', 'r', encoding='utf-8') as f:
    for row in f:
        tmp = json.loads(row)
        dict_1[tmp['user_id']] = tmp['category']

with open (r'C:\Users\Elena\Desktop\test\visit_log.csv', 'r', encoding='utf-8') as f:
    with open (r'C:\Users\Elena\Desktop\test\funnel.csv', 'w', encoding='utf-8') as funnel:
        for row in f: 
            line = row.strip().split(',') 
            if line[0] in dict_1:
                line.append(dict_1[line[0]])
            funnel.write(','.join(line) + '\n')





