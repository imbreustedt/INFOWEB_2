s = input("Diga uma frase:\n")
frase = s.split()
for i in range(len(frase)):
    novafrase = " ".join(frase)
    for j in range(len(s)):
        s = s[1:] + s[0]
