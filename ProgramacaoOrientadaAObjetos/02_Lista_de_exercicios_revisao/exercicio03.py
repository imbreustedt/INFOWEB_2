frase = input('Diga uma frase que contenha números:\n')
soma = 0 
for caractere in frase:
    if caractere in "0123456789":
        soma += int(caractere)

print(f"A soma dos algarismos é: {soma}")