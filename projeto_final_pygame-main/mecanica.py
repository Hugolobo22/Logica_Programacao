import random
from visual import FAIXA_ESQUERDA, FAIXA_DIREITA, JANELA_ALTURA

VEICULO_ALTURA = 250

def alternar_faixa(carro_posicao, faixa):
  carro_posicao.center = (faixa, carro_posicao.center[1])

# Questão 5, item 1
def mover_adversario_aleatoriamente(carro_posicao, velocidade):
  carro_posicao[1] = carro_posicao[1] + velocidade
  
  if carro_posicao[1] > JANELA_ALTURA:
    carro_posicao[1] = -1000
    faixa = random.randint(0, 1)
    if faixa == 0:
      alternar_faixa(carro_posicao, FAIXA_ESQUERDA)
    elif faixa == 1:
      alternar_faixa(carro_posicao, FAIXA_DIREITA)
      return carro_posicao
  
  # Questão 5, itens 3, 4 e 5
  

# Questão 7, item 1
def houve_colisao(carro_posicao, carro2_posicao):
  if carro_posicao[0] == carro2_posicao[0]:
    if carro_posicao[1] <= carro2_posicao[1] + 250:
      return True
  elif carro_posicao[0] != carro2_posicao[0]:
    return False 
# Questão 8, item 1
def subir_nivel(velocidade):
  velocidade = velocidade + 0.5
  print(f"Subiu de nível - Velocidade: {velocidade}")
  return velocidade
  pass # remova esse comando e escreva seu codigo