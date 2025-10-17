import os
import pandas as pd

def executar():
    caminho_csv = os.path.join('data_in', 'csv')
    arquivos = [f for f in os.listdir(caminho_csv) if f.endswith('.csv')]

    dados = []

    for arquivo in arquivos:
        caminho = os.path.join(caminho_csv, arquivo)
        df = pd.read_csv(caminho)
        dados.append(df)

    if dados:
        return pd.concat(dados, ignore_index=True)
    else:
        return pd.DataFrame()