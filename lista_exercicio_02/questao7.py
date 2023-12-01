# Ler os quatro valores inteiros
A = int(input("Insira um valor para A:"))
B = int(input("Insira um valor para B:"))
C = int(input("Insira um valor para C:"))
D = int(input("Insira um valor para D:"))

# Verificar as condições
if (B > C) and (D > A) and (C + D > A + B) and (C > 0) and (D > 0) and (A % 2 == 0):
    print("Valores aceitos")
else:
    print("Valores não aceitos")