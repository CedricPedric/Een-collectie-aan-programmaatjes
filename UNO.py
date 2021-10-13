import random
UnoDeck = []
def deckBuilder():
	kaarten = []
	kleuren = ["Rood","Blauw","Groen","Geel"]
	waardes = ["0","1","2","3","4","5","6","7","8","9","Draw Two","Skip","Reverse"]
	kaart = {"Kleur": 0, "Waarde": 0}
	for kleur in kleuren:
		for waarde in waardes:
			kaart = {"Kleur": kleur, "Waarde": waarde}
			kaarten.append(kaart)
	for x in range(4):
		kaarten.append({"Kleur":"Wild","Waarde":"Draw Four"})
		kaarten.append({"Kleur":"Wild","Waarde":"Null"})
	return kaarten

def canPlay(TopCard:dict, HandPlayer:list):
	for x in range(0, len(HandPlayer)):
		if TopCard["Waarde"] == HandPlayer[x]["Waarde"] or TopCard["Kleur"] == HandPlayer[x]["Kleur"] or HandPlayer[x]["Kleur"] == "Wild":
			print("Je kan spelen!")
			return True	
	print("Je kan niet spelen!")
	return False

def drawCards(amountCards):
	global UnoDeck
	cardsDrawn = []
	for x in range(amountCards):
		cardsDrawn.append(UnoDeck.pop(0))
	return cardsDrawn


def isWinner(players:list):
    for z in range( len(players) ):
        currentPlayer = z + 1
        if len(players[z]) == 0:
            print(f"Player {currentPlayer} is the winner!")
            return True
    return False

def showHand(currentHand:list):
	print("-"*25)
	for z in range(len(currentHand)):
		print("Kaart",str(z + 1) + ":", "Kleur:", str(currentHand[z]["Kleur"]), "Value:", str(currentHand[z]["Waarde"]))
	print("-"*25)

def whatCanBePlayed(topCard:dict,givenHand:list):
    playableCards = []
    for z in range(len(givenHand)):
        if givenHand[z]["Kleur"] == topCard["Kleur"] or givenHand[z]["Waarde"] == topCard["Waarde" or givenHand[z]["Kleur"] == "Wild"]:
            playableCards.append(givenHand[z])    
    return playableCards

def whatIsTheHighest(givenCards:list):
    highestValue = givenCards[0]
    for posite in range(len(givenCards)):
        if givenCards[posite]["Waarde"] == "Draw Two" or givenCards[posite]["Waarde"] == "Reverse" or givenCards[posite]["Waarde"] == "Skip":
            return givenCards[posite]
        elif givenCards[posite]["Waarde"] > highestValue["Waarde"]:
            highestValue = givenCards[posite]
    return highestValue

def mostColor(currentHand:list):
    amountCards = len(currentHand)
    greenCards = []
    redCards = []
    blueCards = []
    yellowCards = []

    for positie in range(amountCards):
        cardColor = currentHand[positie]["Kleur"]
        if cardColor == "Groen":
            greenCards.append(currentHand[positie])
        elif cardColor == "Rood":
            redCards.append(currentHand[positie])
        elif cardColor == "Blauw":
            blueCards.append(currentHand[positie])
        elif cardColor == "Geel":
            yellowCards.append(currentHand[positie])

    mostColors = ""
    if len(greenCards) > len(redCards) and len(greenCards) > len(blueCards) and len(greenCards) > len(yellowCards):
        mostColors = "Groen"
    elif len(redCards) > len(greenCards) and len(redCards) > len(blueCards) and len(redCards) > len(yellowCards):
        mostColors = "Rood"
    elif len(blueCards) > len(redCards) and len(blueCards) > len(greenCards) and len(blueCards) > len(yellowCards):
        mostColors = "Blauw"
    elif len(yellowCards) > len(redCards) and len(yellowCards) > len(greenCards) and len(yellowCards) > len(blueCards):
        mostColors = "Geel"
    else:
        return currentHand[0]["Kleur"]
    return mostColors

