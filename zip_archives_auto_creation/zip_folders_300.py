import os
import zipfile

#path della cartella con dentro i file da comprimere - NB: crea una sottocartella nella stessa directory
path='nome_cartella'
#inzio nome archivi zip da max300
in_nome="archivi_"

flag = 1
j=1
peso_max = 300 #MB
#ciclo while flag =1
while flag == 1:
    # crea la lista dei files list_files
    list_files=os.listdir(path)
    # lista dei files nella sotto-cartella è vuota? sì -> flag = 0
    if not list_files:
        flag=0
        break
    #nome file
    nome_file_vecchio="file da comprimere\\"+list_files[0]
    #sposto il file dalla sottocartella alla main cartella
    nome_file=list_files[0]
    os.replace(nome_file_vecchio,nome_file)
    # prendi il primo file e aggiungilo all'archivio j-esimo
    nome_archivio=in_nome+str(j)+".zip"
    with zipfile.ZipFile(nome_archivio, mode="a") as archive:
        archive.write(nome_file)
    # cancella il file dalla cartella
    os.remove(nome_file)
    # l'archivio pesa >300MB? si -> j = j+1
    peso=os.path.getsize(nome_archivio)*1e-6
    # print(peso)
    if peso>=peso_max:
        j=j+1
