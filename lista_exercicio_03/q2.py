def multiplicacao(a, b):
    resultado = 0
    for _ in range(b):
        resultado += a
    return resultado

def divisao_e_resto(dividendo, divisor):
    quociente = 0
    while dividendo >= divisor:
        dividendo -= divisor
        quociente += 1
    return quociente, dividendo

# Leitura dos números
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Multiplicação
resultado_multiplicacao = multiplicacao(num1, num2)
print(f"A multiplicação de {num1} por {num2} é: {resultado_multiplicacao}")

# Divisão inteira e resto
quociente, resto = divisao_e_resto(num1, num2)
print(f"A divisão inteira de {num1} por {num2} é: {quociente}")
print(f"O resto da divisão de {num1} por {num2} é: {resto}")