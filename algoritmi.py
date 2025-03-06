import matplotlib as mtl
from matplotlib.animation import FuncAnimation
def selection_sort(lista):
    n = len(lista)
    for i in range(n): # ciclo for esterno
        minimo = lista[i] # valore di minimo che verrà utilizzato per il confronto
        trovato = False # variabile sentinella
    for j in range(i+1,n): # ciclo for interno per trovare il minimo tra i valori successivi
        if lista[j] < minimo:
            trovato = True # impostiamo la variabile sentinella se viene trovato un nuovo minimo
            minimo = lista[j]
            indice_trovato = j # memorizziamo la posizione del minimo
        if trovato: # se "trovato" è True abbiamo un nuovo valore minimo e dobbiamo fare uno scambio
            occ = lista[i]
        lista[i] = lista[indice_trovato]
        lista[indice_trovato] = occ
    return lista
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
a=[2,4,6,1,5]
print( selection_sort(a))
print ( bubble_sort(a))
# what?