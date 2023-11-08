# Primeiro inserimos todas as notas do aluno e sua frequência
materia1 = float(input("Digite a nota da primeira matéria: "))
materia2 = float(input("Digite a nota da segunda matéria: "))
materia3 = float(input("Digite a nota da terceira matéria: "))
faltas = int(input("Digite o número total de faltas: "))

# Depois calculamos a média de notas e a porcentagem de faltas do aluno
media = (materia1 + materia2 + materia3) / 3
frequencia = (30 - faltas) / 30 * 100

# Verificamos se a média está maior que 7 e se a frequência está maior que 75%
aprovado = media > 7 and frequencia >= 75

# No final usamos "bool" para exibir um resultado "true" ou "false"
print("Aluno aprovado?", aprovado)