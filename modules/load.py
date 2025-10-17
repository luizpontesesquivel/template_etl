import os

def executar(df):
    caminho_saida = os.path.join('data_out', 'csv')
    os.makedirs(caminho_saida, exist_ok=True)
    df.to_csv(os.path.join(caminho_saida, 'saida.csv'), index=False)