# Faça uma pergunta e o programa te dará a resposta
import random

class decidaPorMim:
  def __init__(self):
    self.respostas = [
      ['Faça isso com certeza!'],
      ['Acho que vc deveria pensar no que está dizendo'],
      ['Tem coisas que vc precisa deixar rolar'],
      ['Se tiver com medo, vá com medo mesmo'],
      ['Mete o loko']
    ]

  def Iniciar(self):
    input('Faça sua pergunta? ')
    print(random.choice(self.respostas))

decida = decidaPorMim()
decida.Iniciar()