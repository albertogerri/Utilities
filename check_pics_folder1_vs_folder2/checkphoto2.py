import os
import sys

#logs salvati qui
logs=open("logs.txt", "w")
logs.close() 

# Scopo: controllare che le immagini dentro la cartella1 non siano già presenti nella cartella_target. se ci sono già allora si vogliono spostare queste immagini in cartelle junk.


## script generico
# ottenere info di nome + dimensione dei file
def funzione(cartella_da_esaminare):
    listone=[]
    sottofiles=os.listdir(cartella_da_esaminare)
    for sottofile in sottofiles:
        if os.path.isfile(cartella_da_esaminare+'\\'+sottofile):
            dati={'nome_intero':cartella_da_esaminare+'\\'+sottofile,
                  'nome':sottofile,
                  'cartella':cartella_da_esaminare,
                  'dim':os.stat(cartella_da_esaminare+'\\'+sottofile).st_size}
            listone=listone+[dati]
        if os.path.isdir(cartella_da_esaminare+'\\'+sottofile):
            listone=listone+funzione(cartella_da_esaminare+'\\'+sottofile)
    return listone


# qui leggi i nomi di tutti i file immagine dentro la cartella da controllare e salvali in una lista1
cartella1=r"nome_directory_1"
# lista1 = os.listdir(cartella1)
lista1=funzione(cartella1)

# qui leggi i nomi di tutti i file dentro tutte le sottocartelle di una cartella target salvali in una lista_target
cartella_target=r'nome_directory_2'
# sottocartelle=os.listdir(cartella_target)
listone=funzione(cartella_target)

#nuovo script
for pic in lista1:
    for pic_2 in listone:
        if pic_2['nome']==pic['nome'] and pic_2['dim']==pic['dim']:
            #muoviamo to junk
            junk=pic['cartella']+'\\gia_fatto'
            if not os.path.exists(junk):
                os.makedirs(junk)
            try:
                os.rename(pic['nome_intero'],junk+'\\'+pic['nome'])
            except:
                print(pic['nome_intero']+' non trovata \n')
            #scriviamo su log
            log_string=pic['nome']+' trovata in folder '+ pic_2['cartella']+'\n'
            logs=open("logs.txt", "a")
            logs.write(log_string)
            logs.close()







