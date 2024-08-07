
def ordenamientoBurbuja(unaLista):
    for numPasada in range(len(unaLista)-1,0,-1):
        for i in range(numPasada):
            if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp



import random
lista=[]
for i in range(500):
    x=random.randint(10000,99999)
    lista.append(x)
print(lista)
ordenamientoBurbuja(lista)
print(lista)