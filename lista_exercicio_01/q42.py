# Defina os valores de A, B, C e D de acordo com a tabela
A = (1, 10, 5)
B = (2, 3, 1)
C = (True, False, True)
D = (False, True, True)

# Calcule o resultado da expressão para cada conjunto de valores
for i in range(len(A)):
    resultado = A[i] > B[i] and C[i] or not D[i]
    print(f"Para A={A[i]}, B={B[i]}, C={C[i]}, D={D[i]}, o resultado é {resultado}")