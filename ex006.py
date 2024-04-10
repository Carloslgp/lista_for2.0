contIn = 0
contOut = 0
for c in range(1, 11):
    num = int(input("Digite um número:"))
    if 10<= num <=20:
        contIn += 1
    else:
        contOut += 1
print(f"Foram contados {contIn} números no intervalo de 10 a 20 \nE {contOut} números fora desse intervalo")
