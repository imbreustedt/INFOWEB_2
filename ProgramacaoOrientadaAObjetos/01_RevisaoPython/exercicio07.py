s = input("Diga uma frase:\n")
frase = s.split()
for i in range(len(frase)):
    frase.pop(0)
    novafrase = " ".join(frase)
    print(novafrase)