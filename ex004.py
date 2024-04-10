tot = 0
times = int(input("Você deseja tirar a média de quantas idades?"))
for i in range(1, times+1):
    idade = int(input("Qual a {} idade?".format(i)))
    tot = tot + idade
media = tot/times
print("A média das {} idade é igual a: {}".format(times, media))
