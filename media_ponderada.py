# números
a = int(input("digite o primeiro número: "))
b = int(input("digite o segundo número: "))
c = int(input("digite o terceiro número: "))
# pesos
peso_a = int(input("digite o o peso do primeiro número: "))
peso_b = int(input("digite o o peso do segundo número: "))
peso_c = int(input("digite o o peso do terceiro número: "))
media = ((a * peso_a) + (b * peso_b) + (c * peso_c))/(peso_a + peso_b + peso_c)
print(f"a média é: {media:.1f}")