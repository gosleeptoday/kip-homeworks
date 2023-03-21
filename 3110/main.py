import random

"""a = [0]*20
i,s = 0, 0
for i in range(20):
    a[i] = random.randint(1, 5)
    if a[i] == 1:
        s+=1
    i += 1

print(f"Список комнат в 20 квартирах: {a}\nВ доме {s} однокомнатных квартир\n")
"""

N = int(input('Введите количество блюд: '))
spisok = [0]*N
for i in range(0, N):
    spisok[i] = random.randint(10, 3000)
m = min(spisok)
print(f'Минимальная калорийность {m}\nСписок калорийности блюд {spisok}')
j = 0
for j in range(20):
    d = spisok[i] - m
    if spisok[i] - m == 20:
        print(f"Блюдо под номером {i+1} отличается по калорийности на 20 от минимального")
    j+=1