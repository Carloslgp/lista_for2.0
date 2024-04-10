cont = 0
lista = []
contLista = 0
while cont < 1:
    numero = int(input("Digite o número inteiro que você quer saber os divisores:"))
    if numero < 0:
        print("O Número precisa ser positivo!!!")
    else:
        cont += 1
for c in range(1, numero + 1):
    if numero % c == 0:
        lista.insert(contLista, c)
        contLista += 1
print(lista)
