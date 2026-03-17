def calcular_media(notas):
    soma = sum(notas)
    quantidade = len(notas)
    return soma / quantidade
notas = []
quant = int(input("digite a quantidade de notas: "))
while len(notas) < quant:
    try: #linha principal
        n = int(input("digite a nota: "))
        if n > 10 or n < 0:
            print("erro, digite notas validas")
            continue
        else:
            notas.append(n)
    
    except ValueError: #caso o usuario coloque tipo errado
        print("tipo invalido")
        
media = calcular_media(notas)
print(f"média: {media:.2f}")