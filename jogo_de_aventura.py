# Um jogo de decisões que terei que criar vários finais diferentes

class jogoDeAventura:
  def __init__(self):
    self.pergunta1 = 'Você nasceu no norte ou no sul? ' 
    self.pergunta2 = 'Você prefere espada ou escudo? ' 
    self.pergunta3 = 'Qual é linha de frente ou tático? ' 

  def Iniciar(self):
    self.resposta1 = input(self.pergunta1)
    if self.resposta1 == 'norte':
      resposta1A = input(self.pergunta2)
      if resposta1A == 'espada':
        resposta1A1 = input(self.pergunta3)
        if resposta1A1 == 'linha de frente':
          print('Você é como um poderoso viking do norte que enfrenta a todos com sua espada de Ganahak')
        if resposta1A1 == 'tatico':
          print('Você é um destemido líder do norte capaz de elaborar grandes planos')
      if resposta1A == 'escudo':
        resposta1A2 = input(self.pergunta3)
        if resposta1A2 == 'linha de frente':
          print('Um soldado valente do norte que fica na muralha de escudos')
        if resposta1A2 == 'tatico':
          print('Um homem caltelozo do norte que sabe identificar de longe qualquer perigo')
    if self.resposta1 == 'sul':
      resposta1B = input(self.pergunta2)
      if resposta1B == 'espada':
        resposta1B1 = input(self.pergunta3)
        if resposta1B1 == 'linha de frente':
          print('Um verdadeiro soldado sulista exercito de um homem só')
        if resposta1B1 == 'tatico':
          print('Astuto líder do sul com potência para comandar as maiores embarcações')
      if resposta1B == 'escudo':
        resposta1B2 = input(self.pergunta3)
        if resposta1B2 == 'linha de frente':
          print('Um sulista de muita força e bravura para ir de frente em batalhas')
        if resposta1B2 == 'tatico':
          print('Um soldado que veio do sul sabendo liderar grandes tropas, profanador de estratégias')

jogoAventura = jogoDeAventura()
jogoAventura.Iniciar()

      