import random 
def cria_pecas():
    lista_de_pecas=[]
    for i in range(7):
        for j in range(i,7):
            lista_de_pecas.append([i,j])
    random.shuffle(lista_de_pecas)
    return lista_de_pecas


    