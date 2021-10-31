def soma_pecas(pecas):   #Função 4 - Soma peças do dominó

    contar = []
    
    for i in pecas:
        contar.extend(i)
    total = sum(contar)
    
    return total