# Solicitar o salário do funcionário
salario = float(input("Digite o salário do funcionário: R$ "))

# Verificar as condições e calcular o aumento
if salario > 1250.00:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

# Calcular o novo salário
novo_salario = salario + aumento

# Exibir os resultados
print(f"Salário antes do aumento: R$ {salario:.2f}")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")