import Funçoes
import random 

x = 0
while x < 1: #lopping do jogo

    num_jogadores = int(input('\033[1m\nNumero de jogadores (2-4): \033[0m'))
    pecas_jogo = Funçoes.cria_pecas()
    peças_monte_mesa = Funçoes.inicia_jogo(num_jogadores, pecas_jogo)
    sem_jogadas = 0
    pontos = []

    j = -1
    while j == -1:
        
        for i in peças_monte_mesa['jogadores']:

            mesa = peças_monte_mesa['mesa']
            peça = peças_monte_mesa['jogadores'][i]
            monte = peças_monte_mesa['monte']
            posicoes = Funçoes.posicoes_possiveis(mesa, peça)


            if peça == peças_monte_mesa['jogadores'][0]:
                print('{}\n\033[1m MESA:\n {}{}\033[0m'.format('\033[0;34m', '\033[m',mesa))
                print('{}\033[1m\nEssas são suas peças:\n{} {}\033[0m'.format('\033[0;36m', '\033[m',peças_monte_mesa['jogadores'][i]))
                print('{}posicoes:{}{}'.format('\033[3;37m',posicoes, '\033[m'))


            if peça == []:
                v = Funçoes.verifica_ganhador(peças_monte_mesa['jogadores'])
                if v == 0:
                    vencedor = '{}\n...Você venceu...\n{}'.format('\033[4;33m', '\033[m')
                else:
                    vencedor = '{}\n...jogador {} venceu...\n{}'.format('\033[4;33m', v,  '\033[m')
                j = 0
                break


            if monte == [] and posicoes == [] :
                sem_jogadas = sem_jogadas + 1
                pontos.append(Funçoes.soma_pecas(peça))
                if sem_jogadas == num_jogadores: 
                        ganhou = Funçoes.quem_ganha(pontos)
                        if ganhou == 0:
                            vencedor = '\n{}...Você venceu por pontos...\n{}'.format('\033[4;33m', '\033[m')
                        else:
                            vencedor = '{}\n...O jogador {} venceu por pontos...\n{}'.format('\033[4;33m',ganhou, '\033[m')
                        j = 0 
                        break   

            if peça != []:
                if posicoes == []:
                    if num_jogadores == 4: 
                        if peça == peças_monte_mesa['jogadores'][0]:
                            print('{}\033[1m\nVocê passou a vez\033[0m\n{}'.format('\033[4;31m', '\033[m'))
                        else:
                            print('{}\033[1m\nO jogador {} passou a vez\033[0m\n{}'.format('\033[4;32m',i, '\033[m'))
                        
                    else:
                        aleatorio = random.choice(monte)
                        peças_monte_mesa['jogadores'][i].append(aleatorio)
                        peças_monte_mesa['monte'].remove(aleatorio)
                        if peça == peças_monte_mesa['jogadores'][0]:
                            print('{}\033[1m\nVocê teve que comprar\033[0m\n{}'.format('\033[4;31m', '\033[m'))                                
                        else:
                            qnt = len(peças_monte_mesa['jogadores'][i])
                            print('{}\033[1m\nO jogador {} teve que comprar e ficou com {} peças \033[0m\n{}'.format('\033[4;32m',i,qnt, '\033[m'))

                else:
                    sem_jogadas = 0
                    pontos = []
                    if peça == peças_monte_mesa['jogadores'][0]:
                        jogada = int(input('{}\033[1mqual vai jogar?  \033[0m{}'.format('\033[0;36m', '\033[m')))
                        if jogada not in posicoes:
                            print('{}\033[1m\nVocê jogou uma peça errada, por isso perdeu a vez\033[0m\n{}'.format('\033[4;31m', '\033[m'))
                            
                            
                        else:
                            peças_monte_mesa['mesa'] = Funçoes.adiciona_na_mesa(peça[jogada], mesa)
                            peças_monte_mesa['jogadores'][i].pop(jogada)

                
                    else:
                        jogada = random.choice(posicoes)
                        peças_monte_mesa['mesa'] = Funçoes.adiciona_na_mesa(peça[jogada], mesa)
                        peças_monte_mesa['jogadores'][i].pop(jogada)
                    #checar aqui
                    if peça == [] or Funçoes.verifica_ganhador(peças_monte_mesa['jogadores']) != -1:
                        if i == 0:
                            vencedor = '\n{}...Você venceu...\n{}'.format('\033[4;33m', '\033[m')
                        else:
                            vencedor = '\n{}..jogador {} venceu...\n{}'.format('\033[4;33m', i, '\033[m')
                        j = 0
                        break

                    if peça != peças_monte_mesa['jogadores'][0]:
                        qnt = len(peças_monte_mesa['jogadores'][i])
                        print('{}\033[1m\nO jogador {} jogou e ficou com {} peças\033[0m{}'.format('\033[0;35m',i,qnt, '\033[m'))

                        
    print (vencedor)
    continuar = input('\nQuer jogar novamente?\n ') #continuar jogando ou parar lopping
    if continuar == 'sim': 
        x = 0
    else:
        x = 1