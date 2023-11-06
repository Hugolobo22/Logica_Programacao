# Primeiro atribuímos o valor de cada uma das 3 notas
nota1 = float(input("Digite a primeira nota do aluno:"))
nota2 = float(input("Digite a Segunda nota do aluno:"))
nota3 = float(input("Digite a Terceira nota do aluno"))

# Depois calculamos o valor de cada peso para cada nota
nota1 = nota1 * 2
nota2 = nota2 * 3
nota3 = nota3 * 5

# Depois calculamos a nota final e exibimos através do "print"
notaf = (nota1 + nota2 + nota3)/10
print(notaf)