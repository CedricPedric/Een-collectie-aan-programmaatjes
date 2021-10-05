import random

scores = [''] *3
rolledDice = ['']*5
#Function voor dobbelstenen rerollen
def reroll(givenRerolls:list):
    global rolledDice
    for x in (givenRerolls):
        position = x -1
        roll = random.randint(1,6)
        rolledDice[position] = roll
#Functon voor de dobbelstenen rollen
def rollDice(begin=1,end = 5):
    global rolledDice
    while begin <= end:
        position = begin - 1
        roll = random.randint(1,6)
        rolledDice[position]= roll
        begin += 1
#Function voor de text/resultaten van de dobbelstenen
def text():
    TEXT = """
1: Dobbelsteen = {}
2: Dobbelsteen = {}
3: Dobbelsteen = {}
4: Dobbelsteen = {}
5: Dobbelsteen = {}
""".format(rolledDice[0], rolledDice[1], rolledDice[2], rolledDice[3],rolledDice[4])
    return TEXT
#Simple Yes or No functie
def YesOrNo(vraag = 'yes or no'):
    while True:
        antwoord = input(vraag)
        if antwoord == 'yes':
            return True
        elif antwoord == 'no':
            return False
        else:
            print("Invalid Option!")
#Funcite om de score te berkenen van het gegooide dobbelstenen
def score(givenList:list):
    #Checkt hoeveel van elk getal in de list staat en stopt dat in een list
    howManyDigits = []
    for digit in range(1,7):
        howManyDigits.append(givenList.count(digit))
    #Berekent de resultaten van bovenste helft
    listUpperHalf = []
    resultsUpperHalf = 0
    for z in range(0,6):
        x = howManyDigits[z] * (z + 1)
        listUpperHalf.append(x)
    for z in range(0,5):
        resultsUpperHalf += givenList[z]
    #Berekent de resultaten van de onderste helft/Bonus Points
    bonusPoints = 0
    bonus = ""
    if 5 in howManyDigits:
        bonus = "Yahtzee!"
        bonusPoints = 50
    elif (1 in givenList and 2 in givenList and 3 in givenList and 4 in givenList and 5 in givenList) or (2 in givenList and 3 in givenList and 4 in givenList and 5 in givenList and 6 in givenList):
        bonus = "Grote Straat"
        bonusPoints = 40
    elif (1 in givenList and 2 in givenList and 3 in givenList and 4 in givenList) or (2 in givenList and 3 in givenList and 4 in givenList and 5 in givenList) or (3 in givenList and 4 in givenList and 5 in givenList and 6 in givenList):
        bonus = "Kleine Straat"
        bonusPoints = 30
    elif 4 in howManyDigits:
        bonus = "Four of a Kind"
        for positie in range(0,5):
            bonusPoints += givenList[positie]
    elif 3 in howManyDigits and 2 in howManyDigits:
        bonus = "Full House!"
        bonusPoints = 25
    elif 3 in howManyDigits:
        bonus = "Three of a Kind"
        for positie in range(0,5):
            bonusPoints += givenList[positie]
    #Bereken resultaten
    subTotal = bonusPoints + resultsUpperHalf
    #Maakt en format de texten
    TextBovensteHelft = """
Totaal resultaten van allen 1's: {0} 
Totaal resultaten van allen 2's: {1} 
Totaal resultaten van allen 3's: {2} 
Totaal resultaten van allen 4's: {3} 
Totaal resultaten van allen 5's: {4} 
Totaal resultaten van allen 6's: {5} 
Totaal resultaten opgeteld is: {6}
""".format(listUpperHalf[0],listUpperHalf[1],listUpperHalf[2],listUpperHalf[3],listUpperHalf[4],listUpperHalf[5],resultsUpperHalf)

    TextOndersteHelft = """U heeft: {}
Je extra punten zijn: {}
""".format(bonus,bonusPoints)

    #Prints naar de terminal
    print('-'*40)
    print(TextBovensteHelft)
    if bonusPoints > 0:
        print(TextOndersteHelft)
    print("Het subtotaal is:", str(subTotal))         
    print('-'*40)
    #Als laaste wordt het subtotaal terug gegeven
    return subTotal

#De code voor de game
for rondes in range(1,4):
    if YesOrNo('Dit is ronde ' + str(rondes) +' wil je een nog een ronde?:'):
        rollDice()
        print(text())
        for x in range(2):
            listRerolls = [] #Geeft hier aan dat de list leeg is zodat de oude rerolls niet worden gebruikt
            if YesOrNo("Wilt u dobbelstenen rerollen?: "):
                while True:
                    inputReroll = int(input("Welke dobbelstenen moeten opnieuw gerolled worden? (0 is done): "))
                    if inputReroll != 0:
                        listRerolls.append(inputReroll)
                    else:
                        break
                reroll(listRerolls)
                print("Rerolled Dice" + text())
        ScoreThisRound = score(rolledDice)
        postion = rondes - 1
        scores[postion] = ScoreThisRound
    else:
        break
#De prints voor de finalscore
print("""Score Round 1: {}
Score Round 2: {}
Score Round 3: {}
""".format(scores[0],scores[1],scores[2]))

