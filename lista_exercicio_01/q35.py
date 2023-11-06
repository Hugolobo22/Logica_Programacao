# Primeiro informa-se o valor do quadrado e a fórmula de cada informação requerida
lado = int(input("Insira o lado do quadrado:"))
perimetro = lado * 4
area = lado * lado 
diagonal = lado ** (1/2)

# No final, exibimos o valor de cada informação
print("O perímetro do seu quadrado é:", perimetro)
print("A área do seu quadrado é:", area)
print("A diagonal do seu quadrado é:", diagonal)