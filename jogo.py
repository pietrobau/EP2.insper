from Funcoes import cria_pecas


i = 0
while i < 1: #lopping do jogo

    import Funcoes
    mesa = cria_pecas()
    print(mesa)









    continuar = input('Quer continuar jogando?\n') #continuar jogando ou parar lopping
    if continuar == 'sim': 
        i = 0
    else:
        i = 1