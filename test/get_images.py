from glob import glob
from os.path import isdir

# Substitua 'caminho/da/pasta' pelo caminho do diretório que você quer pesquisar
caminho_da_pasta = '../animals'

def dir_images(caminho_da_pasta:str = "../animals"):
    files = []

    # Use a função glob com '**' para pesquisar recursivamente
    for arquivo in glob(caminho_da_pasta + '/**', recursive=True):
        if not isdir(arquivo):
            files.append(arquivo)
            
            
    #print(len(files))

    
    return files


#files = dir_images(caminho_da_pasta)
#print(files[0])