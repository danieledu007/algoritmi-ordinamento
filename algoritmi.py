import random
import time
#def lista_random(n):
#   limite=n
#   for a in range(i,limite):
#    a=[]
#    return list
#    ra=random.randint(1,1000)
#    a.append(ra)
def selection_sort(lista,len):
    for i in range(len):
        min=i
        for j in range(i+1,len):
            if lista[min]>lista[j]:
                (lista[min],lista[j])=(lista[j],lista[min])
    return li
def bubble_sort(lista,n):
    n=len(lista)
    for i in range (n-1):
        for j in range (n-1):
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
#def merge_sort(lista):
#def merge()
a=[2,4,6,1,5]
length= len(a)
start=0
end=0
n=int(input("lunghezza della lista:"))
li=[random.sample(range(n),n)]
#for i in range(n):
li=random.sample(range(n),n)
#li.append(random.sample(range(100),n))
#ra=random.randint(0,1000)
#li.append(ra)
#lista_random(n)
start=time.time()
selection_sort(li,n)
end=time.time()
print((end-start)*1000)
#print ( bubble_sort(a))

#print(length)
# what?