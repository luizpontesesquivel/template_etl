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