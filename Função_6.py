def adiciona_na_mesa(peca, mesa):   #Função 6 - Adicionando peças a mesa num jogo de dominó

    ponta = []
    nova_mesa = []
    j = len(mesa)-1
    for i in mesa:
        if i == mesa[0]:
            ponta.append(i[0])
        if i == mesa[j]:
            ponta.append(i[1])

    if mesa == []:
        nova_mesa.append(peca)
    elif peca[0] == ponta[0]:
        ladoD = peca[0]
        ladoF = peca[1]
        lado = [ladoF,ladoD]
        nova_mesa.append(lado)
        nova_mesa.extend(mesa)

    elif peca[1] == ponta[0]:
        nova_mesa.append(peca)
        nova_mesa.extend(mesa)

    elif peca[0] == ponta[1]:
        nova_mesa.extend(mesa)
        nova_mesa.append(peca)

    elif peca[1] == ponta[1]:
        ladoD = peca[1]
        ladoF = peca[0]
        lado = [ladoD,ladoF]
        nova_mesa.extend(mesa)
        nova_mesa.append(lado)

    return nova_mesa