def whatMove(currentHand:list,topCard:dict,playableCards:list):
    amountCards = len(currentHand)
    greenCards = []
    redCards = []
    blueCards = []
    yellowCards = []

    for positie in range(amountCards):
        cardColor = currentHand[positie]["Kleur"]
        if cardColor == "Groen":
            greenCards.append(currentHand[positie])
        elif cardColor == "Rood":
            redCards.append(currentHand[positie])
        elif cardColor == "Blauw":
            blueCards.append(currentHand[positie])
        elif cardColor == "Geel":
            yellowCards.append(currentHand[positie])
        elif cardColor == "Wild":
            return currentHand[positie]

    mostColors = ""
    if len(greenCards) > len(redCards) and len(greenCards) > len(blueCards) and len(greenCards) > len(yellowCards):
        mostColors = greenCards
    elif len(redCards) > len(greenCards) and len(redCards) > len(blueCards) and len(redCards) > len(yellowCards):
        mostColors = redCards
    elif len(blueCards) > len(redCards) and len(blueCards) > len(greenCards) and len(blueCards) > len(yellowCards):
        mostColors = blueCards
    elif len(yellowCards) > len(redCards) and len(yellowCards) > len(greenCards) and len(yellowCards) > len(blueCards):
        mostColors = yellowCards
    else:
        return whatIsTheHighest(playableCards)
    
    if topCard["Kleur"] == mostColors[0]["Kleur"]:
        return whatIsTheHighest(mostColors)
            
    else:
        mostColorPlayable = []
        specialValuesPlayable = []
        highestValue = playableCards[0]
        for z in range(len(playableCards)):
            if playableCards[z]["Kleur"] == mostColors[0]["Kleur"]:
                mostColorPlayable.append(playableCards[z])
            elif playableCards[z]["Waarde"] == "Draw Two" or playableCards[z]["Waarde"] == "Reverse" or playableCards[z]["Waarde"] == "Skip":
                specialValuesPlayable.append(playableCards[z])
            elif playableCards[z]["Waarde"] > highestValue["Waarde"]:
                highestValue = playableCards[z]
        
        if len(mostColorPlayable) > 0:
            return whatIsTheHighest(mostColorPlayable)
        elif len(specialValuesPlayable) > 0:
            return specialValuesPlayable[0]
        return highestValue

def ScoreConverter(givenCard:dict):
    if givenCard["Kleur"] == "Wild":
        return 50
    elif givenCard["Waarde"] == "Draw Two" or givenCard["Waarde"] == "Skip" or givenCard["Waarde"] == "Reverse":
        return 20
    else:
        valueCard = givenCard["Waarde"]
        return int(valueCard)

def isWinnerScore(playerScores):
    for z in range(len(playerScores)):
        if playerScores[z] >= 500:
            print(f"De winnaar is Speler {z + 1}!")
            return True
    return False

UnoDeck = deckBuilder()
random.shuffle(UnoDeck)

players = []

while True:
	inputHowManyPlayer = int(input("Vul het aantal spelers in: "))
	if inputHowManyPlayer < 2:
		print("Je hebt 2 spelers nodig om te spelen")
	else:
		break

for z in range(inputHowManyPlayer):
	PlayerCards = drawCards(3)
	players.append(PlayerCards)

playerScores = []
for z in range(inputHowManyPlayer):
    playerScores.append(0)

topCard = UnoDeck.pop(0)
LastPlayer = len(players)
CurrentPlayer = 0 
Reverse = False

