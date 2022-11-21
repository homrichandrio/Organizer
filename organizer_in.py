import os

# comentar linha abaixo quando mover para o diretorio
# os.chdir('C:/Users/andyh/Downloads')

diretorio = os.getcwd()
lista_arquivos = os.listdir(diretorio)

info_arquivo = []
for i in lista_arquivos:
    info_arquivo.append(i.split('.'))

formatos = []
for i in info_arquivo:
    formatos.append(i[-1])

set_formatos = set(formatos)
set_formatos.remove('py')
for i in set_formatos:
    os.mkdir(i)

for i in lista_arquivos:
    if i.split('.')[-1] == 'py':
        pass
    else:    
        os.rename(i,i.split('.')[-1]+'/'+i)

print('programa finalizado')