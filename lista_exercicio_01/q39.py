# Primeiro exibimos o valor que desejamos contar
valor = float(input("Informe o valor desejado:"))

# Criamos as variáveis das notas possíveis
notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = moeda1 = moeda50 = moeda25 = moeda10 = moeda5 = moeda01 = 0

# Calculamos o valor de cada nota
notas100 = valor // 100
valor %= 100
notas50 = valor // 50
valor %= 50
notas20 = valor // 20
valor %= 20
notas10 = valor // 10
valor %= 10
notas5 = valor // 5
valor %= 5
notas2 = valor // 2
valor %= 2
moeda1 = valor // 1
valor %= 1
moeda50 = valor // 0.50
valor %= 0.50
moeda25 = valor // 0.25
valor %= 0.25
moeda10 = valor // 0.10
valor %= 0.10
moeda5 = valor // 0.05
valor %= 0.05 
moeda01 = valor // 0.01
valor %= 0.01


# Exibimos a quantidade de notas utilizadas
print("Valor:", valor)
print("Quantidade de notas de 100:", notas100)
print("Quantidade de notas de 50:", notas50)
print("Quantidade de notas de 20:", notas20)
print("Quantidade de notas de 10:", notas10)
print("Quantidade de notas de 5:", notas5)
print("Quantidade de notas de 2:", notas2)
print("Quantidade de moedas de 1 real:", moeda1)
print("Quantidade de moedas de 50 centavos:", moeda50)
print("Quantidade de moedas de 25 centavos:", moeda25)
print("Quantidade de moedas de 10 centavos:", moeda10)
print("Quantidade de moedas de 5 centavos:", moeda5)
print("Quantidade de moedas de 1 centavo:", moeda01)