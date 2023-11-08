# 2 ** 3 = 8 e 3 < 8 (3 é menor que 8) / 3 == 3 (3 é igual a 3), portanto a expressão é true devido às informações serem corretas 
questao1 = 3 < 2 ** 3 and 3 == 3

# 0 != 4 (0 é diferente de 4) / 3/3 = 1 == 1 (1 é igual a 1) e (5 + 1) = 6, 6/3 == 2, portanto, o resultado da expressão é true devido às informações estarem corretas
questao2 = 0 != 4 or (3/3 == 1 and (5 + 1) / 3 == 2)

# No final, utilizamos "print" para exibir os resultados
print(questao1)
print(questao2)

# A ordem em que foram executadas segue o padrão da ordem de precedência, fazendo os parênteses primeiro, depois as potências e fatoriais, multiplicação e divisão, adição e subtração
# e, por fim, os valores lógicos como "menor que", "maior que" e "igual"