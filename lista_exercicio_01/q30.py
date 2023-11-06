# Primeiro atribuo um valor aleatório para "a", "b" e "c"
a = float(input("Insira valor de a:"))
b = float(input("Insira valor de b:"))
c = float(input("Insira valor de c:"))
pi = 3.14159

# Depois realizo as operações para calcular a área de cada forma geométrica
triangulo = (a * c) / 2
circulo = pi * c**2
trapezio = (a + b) * c / 2
quadrado = b * b
retangulo = a * b

# Finalizando, utilizo "print" para exibir o resultado das operações
print(triangulo)
print(circulo)
print(trapezio)
print(quadrado)
print(retangulo)