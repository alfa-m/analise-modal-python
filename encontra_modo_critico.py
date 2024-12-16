import pandas as pd
from procura_arquivos import procura

matrizes_diagonais = procura("matriz_diagonal_Z_real*.csv", "./arquivos_csv_base/")
modos_criticos = []

for matriz in matrizes_diagonais:
    matriz_atual = pd.read_csv("./arquivos_csv_base/{}".format(matriz))
    print("Matriz diagonal analisada:\n")
    print(matriz_atual)
    matriz_real_atual = matriz_atual.abs()
    print("Matriz diagonal analisada:\n")
    print(matriz_real_atual)
    matriz_real_atual.describe()
    print("Modo crítico:\n")
    modo_critico = matriz_real_atual.to_numpy().max()
    print(modo_critico)
    modos_criticos.append(modo_critico)


#df.max(numeric_only=True).max()