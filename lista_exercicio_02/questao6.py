# Ler os três valores de ponto flutuante
A = float(input("Insira o valor do Ponto A:"))
B = float(input("Insira o valor do ponto B:"))
C = float(input("Insira o valor do ponto C:"))

# Verificar o tipo de triângulo
if A >= B + C:
    tipo_tri = "NAO FORMA TRIANGULO"
elif A**2 == B**2 + C**2:
    tipo_tri = "TRIANGULO RETANGULO"
elif A**2 > B**2 + C**2:
    tipo_tri = "TRIANGULO OBTUSANGULO"
elif A**2 < B**2 + C**2:
    tipo_tri = "TRIANGULO ACUTANGULO"

# Verificar se é equilátero ou isósceles
if A == B == C:
    tipo_tri += "\nTRIANGULO EQUILATERO"
elif A == B or B == C or A == C:
    tipo_tri += "\nTRIANGULO ISOSCELES"

# Exibir o resultado
print(tipo_tri) 