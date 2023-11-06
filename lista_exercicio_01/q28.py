# Primeiro atribuo as variáveis de "nome", "salário" e "valor"
nome = input("Digite seu nome:")
salario = float(input("Insira seu salário:"))
valor = float(input("Insira o valor das vendas realizadas:"))

# Depois, calculo o valor do lucro das vendas com uma porcentagem de 15%
valor2 = valor * 0.15

# Somo o valor do lucro com o salário
valort = salario + valor2

# Exibo na tela o nome do usuário e o seu ganho total
print("Seu nome é:", nome)
print("Seus ganhos finais foram:", valort)