import random
import time
def selection_sort(lista,len):
    for i in range(len):
        min=i
        for j in range(i+1,len):
            if lista[min]>lista[j]:
                (lista[min],lista[j])=(lista[j],lista[min])
    return li
def bubble_sort(lista, n):
    for i in range(n):
        scambio = False
        for j in range(0, n-i-1): 
            if lista[j] > lista[j+1]:
                (lista[j], lista[j+1]) = (lista[j+1], lista[j])
                scambio = True
        if scambio == False:  
            break
    return lista
def insertion_sort(lista):
    n = len(lista)
    for i in range(1,n): # effettua n-1 iterazioni a partire dal secondo elemento della lista
        valore = lista[i] # salviamo il valore i-esimo
        j = i-1
    while j >= 0 and valore < lista[j]:
        lista[j+1] = lista[j] # effettua almeno uno spostamento verso destra dei valori maggiori di "valore"
        j -= 1
        lista[j+1] = valore
    return lista
def merge_sort(lista,n):
    if n<=1:
        return lista
    mid=n//2
    #divide la lista fino a valori singoli
    sinistra=merge_sort(lista[:mid])
    destra=merge_sort(lista[mid:])

    return merge(destra,sinistra)
def merge(destra,sinistra):
    risultato = []
    i = j = 0
    
    # Confronta elementi liste e aggiunge il più piccolo
    while i < len(sinistra) and j < len(destra):
        if sinistra[i] <= destra[j]:
            risultato.append(sinistra[i])
            i += 1
        else:
            risultato.append(destra[j])
            j += 1
    
    # Aggiunge gli elementi rimanenti
    risultato.extend(sinistra[i:])
    risultato.extend(destra[j:])
    return risultato

a=[4,2,6,1,5]
length= len(a)
start=0
end=0
n=int(input("lunghezza della lista:"))
li=[random.sample(range(n),n)]
#for i in range(n):
li=random.sample(range(n),n)

#tempo bubble sort:
start=time.time()
selection_sort(li,n)
end=time.time()

print((end-start)*1000)
#selection_sort(a,length)
bubble_sort(a,length)
print(a)
#print ( bubble_sort(a))
