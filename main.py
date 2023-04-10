# receber a tabuada (inteiro ou decimal)
# mostra a tabuada desse numero
print("Tabuada")

numero = float(input("\nDigite um numero:"))
for fator in range(1,11):
    print(f"{numero}x{fator} = {numero*fator}".replace(".0",""))

    