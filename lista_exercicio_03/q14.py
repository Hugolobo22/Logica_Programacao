def referencia(param1):
    print('O valor inicial:',param1)
    param1 = 50
    print('O valor na função:',param1)

x = 5
referencia(x)
print('O valor após sair da Função:',x)

def valor(param2):
    param2 = y
    print('O valor inicial:',param2)
    param2 = 50
    print('O valor na função:',param2)

y = 5
referencia(y)
print('O valor após sair da Função:',y)