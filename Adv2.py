#Задача 2
# #Відкрити текстовий файл та проаналізувати дані.
# # Замінити всі помилки на середнє арифметичне значення властивості та записати у файл Base2.txt.
import collections
d = {}
first_str=''
with open("Base.txt") as file:
    for line in file:
        key, *value = line.split()
        key1=key+value[0]
        del value[0]
        d[key1] = value

avg=0
k=0
avg1=0
k1=0
avg2=0
k2=0
mas=[]
k3=0
avg3=0
k4=0
avg4=0

first_str=d['Cost($)product_1(kg)']

for i in sorted(d.items(), key=lambda x: (len(x[0]), x[0])):
    print (i[0])
del d['Cost($)product_1(kg)']
for i in d:
    if d[i][0]!='N/A':
        k=k+1
        avg=float(d[i][0].replace(',','.'))+avg

    if d[i][1]!='N/A':
        k1=k1+1
        avg1 = float(d[i][1].replace(',','.')) + avg1

    if d[i][2]!='N/A':
        k2 = k2 + 1
        avg2= float(d[i][2].replace(',','.')) + avg2
    if d[i][3]!='N/A':
        k3= k3 + 1
        avg3 = float(d[i][3].replace(',','.')) + avg3
    if d[i][4]!='N/A':
        k4 = k4 + 1
        avg4 = float(d[i][4].replace(',','.')) + avg4
ss=avg/k
ss1=avg1/k1
ss2=avg2/k2
ss3=avg3/k3
ss4=avg4/k4
for i in d:
    if d[i][0] == 'N/A':
        d[i][0]=round(ss,2)
    if d[i][1] == 'N/A':
        d[i][1] = round(ss1,2)
    if d[i][2] == 'N/A':
        d[i][2] = round(ss2,2)
    if d[i][3] == 'N/A':
        d[i][3] = round(ss3,2)
    if d[i][4] == 'N/A':
        d[i][4] = round(ss4,2)
f=open("Base2.txt",'w')
f.writelines('      Cost($)  product_1(kg)  ')
for u in first_str:
    f.writelines(u+'  ')
f.writelines("\n")
for i in sorted(d.items(), key=lambda x: (len(x[0]), x[0])):
    f.writelines(i[0]+" ")
    for j in d[i[0]]:
        f.writelines(str(j)+" ")
    f.writelines("\n")
f.close()

