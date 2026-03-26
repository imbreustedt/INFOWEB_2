entrada = input("Digite uma sequência de números separados por vírgula: ")
l = entrada.split(',')
soma = 0
for i in l:
    soma += int(i.strip())
print(f"Soma = {soma}")