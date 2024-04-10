lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]
repetido = 0
maior = 0
for c in range(0,11):
    vezes = lista.count(c)  
    if vezes > maior:
        maior = vezes
        repetido = c
print(repetido)