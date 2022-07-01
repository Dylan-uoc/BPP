import pdb
pdb.set_trace()

"""Haciendo uso de comprensión de listas realice un programa que, dado una lista de listas de 
números enteros, devuelva el máximo de cada lista"""

lista1 = [2, 4, 1]
lista2 = [1,2,3,4,5,6,7,8]
lista3 = [100,250,43]

lista_maximos = [max(i) for i in [lista1, lista2, lista3]]
print(lista_maximos)