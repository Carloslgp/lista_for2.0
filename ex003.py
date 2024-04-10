cont = 0
num = 0
while cont < 1:
    num = int(input("Digite um número de 1 a 10:"))
    if 10 >= num > 0:
        cont += 1
    else:
        print("Número invalido, tente novamente.")
        continue
for tab in range(1, 11):
    print("{} x {} = {}".format(num, tab, (num*tab)))
