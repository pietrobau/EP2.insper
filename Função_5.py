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