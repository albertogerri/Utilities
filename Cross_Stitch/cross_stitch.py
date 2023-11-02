from PIL import Image, ImageDraw
import numpy as np
from scipy.spatial import cKDTree
from sklearn.cluster import KMeans

# input
image_name='marte-NASA.jpg'

colori_filo=15
dim_punto = 10 #ogni quanti pixel tiro la linea
# info: numero punti saranno = pix_l*pix_h/dim_punto^2


# Carica l'immagine
image = Image.open(image_name)

# Ridimensiona l'immagine a 1000 pixel
# new_size = (pix_l, pix_h)  # colonne x righe
# image = image.resize(new_size)

# size immagine
new_size=image.size

# Converte l'immagine in un array numpy
image_array = np.array(image)

# Get the picture palette
km=KMeans(colori_filo, n_init='auto')
image_array_reshape=np.unique(image_array.reshape((image_array.shape[0]*image_array.shape[1],3)),axis=0)

groups=km.fit(image_array_reshape)
palette_array=groups.cluster_centers_

# Estrai i colori dalla palette (supponiamo che tu abbia una lista di 10 colori in formato RGB)
# palette = [
#     (128, 64, 0),    # Marrone scuro
#     (179, 89, 0),    # Marrone arancio
#     (204, 102, 0),   # Arancio scuro
#     (230, 115, 0),   # Arancio
#     (255, 128, 0),   # Arancio brillante
#     (255, 153, 102), # Rosso chiaro
#     (255, 77, 77),   # Rosso acceso
#     (255, 51, 51),   # Rosso brillante
#     (204, 51, 51),   # Rosso scuro
#     (153, 0, 0),     # Rosso profondo
#     (0, 0, 0)        # Nero
# ]
# Converte la lista di colori in un array numpy
# palette_array = np.array(palette)

# Calcola l'albero KD per la palette dei colori
tree = cKDTree(palette_array)

story=[]
# Per ogni pixel nell'immagine, trova il colore più vicino dalla palette
for i in range(new_size[1]):
    for j in range(new_size[0]):
        if (i%dim_punto==1) & (j%dim_punto==1):
            story=story+[i,j]
            pixel = image_array[i][j]
            closest_color_index = tree.query(pixel)[1]
            closest_color = palette_array[closest_color_index].tolist()
            # dimensione 2x2
            # print(closest_color)
            for z in range(dim_punto-1):
                for u in range(dim_punto-1):
                    try:
                        image_array[i+z][j+u] = closest_color
                    except:
                        continue


# Crea una nuova immagine con i colori più vicini
new_image = Image.fromarray(image_array.astype('uint8'))

# Crea un disegno su cui verrà disegnata la griglia
draw = ImageDraw.Draw(new_image)

# Specifica il colore dei bordi (in questo caso, grigio)
colore_bordo = (128, 128, 128)
colore_bordo_10=(200,200,200)

# Specifica le dimensioni della griglia (dimensione dei rettangoli)

# Disegna la griglia sulla tua immagine
larghezza, altezza = image.size
for x in range(0, larghezza, dim_punto):
    if (x/dim_punto)%10==0:
        draw.line([(x, 0), (x, altezza)], fill=colore_bordo_10, width=1)
    else:
        draw.line([(x, 0), (x, altezza)], fill=colore_bordo, width=1)
for y in range(0, altezza, dim_punto):
    if (y/dim_punto)%10==0:
        draw.line([(0, y), (larghezza, y)], fill=colore_bordo_10, width=1)
    else:
        draw.line([(0, y), (larghezza, y)], fill=colore_bordo, width=1)

# Salva l'immagine con la griglia
new_image.save('output_'+image_name)

