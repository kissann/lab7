#Задача 1
#У текстовий файл записуються прізвище та ім'я учнів класу і його оцінка за контрольну роботу
# у 12 бальній системі (написати текстовий інтерфейс для додавання даних). Вивести на екран всіх учнів,
# у кого оцінка менше за 7 балів і порахувати середній бал по класу. Вивести загальну статистику ушпішності.
flag=True
spisok={}
while flag:
    p=input("Введите фамилию и имя ученика и его оценку")
    if (p == '^'):
        flag = False
        break
    st=list(map(str,p.split(' ')))
    name=st[0]
    spisok[name]=st
f = open('class.txt', 'w')
sp={}
print("Ученики у которіх оценка меньше 7 балов")
kol=0
ii=0
for s in spisok:
    kol=kol+int(spisok[s][2])
    ii=ii+1
    for k in spisok[s]:
        f.write(k+' ')
    f.write('\n')
    if int(spisok[s][2])<7:
        print(spisok[s])
print("Средний бал по классу")
print(kol)
print(ii)
print(kol/(ii))
f.close()