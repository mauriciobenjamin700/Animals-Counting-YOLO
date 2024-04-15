from glob import glob
from os.path import isdir, basename, join

# Substitua 'caminho/da/pasta' pelo caminho do diretório que você quer pesquisar
caminho_da_pasta = '../animals'

def dir_images(caminho_da_pasta:str = "../animals", recursive: bool = False):
    files = []
    valid_ext = ["jpg", "png", "jpeg","JPG", "PNG","JPEG"]

    
    if recursive == True:
        # Use a função glob com '**' para pesquisar recursivamente
        for arquivo in glob(caminho_da_pasta + '/**', recursive=True):
            if not isdir(arquivo):
                if basename(arquivo).split('.')[-1] in valid_ext:
                    files.append(arquivo)
    
    else:
        for ext in valid_ext:
            for arquivo in glob(join(caminho_da_pasta,f"*.{ext}")):
                if basename(arquivo).split('.')[-1] in valid_ext:
                    files.append(arquivo)
            
    #print(len(files))

    
    return files



#files = dir_images(caminho_da_pasta)
#print(files[0])