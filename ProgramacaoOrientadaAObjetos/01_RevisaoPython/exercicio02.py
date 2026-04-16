n = int(input())
x = 0
nomes = ["janeiro", "feverriro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
numeros = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
for i in numeros:
    i = x
    nomes[x-1] = numeros[x-1]
    if n > 3:
        print(f"")