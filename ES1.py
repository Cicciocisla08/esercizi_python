fascine=int(input("Inserire il numero di fascine da acquistare "))
sacchi=int(input("Inserire il numero di sacchi da acquistare "))
bancali=int(input("Inserire il numero di bancali da acquistare "))
peso=(fascine*5)+(sacchi*20)+(bancali*50)
costo=peso*0.8
if(costo>100):
  sconto=costo/100*15
else:
  sconto=0
costotot=costo-sconto+3
print(f"Peso totale: {peso}kg")
print(f"Prezzo della legna senza sconto: {round(costo, 2)}€")
print(f"Sconto applicato: {round(sconto, 2)}€")
print(f"Spese di trasporto: 3€")
print(f"Prezzo finale su scontrino: {round(costotot, 2)}€")