'''Задача 1
Відкрийте файл Queen.txt. Проведіть аналіз тексту.
1. Розрахуйте кількість куплетів(куплети відрізняються знаком \n).
2. Визначте кількість рядків у кожному куплеті.
3. Порахуйте кількість слів у тексті.
5. Виведіть статистику найбільш уживаних слів тексту.
6. Передбачте розробку текстового інтерфейсу для виконання перших 5 завдань.'''
import re
import statistics
frequency = {}
f = open('Queen.txt', 'r')
sp={}
sp=f.readlines()
pr=1
kol_r=0
rez={}
nom_k=1
slov={}
k=0;
kol_slov=0
for i in sp:
    rez[nom_k] = kol_r
    kol_r=kol_r+1
    slov[k]=i.split(' ')
    k=k+1
    if i=='\n':
        pr=pr+1
        kol_r=0
        nom_k=nom_k+1
for kk in slov:
    for sl in slov[kk]:
        kol_slov=kol_slov+1
print("Кількість слів")
pr=pr-1
print(kol_slov-pr)
print("Кількість рядків в кожному куплеті")
print(rez)
print("Кількість куплетів "+str(pr))
f.close()
document_text = open('Queen.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

frequency_list = frequency.keys()
k_kol=[]
o=0
for words in frequency_list:
    '''print(words)
    print(frequency[words])'''
    k_kol.append(frequency[words])
print(statistics.mean(k_kol))
print("Виведіть статистику найбільш уживаних слів тексту")
for words in frequency_list:
    if int(frequency[words])>statistics.mean(k_kol):
        print(words)
        print(frequency[words])

document_text.close()