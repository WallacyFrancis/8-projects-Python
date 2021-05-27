# SIMULADOR DE DADOS
# Simular um gerador numerico de dados de 1 a 6
import random


class simuladorDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor? '

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:
          if resposta == 'sim' or resposta == 's':
            self.gerarValorDado()
          elif resposta == 'não' or resposta == 'n':
            print('Obrigado, até breve')
          else:
            print('Favor digitar "sim/s" ou "não/n"')
        except:
          print('Ocorreu um erro ao receber a resposta')

    def gerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = simuladorDados()
simulador.Iniciar()
