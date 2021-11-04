import random 
def cria_pecas():
    lista_de_pecas=[]
    for i in range(7):
        for j in range(i,7):
            lista_de_pecas.append([i,j])
    random.shuffle(lista_de_pecas)
    return lista_de_pecas
#___________________________________________________________________________________________________________________

def inicia_jogo(numero_de_jogadores, pecas): #Função 2- Inicia jogo
    mesa=[]
    dicionario={
        'jogadores':{},
        'monte':[],
        'mesa':[]
    }

    for i in range(numero_de_jogadores):
        dicionario["jogadores"][i]=pecas[0+(i*7):7+(i*7)]
    dicionario["monte"]=pecas[numero_de_jogadores*7::]

    return dicionario
#___________________________________________________________________________________________________________________

def verifica_ganhador (dicionario): #Função 3 - verificar vencedor
    for jogador in dicionario:
        pecas_do_jogador= dicionario[jogador]
        if len(pecas_do_jogador) == 0:
            return jogador
    return -1
#___________________________________________________________________________________________________________________

def soma_pecas(pecas):   #Função 4 - Soma peças do dominó

    contar = []
    
    for i in pecas:
        contar.extend(i)
    total = sum(contar)
    
    return total
#___________________________________________________________________________________________________________________

def posicoes_possiveis(mesa, pecas):   #Função 5 - Posições possíveis da mão

    pontas = []
    qnt = []

    if mesa == []:
        todos = [0]*len(pecas)
        i = 0
        while i<len(pecas):
            todos[i] = i
            i = i + 1
        return todos

    j = len(mesa)-1
    for i in mesa:
        if i == mesa[0]:
            pontas.append(i[0])
        if i == mesa[j]:
            pontas.append(i[1])

    for f in pecas:
        if f[0] == pontas[0] or f[0] == pontas[1] or f[1] == pontas[1] or f[1] == pontas[0]:
            qnt.append(f)
    
    i = 0
    j = 0
    posicao = [0]*len(qnt)
    while i < len(pecas):
        f = pecas[i]
        if f[0] == pontas[0] or f[0] == pontas[1] or f[1] == pontas[1] or f[1] == pontas[0]:
            posicao[j] = i
            j = j + 1
        i = i + 1
            
    return posicao
#___________________________________________________________________________________________________________________

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