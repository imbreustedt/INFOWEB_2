lista = []
for i in range(1, 11):
    if i%2 == 0:
        i = -i
    lista.append(i)
print(*lista)