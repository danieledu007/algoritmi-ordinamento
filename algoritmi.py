import matplotlib as mtl
import random
from matplotlib.animation import FuncAnimation
def selection_sort(lista,n):
   for i in range(n):
    min=i
    for j in range(i+1,n):
        if lista[min]>lista[j]:
         (lista[min],lista[j])=(lista[j],lista[min])
#    return lista
def bubble_sort(lista):
    n=len(lista)
    for i in range (n-1):
        print (list[i])
        for j in range (n-1):
            print (lista[j])
    return lista
#            if lista[j] > lista
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
selection_sort(a,length)
print(a)
#print ( bubble_sort(a))
#print(length)
# what?