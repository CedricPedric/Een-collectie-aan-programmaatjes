import random

Score =['',]*5
Dobbels = ['',]*5
resultaten = []


def text():
    TEXT = """
1: Dobbelsteen = {}
2: Dobbelsteen = {}
3: Dobbelsteen = {}
4: Dobbelsteen = {}
5: Dobbelsteen = {}
    """.format(Dobbels[0], Dobbels[1], Dobbels[2], Dobbels[3],Dobbels[4])
    return TEXT

def dobbel(begin=1,einde = 5):
    global Dobbels
    while begin <= einde:
        positie = begin - 1
        roll = random.randint(1,6)
        Dobbels[positie]= roll
        begin += 1

def reroll(getalRerolls:list):
    global Dobbels
    for x in (getalRerolls):
        positieVanKeuze = x -1
        roll = random.randint(1,6)
        Dobbels[positieVanKeuze] = roll

def YesOrNo(vraag = 'yes or no'):
    while True:
        antwoord = input(vraag)
        if antwoord == 'yes':
            return True
        elif antwoord == 'no':
            return False
        else:
            print("Invalid Option!")

def score(givenList):
    global hoevaak
    global Dobbels
    finalLowResult = 0
#Onder Berekening
    for x in range(1,7):
        y = x -1
        hoevaak.append(givenList.count(x))
        finalLowResult = finalLowResult + hoevaak[y]

    TEXT = """
Totaal aantal van 1: {0} 
Totaal aantal van 2: {1} 
Totaal aantal van 3: {2} 
Totaal aantal van 4: {3} 
Totaal aantal van 5: {4} 
Totaal aantal van 6: {5} 
Totaal alles opgeteld is: {6}
    """.format(hoevaak[0],hoevaak[1],hoevaak[2],hoevaak[3],hoevaak[4],hoevaak[5],finalLowResult)

#Boven Berekening
    finalTopResult = 0
    if 5 in hoevaak:
        bonus = "Yahtzee!"
        finalTopResult + 50
    elif 1 in Dobbels and 2 in Dobbels and 3 in Dobbels and 4 in Dobbels and 5 in Dobbels:
        finalTopResult + 30
        bonus = "Kleine Straat"
    elif 2 in Dobbels and 3 in Dobbels and 4 in Dobbels and 5 in Dobbels and 6 in Dobbels:
        finalTopResult + 40
        bonus = "Grote Straat"
    elif 4 in hoevaak:
        for x in range(0,5):
            y = x - 1
            if givenList[y] == givenList[x]: 
                finalTopResult = givenList[x] * 4
                break
        bonus = "Four of a kind!"
    elif 3 in hoevaak and 2 in hoevaak:
        finalTopResult = + 25
        bonus = "Full house!"
    elif 3 in hoevaak:
        bonus = "Three of a kind!"
        for x in range(0,5):
            y = x - 1
            if givenList[y] == givenList[x]: 
                finalTopResult = givenList[x] * 3
                break
    
#Alles optellen
    FinalResult = finalLowResult + finalTopResult
    print('-'*20)
    print(hoevaak)
    if finalTopResult > 0:
        print(bonus)
        print("U heeft een Bonus Score = " + str(finalTopResult))
    print(TEXT)
    print("Alles Opgeteld = ", str(FinalResult))
    print('-'*20)
    return FinalResult



# Begin Code
for game in range(1,6):
    if YesOrNo("Dit is ronde {} wilt u een een ronde spelen?: ".format(game)):
        dobbel()
        print(text())
        hoevaak = []
        for x in range(2):
            if YesOrNo("Wilt u rerollen?:"):
                rerolls = []
                while True:
                    inputReroll = int(input("Welke dobbelstenen moeten opnieuw gerolled worden? (0 is done): "))
                    if inputReroll != 0:
                        rerolls.append(inputReroll)
                    else:
                        break
                reroll(rerolls)
                print("New" + text())
            else:
                break
        ScoreRound = (score(Dobbels))
        positie = game - 1
        Score[positie] = ScoreRound
    else:
        print("Geen rondes meer")
        break

print("Uw eind scores zijn:", Score)


