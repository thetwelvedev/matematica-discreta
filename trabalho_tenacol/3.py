import sympy as sp
import matplotlib.pyplot as plt;
import numpy as np


def gerar_formula_soma_potencias(m):
    n = sp.symbols('n')
    
    def a(m,j):
        soma = sum(((-1)**k)*sp.binomial(j,k)*(1-k+j)**m for k in range(j+1))
        return soma
    
    def soma_potencias(m):
        termo = sum(sp.binomial(n, j+1) * a(m,j) for j in range(m + 1))
        return termo 

    formula = soma_potencias(m)
    
    formula = sp.simplify(formula)
    
    return formula

m = int(input("Valor de M: "))
formula = gerar_formula_soma_potencias(m)
print(formula)

# Plota a função
sp.init_printing()
fig, ax = plt.subplots(figsize=(8, 2))
ax.text(0.5, 0.5, f"${sp.latex(formula)}$", size=24, ha='center', va='center')
ax.axis('off')
plt.show()


