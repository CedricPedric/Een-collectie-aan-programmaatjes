import random

def deckBuilder():
	kaarten = []
	kleuren = ["Rood","Blauw","Groen","Geel"]
	waardes = ["0","1","2","3","4","5","6","7","8","9"]

	kaart = {"Kleur": 0, "Waarde": 0}
	for kleur in kleuren:
		for waarde in waardes:
			kaart = {"Kleur": kleur, "Waarde": waarde}
			kaarten.append(kaart)
	return kaarten


def canPlay(TopCard:dict, HandPlayer:list):
	for x in range(len(HandPlayer)):
		if TopCard["Waarde"] == HandPlayer[x]["Waarde"] or TopCard["Kleur"] == HandPlayer[x]["Kleur"]:
			print("Je kan spelen!")
			return True
		else:
			print("Je kan niet spelen!")
			return False

def drawCards(amountCards):
	cardsDrawn = []
	for x in range(amountCards):
		cardsDrawn.append(UnoDeck.pop(0))
	return cardsDrawn



UnoDeck = deckBuilder()
random.shuffle(UnoDeck)




players = []
inputHowManyPlayer = int(input("Vul het aantal spelers in: "))

for z in range(inputHowManyPlayer):
	PlayerCards = drawCards(7)
	players.append(PlayerCards)

print(len(players[0]))
topCard = UnoDeck[0]
print("Top Card = " + topCard["Kleur"], topCard["Waarde"])


