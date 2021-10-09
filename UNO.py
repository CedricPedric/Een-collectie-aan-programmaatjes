import random

def deckBuilder():
	kaarten = []
	kleuren = ["Rood","Blauw","Groen","Geel"]
	waardes = ["0","1","2","3","4","5","6","7","8","9","Draw Two","Skip Turn","Reverse"]

	kaart = {"Kleur": 0, "Waarde": 0}
	for kleur in kleuren:
		for waarde in waardes:
			kaart = {"Kleur": kleur, "Waarde": waarde}
			kaarten.append(kaart)
	return kaarten

UnoDeck = deckBuilder()

print(UnoDeck)

chosenCard = UnoDeck[0]
randomCard = random.choice(UnoDeck)


print(chosenCard)
print(randomCard)

if randomCard["Waarde"] == chosenCard["Waarde"] or randomCard["Kleur"] == chosenCard["Kleur"]:
	print("Je kan spelen!")
else:
	print("Je kan niet spelen")
