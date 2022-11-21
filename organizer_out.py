import os

# comentar linha abaixo quando mover para o diretorio
os.chdir('C:/Users/andyh/Downloads')

diretorio = os.getcwd()
lista_arquivos = os.listdir(diretorio)

lista_pastas = []
for i in lista_arquivos:
    if len(i) > 3:
        pass
    else:
        lista_pastas.append(i)      

lista_movendo = []
diretorio_avaliado = []

for i in lista_pastas:
    diretorio_avaliado = os.path.join(diretorio, i) 

    lista_movendo = os.listdir(diretorio_avaliado)
    for j in lista_movendo:
        os.chdir('C:/Users/andyh/Downloads')
        os.rename(j.split('.')[-1]+'/'+j,j)
#    for j in lista_movendo:
#        print(j)
        

#        os.rename(j.split('.')[-1]+'/'+j,j)
    lista_movendo.clear()
    os.rmdir(i)
    