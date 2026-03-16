def calculadora(opc, num1, num2):
    match opc:
        case 1:
           return print(f"a soma dos números é: {num1 + num2}")
        case 2:
            return print(f"a subtração dos números é: {num1 - num2}")
        case 3:
            return print(f"a multiplição dos números é: {num1 * num2}")
        case 4:
            return print(f"a divisão dos números é: {num1 / num2}")

num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
opc = int(input("escolha: [1] soma [2] subtração [3] multiplição [4] divisão"))
calculadora(opc, num1, num2)
