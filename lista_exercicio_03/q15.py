def grito_feliz(n):
    if n <= 1:
        return "A felicidade precisa ser maior que 1!"
    
    grito = "Feliz N" + "a" * (n-1) + "tal!!"
    return grito

# Exemplos de uso
print(grito_feliz(2))
print(grito_feliz(5))
print(grito_feliz(10))