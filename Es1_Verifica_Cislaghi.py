negozio=['gucci','fendi','armani','disel','versace']
vendite_max=[16000, 12500, 11030, 13000, 14050]
vendite_min=[6700, 4530, 8030, 7600, 6150]
media_max=0
media_min=0

for i in range (len(negozio)):
    media_max+=vendite_max[i]
    media_min+=vendite_min[i]
media_max=media_max/len(negozio)
media_min=media_min/len(negozio)
print(f"la media delle vendite massime è di {media_max} mentre la media delle vendite minime è di {media_min} ")
print("i negozi con la vendita minima sotto la media sono: ")
for i in range (len(negozio)):
    if (vendite_min[i]<media_min):
        print(negozio[i])
nome=str(input("inserire il nome di un negozio "))
condizione=False
for i in range (len(negozio)):
    if(negozio[i]==nome):
        condizione=True
if(condizione):
    print(f"il negozio {nome} è presente nell'elenco ")
else:
    print(f"il negozio {nome} non è presente nell'elenco ") 
vendita_alta=vendite_max[0]
vendita_bassa=vendite_min[0]
indice_max=0
indice_min=0
for i in range (len(negozio)):
    if(vendita_alta<vendite_max[i]):
        vendita_alta=vendite_max[i]
        indice_max=i
    if(vendita_bassa>vendite_min[i]):
        vendita_bassa=vendite_max[i]
        indice_min=i
print(f"il negozio con la vendita maggiore è {negozio[indice_max]} mentre il negozio con la vendita minore è {negozio[indice_min]} ")