import pandas as pd
from procura_arquivos import procura

matrizes_diagonais = procura("matriz_diagonal_Z_real*.csv", "./arquivos_csv_base/")
lista_de_nos = pd.read_csv("./arquivos_csv_base/lista_de_nos.csv", index_col=0).drop([0,1,2])
lista_de_nos = lista_de_nos.reset_index(drop=True)
lista_de_nos_numpy = lista_de_nos.to_numpy()
modos_criticos = pd.DataFrame(columns=["local","magnitude"])

for matriz in matrizes_diagonais:
    indice_modo_critico = []
    matriz_atual = pd.read_csv("./arquivos_csv_base/{}".format(matriz), index_col=0)
    matriz_atual.index = lista_de_nos
    matriz_atual.columns = lista_de_nos
    matriz_atual_complexa = matriz_atual.astype(complex)
    matriz_atual_real = matriz_atual_complexa.abs()
    valores_maximos = matriz_atual_real.max()
    modo_critico = valores_maximos.max()
    indice_modo_critico = [i for i, x in enumerate(valores_maximos) if x == modo_critico][0]
    no_modo_critico = lista_de_nos_numpy[indice_modo_critico]
    modos_criticos.loc[matriz] = no_modo_critico, modo_critico

modos_criticos.to_csv('./modos_criticos.csv')
