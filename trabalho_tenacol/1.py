import math

def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=" ")
        print()

def criar_matriz(n):
    colunas = 2 ** n

    matriz = [[0 for _ in range(n)] for _ in range(colunas)]

    for i in range(colunas):
        for j in range(n):
            if(math.floor(((i+1)-1)/2**(n-(j+1))) %2==0):
                matriz[i][j]=0
            else:
                matriz[i][j]=1 

    return matriz

n = int(input("Valor de N(Entradas da matriz): "))
matriz = criar_matriz(n)
imprimir_matriz(matriz)