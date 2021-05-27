# SIMULADOR DE DADOS
# Simular um gerador numerico de dados de 1 a 6
import random
import PySimpleGUI as sg


class simuladorDados:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor? '
        # Layout
        self.layout = [
          [sg.Text('Jogar o dador?')]
          [sg.Button('sim'),sg.Button('não')]
        ]
        # criar janela
        

    def Iniciar(self):
      self.janela = sg.Window('Simulador de Dado',layout=self.layout)
      # ler valore na tela
      self.eventos, self.valores = self.janela.Read()
      # fazer algo com os valores
      while True:
        try:
          if self.eventos == 'sim' or self.eventos == 's':
            self.gerarValorDado()
          elif self.eventos == 'não' or self.eventos == 'n':
            print('Obrigado, até breve')
          else:
            print('Favor digitar "sim/s" ou "não/n"')
        except:
          print('Ocorreu um erro ao receber a resposta')

    def gerarValorDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = simuladorDados()
simulador.Iniciar()