while not isWinner(players) and not isWinnerScore(playerScores):
	if CurrentPlayer <= -1:
		CurrentPlayer = LastPlayer -1
	elif CurrentPlayer >= LastPlayer:
		CurrentPlayer = 0

	if topCard["Kleur"] == "Wild":
		if topCard == {'Kleur': 'Wild', 'Waarde': 'Draw Four'}:
			print(f"Er is een Wild Four gespeeld Speler {CurrentPlayer + 1} pakt 4 kaarten en slaat deze beurt over!")
			players[CurrentPlayer].extend(drawCards(4))
			if Reverse:
				CurrentPlayer -= 1
			else:
				CurrentPlayer += 1
			givenColor = mostColor(players[CurrentPlayer -2])
			print(f"Speler die de Wild Card speelt wilt {givenColor}")
			if givenColor == "Groen":
				topCard = {"Kleur":"Groen","Waarde":"Null"}
			elif givenColor == "Rood":
				topCard = {"Kleur":"Rood","Waarde":"Null"}
			elif givenColor == "Blauw":
				topCard = {"Kleur":"Blauw","Waarde":"Null"}
			elif givenColor == "Geel":
				topCard = {"Kleur":"Geel","Waarde":"Null"}
		else:
			print("Er is een Wild Kaart gespeeld")
			givenColor = mostColor(players[CurrentPlayer -1])
			print(f"Speler die de Wild Card speelt wilt {givenColor}")
			if givenColor == "Groen":
				topCard = {"Kleur":"Groen","Waarde":"Null"}
			elif givenColor == "Rood":
				topCard = {"Kleur":"Rood","Waarde":"Null"}
			elif givenColor == "Blauw":
				topCard = {"Kleur":"Blauw","Waarde":"Null"}
			elif givenColor == "Geel":
				topCard = {"Kleur":"Geel","Waarde":"Null"}
	elif topCard["Waarde"] == 'Reverse':
		print(f"Er is een reverse gespeeld het rondje draait om!")
		if len(players) == 2:
			if Reverse == True:
				Reverse = False
				CurrentPlayer += 1
			elif Reverse == False:
				Reverse = True
				CurrentPlayer -= 1			
		else:
			if Reverse == True:
				Reverse = False
				CurrentPlayer += 2
			elif Reverse == False:
				Reverse = True
				CurrentPlayer -= 2
	elif topCard["Waarde"] == "Skip":
		print(f"Er is een skip gespeeld Speler {CurrentPlayer + 1} slaat deze beurt over!")
		if Reverse:
			CurrentPlayer -= 1
		else:
			CurrentPlayer += 1
	elif topCard["Waarde"] == "Draw Two":
		print(f"Er is een Draw Two gespeeld Speler {CurrentPlayer + 1} pakt 2 kaarten en slaat deze beurt over!")
		players[CurrentPlayer].extend(drawCards(2))
		if Reverse:
			CurrentPlayer -= 1
		else:
			CurrentPlayer += 1

	if CurrentPlayer <= -1:
		CurrentPlayer = LastPlayer -1
	elif CurrentPlayer >= LastPlayer:
		CurrentPlayer = 0

	print(f"Speler {CurrentPlayer + 1} is aan de beurt.")
	print("De bovenste kaart is Kleur: ", str(topCard["Kleur"]) , "Waarde:", str(topCard["Waarde"]))
	while True:
		showHand(players[CurrentPlayer])
		if canPlay(topCard, players[CurrentPlayer]):
			playableCards = whatCanBePlayed(topCard,players[CurrentPlayer])
			playCard = whatMove(players[CurrentPlayer],topCard,playableCards)
			print(f"Speler {CurrentPlayer + 1} legt de kaart {playCard}")
			topCard = players[CurrentPlayer].pop(players[CurrentPlayer].index(playCard))
			CurrenScore = ScoreConverter(topCard)
			playerScores[CurrentPlayer] += CurrenScore
			break
		else:
			players[CurrentPlayer].extend(drawCards(1))

	answer = input("Wilt u dat het spel stopt [yes] or [no]?")
	if answer.lower == 'yes':
		break
	
	print("Scores zijn",playerScores)
	if Reverse:
		CurrentPlayer -= 1
	else:
		CurrentPlayer += 1
