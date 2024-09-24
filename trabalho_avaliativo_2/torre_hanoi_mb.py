import tkinter as tk  
from tkinter import messagebox  
import time  
import threading 
from math import floor  

class TorreDeHanoi(tk.Tk):  
    def __init__(self):  
        super().__init__()  
        self.title("Torre de Hanói")  
        
        self.label = tk.Label(self, text="Escolha o número de discos (1-5):")  
        self.label.pack()  
        
        self.num_disco_var = tk.IntVar()  
        self.num_disco_entry = tk.Entry(self, textvariable=self.num_disco_var)  
        self.num_disco_entry.pack()  

        self.iniciar_button = tk.Button(self, text="Iniciar", command=self.iniciar)  
        self.iniciar_button.pack()  

        self.canvas = tk.Canvas(self, width=400, height=300, bg="white")  
        self.canvas.pack()  
        
        self.peg1 = 50  
        self.peg2 = 200  
        self.peg3 = 350  

    def iniciar(self):  
        n = self.num_disco_var.get()  
        if n < 1 or n > 5:  
            messagebox.showinfo("Torre de Hanói", "Por favor, escolha um número de discos entre 1 e 5.")  
            return  
        
        self.canvas.delete("all")  
        
        # Inicializa as hastes
        self.hastes = [list(range(n, 0, -1)), [], []]  # Haste A com todos os discos, B e C vazias
        self.mostrar_hastes()  

        # Gera e imprime a matriz binária no início
        matriz = self.matriz_binaria(n)
        self.imprimir_matriz(matriz)

        # Executa a solução em uma thread
        threading.Thread(target=self.movimentar_discos, args=(n, 0, 2, 1)).start()  

    def mostrar_hastes(self):  
        self.canvas.delete("disco")  
        # Desenha as hastes
        self.canvas.create_line(self.peg1, 250, self.peg1, 50, fill="black", width=5)  # Haste A  
        self.canvas.create_line(self.peg2, 250, self.peg2, 50, fill="black", width=5)  # Haste B  
        self.canvas.create_line(self.peg3, 250, self.peg3, 50, fill="black", width=5)  # Haste C  

        # Desenha os discos
        for i, haste in enumerate(self.hastes):
            for j, disco in enumerate(haste):
                self.canvas.create_rectangle(  
                    (self.peg1 if i == 0 else self.peg2 if i == 1 else self.peg3) - (disco * 5),  
                    250 - (20 * (j + 1)),  
                    (self.peg1 if i == 0 else self.peg2 if i == 1 else self.peg3) + (disco * 5),  
                    250 - (20 * j),  
                    fill="blue",  
                    tags="disco"  
                ) 

    # Matriz que serve como base para movimentação dos discos
    def matriz_binaria(self, n):  
        m = [[0 for x in range(n)] for y in range(2**n)]  # Cria a matriz  
        for i in range(2**n):  
            for j in range(n):  
                m[i][j] = (1 if floor(i / (2 ** j)) % 2 != 0 else 0)  
        return m  

    def imprimir_matriz(self, matriz):  
        print("Matriz Binária:")  
        for linha in matriz:  
            print(linha) 

    #Quando é 1 na linha da matriz binária, na sua primeira aparição faz a movimentação do disco equivalente na coluna
    def movimentar_discos(self, n, origem, destino, auxiliar):  
        if n == 1:  
            self.mover_disco(origem, destino)  
        else:  
            self.movimentar_discos(n - 1, origem, auxiliar, destino)  
            self.mover_disco(origem, destino)  
            self.movimentar_discos(n - 1, auxiliar, destino, origem)  

    def mover_disco(self, origem, destino):  
        if self.hastes[origem]:  # Verifica se há discos na haste de origem
            disco = self.hastes[origem].pop()  # Remove o disco da haste de origem
            self.hastes[destino].append(disco)  # Adiciona o disco à haste de destino
            
            # Exibe no terminal qual disco foi movido e para onde
            print(f"Movendo disco {disco} de haste {origem + 1} para haste {destino + 1}")  
            
            self.mostrar_hastes()  
            self.update()  
            time.sleep(1.0)  # Pausa para visualização

if __name__ == "__main__":  
    app = TorreDeHanoi()  
    app.mainloop()  