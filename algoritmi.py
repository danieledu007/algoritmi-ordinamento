import random
import time
import matplotlib
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
def insertion_sort(lista,n):
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
    sinistra=merge_sort(lista[:mid],mid)
    destra=merge_sort(lista[mid:],n-mid)

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
def heapify(lista,n,i):
    max=i
    #index sinistro 
    l=2*i+1
    #index destro
    r=2*i+2
    #se rama destra è maggiore della radice
    if l<n and lista[l]>lista[max]:
         max=l
    #se rama sinistra è maggiore della radice
    if r<n and lista[r]>lista[max]:
        max=r
    #se la radice non è la più grande
    if max !=i:
        (lista[i],lista[max])=(lista[max],lista[i])
        heapify(lista,n,max)
    
def heap_sort(lista,n):
    for i in range(n//2-1,-1,-1):
        heapify(lista,n,i)
    for i in range(n-1,0,-1):
        (lista[0],lista[i])=(lista[i],lista[0])
        heapify(lista,i,0)
    return li
        
punti=[]
start=0
end=0
n=int(input("lunghezza della lista:"))
f=int(input("iterazioni da fare:"))
 #generatore di numeri unici casuali 
for a in range(n):
    li=0
    li=random.sample(range(n),n)


#tempo bubble sort:
print("Bubble sort:")
#for i in range(f):
start=time.time()
selection_sort(li.copy(),n)
end=time.time()
#tentativo per fare un grafico
#punti.append(((end-start)*1000))
print(f"il tempo è:{(end-start)*1000} ms")

# Tempo insertion sort
print("Insertion Sort:")
start = time.time()
insertion_sort(li.copy(),n)
end = time.time()
print(f"il tempo è: {(end-start)*1000} ms")

# Tempo merge sort
print("Merge Sort:")
start = time.time()
merge_sort(li.copy(),n)
end = time.time()
print(f"Il tempo è: {(end-start)*1000} ms")
#heap sort
print("Heap Sort:")
start = time.time()
heap_sort(li.copy(),n)
end = time.time()
print(f"Il tempo è: {(end-start)*1000} ms")
#selection_sort(a,length)
