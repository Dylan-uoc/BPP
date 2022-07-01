"""Haga uso de la función filter para construir un programa que, dado una lista de n números devuelva aquellos que son primos. 
Por ejemplo, dada la lista [3, 4, 8, 5, 5, 22, 13], el programa que implemente debe devolver como resultado [3, 5, 5, 13]"""

lista = [3, 4, 8, 5, 5, 22, 13]

def es_primo(n):
    primo = True
    for i in range(2, n):
        if(n%i == 0):
            primo = False
    return primo

filter_primos = filter(lambda x: es_primo(x), lista)

if __name__ == '__main__':
    print(list(filter_primos))
    
    