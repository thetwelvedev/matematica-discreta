"""Questão 2 - Matriz de Combinações
A conhecida fórmula da análise combinatória:
(m,r) = m!/(m-r)!r!
nos diz quantas são as combinações de m objetos tomados r a r; no entanto, ela não diz como encontrar as tais combinações A seguir damos uma fórmula que cumpre essa finalidade.
A matriz de combinações e a fórmula geratriz são vistas a seguir:
Aij = 1, se i / 2^j é ímpar; 0, se i / 2^j é par. 
Vai entrar uma lista e um valor do número de combinações:
ex.: {a,b,c,d} e valor = 3
{{a,b,c},{a,b,d},{b,c,d},...}"""
import re
from math import floor

def MATRIZ_COMBINA(n, lista):
    tam = len(lista) #Dá o tamanho da string
    m = [[0 for x in range(tam)] for x in range(2**tam)] # forma a matriz / List Comprehension
    soma = 0
    lista_resultado = []
    for i in range(2**tam):
        for j in range(tam):
            if floor(i / 2**j) % 2 == 0:
                m[i][j] = 0
            else:
                m[i][j] = lista[j] # cada coluna tem um elemento equivalente a ela, na matriz que antes era 1 agora fica o próprio elemento equivalente(que vai ter uma posição na string)
                soma += 1 # vai somar para cada vez que um elemento aparecer na linha
        if soma == n: # Compara a ocorrência de elementos que não seja 0 na linha com a quantidade de elementos que é para ter na combinação
            lista_resultado.append(m[i]) # Coloco os elementos na lista onde vai mostrar as combinações
        soma = 0 # Zera para soma dá próxima linha
    lista_sem_zeros = [[elemento for elemento in sublista if elemento != 0] for sublista in lista_resultado] # Retira os zeros da lista
    return print(lista_sem_zeros)

# Execução
lista = str(input("Coloque a lista de elementos: ")) 
lista_trabalhada = re.sub(r'[ {},;/]','', lista) #elimina qualquer um desses caracteres
n = int(input("Digite o número de combinação: "))
MATRIZ_COMBINA(n, lista_trabalhada)