# Primeiro, atribuo as variáveis, e em "horas" e "valor" coloco na tipagem "float" para realizar o cálculo de salário
matricula = input("Insira o número da sua matrícula:")
horas = float(input("Insira a quantidade de horas trabalhadas:"))
valor = float(input("Insira quanto receberá por hora:"))
salario = (horas * valor)

# Mesmo sendo automático, coloco a tipagem do "salario" para "float"
float(salario)

# Por fim, utilizo o "print" para mostrar na tela o salário já calculado e a matrícula do usuário
print("O número da sua matrícula é:",matricula)
print("O valor de seu salário é:", salario)