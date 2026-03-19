def primo(n):
    primo = True
    for d in range(2, n):
        if n % d == 0:
            primo == False
        if not primo:
            break
    return primo

n = int(input())
if primo:
    print(n, 'é primo')
else:
    print(n, 'não é primo')