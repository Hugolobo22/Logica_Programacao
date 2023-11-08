# Ler o valor do salário do usuário
salario = float(input("Digite o valor do salário: "))

# Verificar se o salário é maior que R$ 1.200,00 
deve_pagar_imposto = salario > 1200

# No final, exibo o resultado através de "print", se o salário for maior que 1200, aparecerá "true", se for menor, aparecerá "false" através do type "bool"
print("Paga imposto?", deve_pagar_imposto)