import random

baralho = []
jogadores = []
dealer = []

def criar_baralho():
    valores = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    naipes = ['\u2665', '\u2666', '\u2663', '\u2660']
    for valor in valores:
        for naipe in naipes:
            baralho.append((valor,naipe))
    return baralho
    
def distribuir_cartas():
    for i in range(5):
        jogadores.append([]) #adiciona 4 listas em jogadores
    random.shuffle(baralho) #embaralha o baralho
    for jogador in range(5): # quantidades de jogadores para distribuir cartas
            if jogador == 0: 
                dealer.append(baralho.pop())
            else:
                jogadores[jogador].append(baralho.pop())
    
def imprimir_mao():
    for jogador in range(1, 5):
        print(f"Jogador {jogador}: {jogadores[jogador]}") # mostra as cartas da mão dos jogadores
    print(f"Dealer: [{dealer[0]}, *]") #mostra apenas uma carta da mão do Dealer

def calcular_pontuacao(mao):
    pontos = 0
    ases = 0
    for carta in mao:
        if carta[0] >= '2' and carta[0] <= '9': 
            pontos += int(carta[0]) # se a carta for numero soma o valor da carta
        elif carta[0] in ["J", "Q", "K"]:
            pontos += 10 # se a carta for (J,Q,K) soma 10
        elif carta[0] == "A":
            ases += 1  
    for _ in range(ases):
        if pontos + 11 <= 21: # se a carta for (A) e a soma não ultrapassar 21 soma 11
            pontos += 11
        else: # se ultrapassar 21 soma 1
            pontos += 1
    return pontos
    
def play_jogador():
    for jogador in range(1, 5):
        while True:
             opcao = input(f'Jogador {jogador}, deseja comprar mais uma carta? (s/n)')
             if opcao.lower() == 's':
                 jogadores[jogador].append(baralho.pop())
                 print(f'Jogador {jogador}: {jogadores[jogador]}')
                 pontos = calcular_pontuacao(jogadores[jogador])
                 if pontos > 21:
                    print(f'Jogador {jogador} ESTOROU! Pontos: {pontos}')
                    break
             else:
                break
             
def play_dealer():  
    while calcular_pontuacao(dealer) < 17: # se a pontuação do Dealer for menor que 17 compra uma carta
        dealer.append(baralho.pop())
        print(f'Dealer: {dealer}')

def vencedor_jogo():
    pontos_dealer = calcular_pontuacao(dealer)
    if pontos_dealer > 21:
         print(f'Dealer PERDEU! Pontos: {pontos_dealer}!') 
         print('FIM DE JOGO!')
    else:
      print(f'Dealer: {pontos_dealer} pontos!')
      for jogador in range(1, 5):
        pontos = calcular_pontuacao(jogadores[jogador])
        if pontos > 21:
          print(f'Jogador {jogador} PERDEU! Pontos: {pontos}')
        elif pontos > pontos_dealer and pontos <= 21:
           print(f'Jogador {jogador} GANHOU! Pontos: {pontos}')
        elif pontos == pontos_dealer:
           print(f'Jogador {jogador} EMPATOU! Pontos: {pontos}')
        else:
            print(f'Jogador {jogador} PERDEU! Pontos: {pontos}')

def main():
    criar_baralho()
    distribuir_cartas()
    distribuir_cartas()
    imprimir_mao()
    play_jogador()
    play_dealer()
    vencedor_jogo()

if __name__ == '__main__':   
    main()
        




    


               




