#es1
anni=int(input("inserire il numero di anni di servizio"))#variabile input
livello=int(input("inserire il livello di programmazione: 1,2 o 3"))#variabile input
if(livello==1):
    if(anni==1):
        bonus=100
    elif(anni>1 and anni<=3):
        bonus=200
    elif(anni>3 and anni>=5):
        bonus=300
    elif(anni>5 and anni<=7):
        bonus=400
    elif(anni>7):
        bonus=500
    else:
        print("errore")
        bonus=0
elif(livello==2):
    if(anni==1):
        bonus=200
    elif(anni>1 and anni<=3):
        bonus=300
    elif(anni>3 and anni>=5):
        bonus=400
    elif(anni>5 and anni<=7):
        bonus=500
    elif(anni>7):
        bonus=600
    else:
        print("errore")
        bonus=0
elif(livello==3):
    if(anni==1):
        bonus=300
    elif(anni>1 and anni<=3):
        bonus=400
    elif(anni>3 and anni>=5):
        bonus=500
    elif(anni>5 and anni<=7):
        bonus=600
    elif(anni>7):
        bonus=700
    else:
        print("errore")
        bonus=0
else:
    print("errore")
    bonus=0
print(f"il bonus di produttività è di {bonus}")
#es2
voto1=int(input("inserire il primo voto"))#variabile input
voto2=int(input("inserire il secondo voto"))#variabile input
voto3=int(input("inserire il terzo voto"))#variabile input
restituzioneMedia=int(input("inserire 1 se si vuole la media in decimi e 2 se si vuole la media in centesimi"))
media=(voto1+voto2+voto3)/3
if(restituzioneMedia==1):
    print(f"la media dei tre voti in decimi è {round(media,2)}")
elif(restituzioneMedia==2):
    media=media*100/10
    print(f"la media dei tre voti in centesimi è {round(media,2)}")
else:
    print("errore")
#es3
lancio1=float(input("inserire la lunghezza del primo lancio, 0 se nullo"))#variabile input
lancio2=float(input("inserire la lunghezza del secondo lancio, 0 se nullo"))#variabile input
lancio3=float(input("inserire la lunghezza del terzo lancio, 0 se nullo"))#variabile input
lancio4=float(input("inserire la lunghezza del quarto lancio, 0 se nullo"))#variabile input
lancio5=float(input("inserire la lunghezza del quinto lancio, 0 se nullo"))#variabile input
conto=0
media=0
if (lancio1!=0):
    media=media+lancio1
    conto=conto+1
if (lancio2!=0):
    media=media+lancio2
    conto=conto+1
if (lancio3!=0):
    media=media+lancio3
    conto=conto+1
if (lancio4!=0):
    media=media+lancio4
    conto=conto+1
if (lancio5!=0):
    media=media+lancio5
    conto=conto+1
if(conto==0):
    print("ci sono stati solo lanci nulli")
else:
    media=media/conto
    print(f"la media dei {conto} lanci è di {media}")