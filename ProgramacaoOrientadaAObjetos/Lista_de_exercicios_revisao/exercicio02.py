entrada = input("Digite a operação: ")
operador = ""
posicao = 0
for i in range(len(entrada)):
    if entrada[i] in "+-*/":
        operador = entrada[i]
        posicao = i
        
n1 = int(entrada[:posicao])
n2 = int(entrada[posicao+1:])

if operador == '+': esultado = n1 + n2
elif operador == '-': resultado = n1 - n2
elif operador == '*': resultado = n1 * n2
elif operador == '/': resultado = n1 / n2

print(f"O resultado é: {resultado}")