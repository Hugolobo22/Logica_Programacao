def area_quadrado(lado, exibir=False):
    area = lado ** 2
    if exibir:
        print(f"A área do quadrado com lado {lado} é: {area}")
    return area

def area_triangulo(base, altura, exibir=False):
    area = (base * altura) / 2
    if exibir:
        print(f"A área do triângulo com base {base} e altura {altura} é: {area}")
    return area

area_quadrado_4 = area_quadrado(4, True)
print(area_quadrado_4)
area_quadrado_9 = area_quadrado(9) 
print(area_quadrado_9)

area_triangulo_69 = area_triangulo(6, 9)
print(area_triangulo_69)
area_triangulo_58 = area_triangulo(5, 8)
print(area_triangulo_58)