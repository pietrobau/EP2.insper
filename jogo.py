import Funçoes

i = 0
while i < 1: #lopping do jogo

    num_jogadores = int(input('\nNumero de jogadores (2-4):\n '))

    pecas_jogo = Funçoes.cria_pecas()
    jogo_inicial = Funçoes.inicia_jogo(num_jogadores, pecas_jogo)

    if num_jogadores == 1:
        print('\nEssas são suas peças:\n {}'.format(jogo_inicial['jogadores']))
    elif num_jogadores > 1 and num_jogadores < 4:
        print('\nEssas são suas peças:\n {}'.format(jogo_inicial['jogadores'][0]))
    else:
        print(' ERRO!!!!! ')











    continuar = input('\nQuer continuar jogando?\n ') #continuar jogando ou parar lopping
    if continuar == 'sim': 
        i = 0
    else:
        i = 1