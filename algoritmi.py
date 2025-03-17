import matplotlib as mtl
import random
from matplotlib.animation import FuncAnimation
import time
#def lista_random(n):
#   limite=n
#   for a in range(i,limite):
#    a=[]
#    return list
#    ra=random.randint(1,1000)
#    a.append(ra)
def selection_sort(lista,n):
    for i in range(n):
        min=i
    for j in range(i+1,n):
        if lista[min]>lista[j]:
         (lista[min],lista[j])=(lista[j],lista[min])
#    return lista
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
n=input("lunghezza della lista:")
#lista_random(n)
start=time.time()
selection_sort(a,length)
end=time.time()
print((end-start)*1000)
print(a)
#print ( bubble_sort(a))

#print(length)
# what?