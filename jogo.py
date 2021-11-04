import Funçoes
import random 
#print ('\033[1m  Your Name  \033[0m')

x = 0
while x < 1: #lopping do jogo

    num_jogadores = int(input('\033[1m\nNumero de jogadores (2-4):  \033[0m'))

    pecas_jogo = Funçoes.cria_pecas()
    peças_monte_mesa = Funçoes.inicia_jogo(num_jogadores, pecas_jogo)

    j = -1

    while j == -1:
        
        for i in peças_monte_mesa['jogadores']:

            print('\033[1m\nEssas são suas peças:\n {}\033[0m'.format(peças_monte_mesa['jogadores'][0]))
         


            mesa = peças_monte_mesa['mesa']
            peça = peças_monte_mesa['jogadores'][i]
            monte = peças_monte_mesa['monte']
            posicoes = Funçoes.posicoes_possiveis(mesa, peça)
            print('Essas são as posições possiveis:  ', posicoes)

            #print(posicoes)
            print('Essa é a mesa:   ',mesa)
            #print('\033[1m\nVez do jogador {}:\033[0m'.format(i))

            if peça == []:
                #print('\033[1m  jogador{} venceu  \033[0m'.format(i))
                j = 50
            elif posicoes == [] and monte == []:
                #print('monte vazio')
                j = 50
                vencedor = Funçoes.soma_pecas(peça)
            elif posicoes == []:
                #print('se lascou, vai ter que comprar')
                peças_monte_mesa['jogadores'][i].append(random.choice(monte))
            elif peça == peças_monte_mesa['jogadores'][0]:
                #pensar em como destacar as pecas que podem ser jogadas
                jogada = int(input('qual peça vai jogar?\n '))
                peças_monte_mesa['mesa'] = Funçoes.adiciona_na_mesa(peça[jogada], mesa)
                peças_monte_mesa['jogadores'][0].pop(jogada)
            else:
                jogada = random.choice(posicoes)
                peças_monte_mesa['mesa'] = Funçoes.adiciona_na_mesa(peça[jogada], mesa)
                peças_monte_mesa['jogadores'][i].pop(jogada)
                print('ele jogou {}'.format(posicoes))







            j = Funçoes.verifica_ganhador(peças_monte_mesa['jogadores'])

    vencedor = Funçoes.verifica_ganhador(peças_monte_mesa['jogadores'])
    print('\033[1m  jogador{} venceu \033[0m'.format(vencedor))

    continuar = input('\nQuer jogar novamente?\n ') #continuar jogando ou parar lopping
    if continuar == 'sim': 
        x = 0
    else:
        x = 1