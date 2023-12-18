def ordenar_lista(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                # Troca os elementos se estiverem fora de ordem
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp

# Exemplo de uso
minha_lista = [7, 4, 3, 12, 8]

print("Lista original:", minha_lista)
ordenar_lista(minha_lista)
print("Lista ordenada:", minha_lista)