import heapq

numeros = (1, 4, 2, 100, 20, 750, 96, 58, 6542, 875214)
resultado = heapq.nlargest(4, numeros)
print(resultado)

resultado2=heapq.nsmallest(4, numeros)
print(resultado2)