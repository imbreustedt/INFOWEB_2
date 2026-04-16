n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Digite um valor inteiro: "))
n3 = int(input("Digite um valor inteiro: "))
n4 = int(input("Digite um valor inteiro: "))
lista = [n1, n2, n3, n4]
menor = min(lista)
maior = max(lista)
print(f"O menor valor é {menor} \nO maior valor é {maior}")
lista.remove(menor)
lista.remove(maior)

soma = lista[0] + lista[1]
print(f"A soma dos numeros restantes é = {soma}")