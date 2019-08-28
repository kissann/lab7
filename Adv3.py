#Задача 3
#Створити рекомендаційну систему для відеохостингу, яка пропонує до перегляду 5
# близьких за параметрами відеороликів. Система працює наступним чином — користувач вводить такі
# параметри як час перегляду, кількість позитивних та негативних оцінок, а система повертає список рекомендованих до перегляду
# відео із вказаними статистичними даними. Має бути передбачено інтерфейс для виконання запитів та додавання даних у БД. Вихідна
# БД представлена у файлів VideoHost.txt. відстані abc скласти та ранжувати
#Для виконання аналізу використовуйте метрику Манхеттен.
import collections
filename="VideoHost.txt"
def addFile(fname,stroka):
    f = open(fname, "a")
    f.write(stroka)
    f.close()
def vids(v_t,v_p,v_n,d):
    k = 0
    ozenki={}
    with open(filename) as file:
        for line in file:

            if k != 0:
                str1=line.split(' ')

                o_ob=abs(int(v_t) - float(str1[1]))+abs(int(v_p) - float(str1[2]))+abs(int(v_n) - float(str1[3]))
                ozenki[str1[0]]=o_ob
            k = k + 1
    list_d = list(ozenki.items())
    list_d.sort(key=lambda i: i[1])
    b=0
    print("Рекомендуем к просмотру:")
    for y in list_d:
        if b<5:
            print(y)
            print(d[y[0]])
        b=b+1

def new_File(fname):
    d = {}
    first_str = ''
    k=0
    with open(fname) as file:
        for line in file:
            k=k+1
            if k!=1:
                key, *value = line.split()
                key1 = key
                d[key1] = value
            elif k==1:
                value = line.split()
                key='FIRST'
                d[key] = value

    avg = 0
    k = 0
    avg1 = 0
    k1 = 0
    avg2 = 0
    k2 = 0
    first_str = d['FIRST']
    del d['FIRST']
    for i in d:
        if d[i][0] != 'N/A':
            k = k + 1
            avg = float(d[i][0].replace(',', '.')) + avg

        if d[i][1] != 'N/A':
            k1 = k1 + 1
            avg1 = float(d[i][1].replace(',', '.')) + avg1

        if d[i][2] != 'N/A':
            k2 = k2 + 1
            avg2 = float(d[i][2].replace(',', '.')) + avg2

    ss = avg / k
    ss1 = avg1 / k1
    ss2 = avg2 / k2

    for i in d:
        if d[i][0] == 'N/A':
            d[i][0] = round(ss, 2)
        if d[i][1] == 'N/A':
            d[i][1] = round(ss1, 2)
        if d[i][2] == 'N/A':
            d[i][2] = round(ss2, 2)

    f = open(fname, 'w')
    f.writelines('    ')
    for u in first_str:
        f.writelines(u + '  ')
    f.writelines("\n")
    for i in sorted(d.items(), key=lambda x: (len(x[0]), x[0])):
        f.writelines(i[0] + " ")
        for j in d[i[0]]:
            f.writelines(str(j) + " ")
        f.writelines("\n")
    f.close()
    return d
print('Выйти из программы - ^')
print('Добавить видео в файл - ADD')
print('Подобрать видео - SEARCH')

while True:
    x = input('Выберите действие: ')
    if x == '^':
        break
    elif x == 'ADD':
        name = input('Название: ')
        v_t = input('Время: ')
        v_p = input('Хорошие оценки: ')
        v_n = input('Плохие оценки: ')
        addFile(filename,name + '\t' + v_t + '\t' + v_p + '\t' + v_n + '\n')
    elif x == 'SEARCH':
        d=new_File(filename)
        print(d)
        v_t = input('Введите время: ')
        v_p = input('Хорошую оценку: ')
        v_n = input('Плохую оценку: ')
        vids(v_t,v_p,v_n,d)
