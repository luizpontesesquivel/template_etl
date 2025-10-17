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