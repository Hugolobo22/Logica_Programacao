def verifica_parenteses(expressao):
    pilha = []

    for char in expressao:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if not pilha:
                return "Erro: parênteses fechados sem terem sido abertos."
            pilha.pop()

    if not pilha:
        return "OK"
    else:
        return "Erro: parênteses abertos sem terem sido fechados."

# Leitura da expressão
expressao = input("Digite a expressão com parênteses: ")

# Verificação e exibição do resultado
resultado = verifica_parenteses(expressao)
print(resultado)