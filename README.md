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
