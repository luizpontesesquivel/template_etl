Claro! Aqui está **todo o código e estrutura do template** conforme solicitado, pronto para copiar e colar. O projeto é simples, modular, e pronto para execução via CLI em qualquer servidor.

---

### 📁 Estrutura de Pastas

```
projeto_etl/
│
├── data_in/
│   ├── csv/
│   ├── json/
│   ├── txt/
│   └── xlsx/
│
├── data_out/
│   ├── csv/
│   ├── json/
│   ├── txt/
│   └── xlsx/
│
├── log/
│
├── temp/
│
├── modules/
│   ├── __init__.py
│   ├── extract.py
│   ├── tratact.py
│   └── load.py
│
├── limpeza.py
├── main.py
└── README.md
```

---

### 📄 `README.md`

````markdown
# Projeto ETL via CLI

Template universal para execução de pipelines de ETL em servidores via linha de comando.

## Estrutura

- **data_in/**: arquivos de entrada organizados por extensão
- **data_out/**: arquivos de saída organizados por extensão
- **log/**: arquivos de log
- **temp/**: arquivos temporários
- **modules/**: scripts de extração, tratamento e carga

## Execução

```bash
python main.py
````

## Limpeza de arquivos temporários e caches

```bash
python limpeza.py
```

````

---

### 🧹 `limpeza.py`

```python
import os
import shutil

def limpar_cache(path='.'):
    for root, dirs, files in os.walk(path):
        for dir_ in dirs:
            if dir_ == '__pycache__':
                shutil.rmtree(os.path.join(root, dir_))
        for file in files:
            if file.endswith('.pyc') or file.endswith('.pyo'):
                os.remove(os.path.join(root, file))

if __name__ == '__main__':
    limpar_cache()
    print("Arquivos de cache e __pycache__ removidos com sucesso.")
````

---

### 🚀 `main.py`

```python
import logging
from modules import extract, tratact, load
import os
from datetime import datetime

# Setup de logging
log_dir = 'log'
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, f"etl_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Iniciando processo ETL")

    try:
        dados = extract.executar()
        dados_tratados = tratact.executar(dados)
        load.executar(dados_tratados)
        logging.info("Processo ETL finalizado com sucesso")

    except Exception as e:
        logging.error(f"Erro durante o processo ETL: {str(e)}")

if __name__ == "__main__":
    main()
```

---

### 🧱 `modules/__init__.py`

```python
# Permite que a pasta modules seja tratada como pacote
```

---

### 📥 `modules/extract.py`

```python
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
```

---

### 🧪 `modules/tratact.py`

```python
def executar(df):
    # Exemplo de tratamento: remove linhas com valores nulos
    df_tratado = df.dropna()
    return df_tratado
```

---

### 📤 `modules/load.py`

```python
import os

def executar(df):
    caminho_saida = os.path.join('data_out', 'csv')
    os.makedirs(caminho_saida, exist_ok=True)
    df.to_csv(os.path.join(caminho_saida, 'saida.csv'), index=False)
```

---

Tudo pronto para uso.

> ✅ **Dica**: você pode facilmente adaptar cada parte do `extract.py`, `tratact.py` e `load.py` conforme o tipo de dado ou necessidade da sua pipeline.

Se quiser que eu adicione suporte para múltiplos formatos (JSON, XLSX, etc.) ou um controle de configuração (via `.env` ou YAML), posso te ajudar a expandir.
