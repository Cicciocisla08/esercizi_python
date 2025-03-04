oreP = [10, 11,13,15,17]
oreA = [11,14,18,19,20]
destinazioni = ["Roma", "Milano", "Parigi", "Praga", "Berlino"]
volo=str(input("inserisci la destinazione"))
condizione=True
print(f"per il volo {volo} l'orario di partenza è alle ")
for i in range (len(destinazioni)):
    if(destinazioni[i]==volo):
        print({oreP[i]})
        condizione=False
if(condizione):
    print("volo non presente ")
inizio=int(input("inserire l'orario di inizio dell'intervallo "))
fine=int(input("inserire l'orario di fine dell'intervallo "))
print("i voli che partono per questo intervallo sono: ")
condizione=True
for i in range (len(destinazioni)):
    if(oreP[i]>=inizio and oreP[i]<=fine):
        print(destinazione[i])
        condizione=False
if(condizione):
    print("non ci sono voli per questo intervallo di tempo ")
volo2=str(input("inserisci la destinazione"))
durataMin=24
for i in range (len(destinazioni)):
     if(destinazioni[i]==volo2):
         durata=oreA-oreP
         if(durata<durataMin):
             durataMin=durata
print(f"il volo per {volo2} più breve dura {durataMin} ore")
