contImp = 0
contPar = 0
for c in range(1,11):
    num = int(input("Digite um número: "))
    if num % 2 == 1:
        contImp += 1
    else:
        contPar += 1
print(f" O número de números ímpares digitados foi {contImp}")
print(f" O número de números pares digitados foi {contPar}")
