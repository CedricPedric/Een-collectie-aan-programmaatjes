import random


#Maakt het Uno Deck
def deckBuilder():
	deck = []
	kleuren = ['rood', 'groen', 'blauw', 'geel']
	getalen = [0,1,2,3,4,5,6,7,8,9, 'Draw Two' ,'Skip Turn', 'Reverse']
	wild = ['Wild', 'Wil Draw Four']

	for kleur in kleuren:
		for getal in getalen:
				deck.append(str(kleur) + ' ' + str(getal))
				if getal != 0:
					deck.append(str(kleur) + ' ' + str(getal))
			
	for x in range(4):
			deck.append(wild[0])
			deck.append(wild[1])

	return deck

UnoDeck = deckBuilder()
print(UnoDeck)
random.shuffle(UnoDeck)


spelers = []
amountSpelers = int(input("Vul aatal spelers in: "))


