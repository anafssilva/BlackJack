import random

class Baralho:

    def __init__(self):
        self.valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        self.naipes = ['\u2665', '\u2666', '\u2663', '\u2660']

        self.baralho= []
    
    def criar_baralho(self):
        for valor in self.valores:
            for naipe in self.naipes:
                self.baralho.append((valor, naipe))
        return self.baralho
    
    def embaralhar(self):
        random.shuffle(self.baralho)
    
    def dar_cartas(self) -> tuple:
        return self.baralho.pop()
    
class Jogador:
     
    def __init__(self, nome):
        self.nome = nome
        self.cartas = []
        self.ativo = True
    
    def receber_cartas(self, carta):
          self.cartas.append(carta)
    
    def mostrar_cartas(self):
        print (f'{self.nome}: {self.cartas}')
    
    def calcular_pontuacao(self)->int:
      self. pontos = 0
      for carta in self.cartas:
       if carta[0] in ["J", "Q", "K"]:
            self.pontos += 10 
       elif carta[0] == "A":
            self.pontos += 11 
            if self.pontos > 21:
             self.pontos -= 10
       else:
            self.pontos += int(carta[0]) 
      return self.pontos
    
class Jogo21:

    def __init__(self):
        self.baralho = Baralho()
        self.baralho.criar_baralho()
        self.baralho.embaralhar()
        self.dealer = Jogador('Dealer')
        self.jogadores = [Jogador(f'Jogador {i}') for i in range (1,5)]
        self.rodada_ativa = True

    def distribuir_cartas(self):
        carta = self.baralho.dar_cartas()
        self.dealer.receber_cartas(carta)
        for jogador in self.jogadores:
            carta = self.baralho.dar_cartas()
            jogador.receber_cartas(carta)
            
   
    def imprimir_mao(self):
     for jogador in self.jogadores:
        jogador.mostrar_cartas()
     Jogador.mostrar_cartas(self.dealer) 

    def jogar_rodada(self):
        while self.rodada_ativa:
         for jogador in self.jogadores:
            if jogador.ativo:
             opcao = input(f'{jogador.nome}: Deseja comprar mais uma carta? (s/n)')
             if opcao.lower() == 'n':
                jogador.ativo = False
             elif opcao.lower() == 's':
              carta = self.baralho.dar_cartas()
              jogador.receber_cartas(carta)
              jogador.mostrar_cartas()
              pontos = jogador.calcular_pontuacao()
              if pontos > 21:
               print(f'{jogador.nome} ESTOUROU! Pontos: {pontos}')
               jogador.ativo = False
            self.rodada_ativa = any(jogador.ativo for jogador in self.jogadores)
            # any() é uma função embutida em Python que retorna True 
            # se pelo menos um elemento em um iterável for avaliado como verdadeiro,
            # e False caso contrário.
                 
        while Jogador.calcular_pontuacao(self.dealer) < 17: 
         carta = self.baralho.dar_cartas()
         self.dealer.receber_cartas(carta)
         Jogador.mostrar_cartas(self.dealer)
         
    
    def vencedor_jogo(self):
     
     pontos_dealer = Jogador.calcular_pontuacao(self.dealer)

     if pontos_dealer > 21:
           print(f'Dealer PERDEU! Pontos: {pontos_dealer}!') 
           print('FIM DE JOGO!')
     else:
           print(f'Dealer: {pontos_dealer} pontos!')
           for jogador in self.jogadores:
            pontos = jogador.calcular_pontuacao()
            if pontos > 21:
             print(f'Jogador {jogador.nome} PERDEU! Pontos: {pontos}')
            elif pontos > pontos_dealer and pontos <= 21:
             print(f'Jogador {jogador.nome} GANHOU! Pontos: {pontos}')
            elif pontos == pontos_dealer:
             print(f'Jogador {jogador.nome} EMPATOU! Pontos: {pontos}')
            else:
             print(f'Jogador {jogador.nome} PERDEU! Pontos: {pontos}')

def main():

    jogo = Jogo21()
    jogo.distribuir_cartas()
    jogo.distribuir_cartas()
    jogo.imprimir_mao()
    jogo.jogar_rodada()
    jogo.vencedor_jogo()

if __name__ == '__main__':
   main()