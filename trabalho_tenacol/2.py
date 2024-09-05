import math,os

def imprimir_matriz(matriz, n):
    print("Matriz:")
    for i,linha in enumerate(matriz):
        for elemento in linha:
            print(elemento, end=" ")
        print("|", end=" ")
        print(imprimir_linha(i,matriz,n))

def contagem(lista):
    return lista.count(1)

def criar_matriz(n):
    colunas = 2 ** n
    matriz = [[0 for _ in range(n)] for _ in range(colunas)]

    for i in range(colunas):
        for j in range(n):
            if(math.floor((i)/(2**(j)))%2==0):
                matriz[i][j]=0
            else:
                matriz[i][j]=1 
    return matriz

def guardar(qtd, matriz):
    listaqtd = []
    for i in range(len(matriz)):
        if(contagem(matriz[i])== qtd):
            listaqtd.append(i)
    
    return listaqtd

def imprimir_linha(linha,matriz,n):
    linha_final = ""
    cont = 0
    for i,elemento in enumerate(matriz[linha]):
        if(elemento==1):
            if(cont<contagem(matriz[linha])-1):
                linha_final+= n[i]+", "
            else:
                linha_final+= n[i]
            cont+=1
        else:
            continue
    return '{'+linha_final+'}'
    
def imprimir_qtd(listaqtd,matriz,n,qtd):
    print("\n")
    print(len(listaqtd),"linhas com combinação de ",qtd," elementos\n")
    for i in range(len(listaqtd)):
        print(f"Linha {listaqtd[i]+1} => {imprimir_linha(listaqtd[i],matriz,n)}")
    print("\n")
    
os.system('cls')
text = str(input("Entre com {lista}, quantidade de elementos: "))
n = text.replace("{", "").replace("}", "").replace(" ","").split(",")
qtd = int(n[len(n)-1])
n.pop()
matriz = criar_matriz(len(n))
imprimir_matriz(matriz,n)
listaqtd = guardar(qtd,matriz)
imprimir_qtd(listaqtd,matriz,n,qtd)
