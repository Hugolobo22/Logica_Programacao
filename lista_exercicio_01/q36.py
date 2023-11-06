# Primeiro exibimos o valor que desejamos contar
valor = int(input("Informe o valor desejado:"))

# Criamos as variáveis das notas possíveis
notas100 = notas50 = notas20 = notas10 = notas5 = notas2 = notas1 = 0

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
notas1 = valor

# Exibimos a quantidade de notas utilizadas
print("Valor:", valor)
print("Quantidade de notas de 100:", notas100)
print("Quantidade de notas de 50:", notas50)
print("Quantidade de notas de 20:", notas20)
print("Quantidade de notas de 10:", notas10)
print("Quantidade de notas de 5:", notas5)
print("Quantidade de notas de 2:", notas2)
print("Quantidade de notas de 1:", notas1)