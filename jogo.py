import Funçoes
import random 

x = 0
while x < 1: #lopping do jogo

    num_jogadores = int(input('\033[1m\nNumero de jogadores (2-4): \033[0m'))
    pecas_jogo = Funçoes.cria_pecas()
    peças_monte_mesa = Funçoes.inicia_jogo(num_jogadores, pecas_jogo)
    sem_jogadas = 0

    j = -1
    while j == -1:
        
        for i in peças_monte_mesa['jogadores']:

            mesa = peças_monte_mesa['mesa']
            peça = peças_monte_mesa['jogadores'][i]
            monte = peças_monte_mesa['monte']
            posicoes = Funçoes.posicoes_possiveis(mesa, peça)


            if peça == peças_monte_mesa['jogadores'][0]:
                print('{}\n\033[1m MESA:\n {}{}\033[0m'.format('\033[0;34m', '\033[m',mesa))
                print('{}MONTE:{} {}(APENAS PARA TESTE){}'.format('\033[3;37m',monte,'\033[7;37m', '\033[m')) #REMOVER ESTE PRINT DEPOIS, está aqui soemnte para testes
                print('{}\033[1m\nEssas são suas peças:\n{} {}\033[0m'.format('\033[0;36m', '\033[m',peças_monte_mesa['jogadores'][i]))
                print('{}posicoes:{} {}(APENAS PARA TESTE){}'.format('\033[3;37m',posicoes,'\033[7;37m', '\033[m')) #REMOVER ESTE PRINT DEPOIS, está aqui soemnte para testes


            if peça == []:
                vencedor = '\n...jogador {} venceu...\n'.format(i)
                j = 0

            elif monte == [] and posicoes == [] and Funçoes.verifica_ganhador(peças_monte_mesa['jogadores']) != -1:
                #ajustar para quando o monte estiver vazio
                vencedor = '\n aq1...monte vazio, e sem jogadas possiveis...{}\n'.format(i)
                #j = 0

            else:
                if posicoes == []:
                    if num_jogadores == 4: 
                        if peça == peças_monte_mesa['jogadores'][0]:
                            print('{}\033[1m\nVocê passou a vez\033[0m\n{}'.format('\033[4;31m', '\033[m'))
                        else:
                            print('{}\033[1m\nO jogador {} passou a vez\033[0m\n{}'.format('\033[4;32m',i, '\033[m'))
                            print('{}Mão do jogador:{}{}(apenas para teste){}'.format('\033[3;37m',peças_monte_mesa['jogadores'][i],'\033[7;37m', '\033[m')) #REMOVER ESTE PRINT DEPOIS, está aqui soemnte para testes
                        
                    else:
                        if monte == []:
                            sem_jogadas = sem_jogadas + 1
                            if sem_jogadas == num_jogadores: #ajustar para quando o monte estiver vazio
                                vencedor = '\n aq2...monte vazio, e sem jogadas possiveis...\n'.format(i)
                                j = 0

                        aleatorio = random.choice(monte)
                        peças_monte_mesa['jogadores'][i].append(aleatorio)
                        peças_monte_mesa['monte'].remove(aleatorio)
                        if peça == peças_monte_mesa['jogadores'][0]:
                            print('{}\033[1m\nVocê teve que comprar\033[0m\n{}'.format('\033[4;31m', '\033[m'))                                
                        else:
                            qnt = len(peças_monte_mesa['jogadores'][i])
                            print('{}\033[1m\nO jogador {} teve que comprar e ficou com {} peças \033[0m\n{}'.format('\033[4;32m',i,qnt, '\033[m'))
                            print('{}Mão do jogador:{}{}(apenas para teste){}'.format('\033[3;37m',peças_monte_mesa['jogadores'][i],'\033[7;37m', '\033[m')) #REMOVER ESTE PRINT DEPOIS, está aqui soemnte para testes

                else:
                    sem_jogadas = 0
                    if peça == peças_monte_mesa['jogadores'][0]:
                        jogada = int(input('{}\033[1mqual vai jogar?  \033[0m{}'.format('\033[0;36m', '\033[m')))
                    else:
                        jogada = random.choice(posicoes)
                    peças_monte_mesa['mesa'] = Funçoes.adiciona_na_mesa(peça[jogada], mesa)
                    peças_monte_mesa['jogadores'][i].pop(jogada)
                    #checar aqui
                    if peça == [] or Funçoes.verifica_ganhador(peças_monte_mesa['jogadores']) != -1:
                        vencedor = '\n...jogador {} venceu...\n'.format(i)
                        j = 0
                        break

                    if peça != peças_monte_mesa['jogadores'][0]:
                        qnt = len(peças_monte_mesa['jogadores'][i])
                        print('{}\033[1m\nO jogador {} jogou e ficou com {} peças\033[0m{}'.format('\033[0;35m',i,qnt, '\033[m'))
                        print('{}Mão do jogador:{}{}(apenas para teste){}'.format('\033[3;37m',peças_monte_mesa['jogadores'][i],'\033[7;37m', '\033[m')) #REMOVER ESTE PRINT DEPOIS, está aqui soemnte para testes

                        
    print (vencedor)
    continuar = input('\nQuer jogar novamente?\n ') #continuar jogando ou parar lopping
    if continuar == 'sim': 
        x = 0
    else:
        x = 1