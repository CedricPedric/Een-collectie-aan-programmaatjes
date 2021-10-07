import random


FinalUpperScores = [" "]*6
FinalLowerScores = [1,2,3,4,5,6,7]
rolledDice = ['']*5
FilledInUpper = []
FilledInLower = []

TextOptiesLower ="""Hey de opties die je hebt om te intevullen onderin zijn!
Three of a Kind! = 1
Four of a Kind! = 2
Full House = 3
Kleine Straat = 4
Grote Straat = 5
Yahtzee = 6
Chance = 7"""

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
#Functie om de Bovenste Helft te berekenen
def upperHalfScore(givenList:list):
    #Checkt hoeveel van elk getal in de list staat en stopt dat in een list
    howManyDigits = []
    for digit in range(1,7):
        howManyDigits.append(givenList.count(digit))
    #Berekent de resultaten van bovenste helft
    listUpperHalf = []
    for z in range(0,6):
        x = howManyDigits[z] * (z + 1)
        listUpperHalf.append(x)
    #De Tekst zodat om de resultaten te zien
    TextBovensteHelft = """
Totaal resultaten van allen 1's: {0} 
Totaal resultaten van allen 2's: {1} 
Totaal resultaten van allen 3's: {2} 
Totaal resultaten van allen 4's: {3} 
Totaal resultaten van allen 5's: {4} 
Totaal resultaten van allen 6's: {5} 
    """.format(listUpperHalf[0],listUpperHalf[1],listUpperHalf[2],listUpperHalf[3],listUpperHalf[4],listUpperHalf[5])

    return listUpperHalf,TextBovensteHelft

#Functie om de Onderste Helft te berekenen
def lowerHalfScore(givenList:list):
    #Checkt hoeveel van elk getal in de list staat en stopt dat in een list
    howManyDigits = []
    for digit in range(1,7):
        howManyDigits.append(givenList.count(digit))
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
        bonus = "Full House"
        bonusPoints = 25
    elif 3 in howManyDigits:
        bonus = "Three of a Kind"
        for positie in range(0,5):
            bonusPoints += givenList[positie]

    return bonus,bonusPoints

#Functie om te kiezen wat je van de bovenste helft wilt behouden
def FillUpper():
    global FilledInUpper
    global resultUpperHalf
    global FinalUpperScores
    while True:
        inputKeep = int(input("Welk getal wil je houden?:"))
        if inputKeep == 1:
            if 1 in FilledInUpper:
                print("U heeft deze al ingevuld!")
            else:
                FinalUpperScores[0] = resultUpperHalf[0]
                FilledInUpper.append(inputKeep)
                break
        elif inputKeep == 2:
            if 2 in FilledInUpper:
                print("U heeft deze al ingevuld!")
            else:
                FinalUpperScores[1] = resultUpperHalf[1]
                FilledInUpper.append(inputKeep)
                break                
        elif inputKeep == 3:
            if 3 in FilledInUpper:
                print("U heeft deze al ingevuld!")
            else:
                FinalUpperScores[2] = resultUpperHalf[2]
                FilledInUpper.append(inputKeep)
                break
        if inputKeep == 4:
            if 4 in FilledInUpper:
                print("U heeft deze al ingevuld!")
            else:
                FinalUpperScores[3] = resultUpperHalf[3]
                FilledInUpper.append(inputKeep)
                break
        if inputKeep == 5:
            if 5 in FilledInUpper:
                print("U heeft deze al ingevuld!")
            else:
                FinalUpperScores[4] = resultUpperHalf[4]
                FilledInUpper.append(inputKeep)
                break
        if inputKeep == 6:
            if 6 in FilledInUpper:
                print("U heeft deze al ingevuld!")
            else:
                FinalUpperScores[5] = resultUpperHalf[5]
                FilledInUpper.append(inputKeep)
                break

#Functie om te kiezen wat je van de ondeste helft wilt behouden
def FillLower():
    global resultLowerHalf
    global FilledInLower
    global AmountLowerHalf
    global FinalLowerScores
    global TextOptiesLower
    global rolledDice

    print(TextOptiesLower)
    while True:
        inputKeepLower = int(input("Welke bonus wilt u invullen?"))
        if inputKeepLower == 1:
            chosenBonus = "Three of a Kind"
            if 1 in FilledInLower:
                print("Deze is al eeder toegevoed!")
            else:
                if chosenBonus == resultLowerHalf:
                    FinalLowerScores[0] = AmountLowerHalf
                    FilledInLower.append(1)
                    break
                else:
                    FinalLowerScores[0] = 0
                    FilledInLower.append(1)
                    break
        elif inputKeepLower == 2:
            chosenBonus = "Four of a Kind"
            if 2 in FilledInLower:
                print("Deze is al eeder toegevoed!")
            else:
                if chosenBonus == resultLowerHalf:
                    FinalLowerScores[1] = AmountLowerHalf
                    FilledInLower.append(2)
                    break
                else:
                    FinalLowerScores[1] = 0
                    FilledInLower.append(2)
                    break
        elif inputKeepLower == 3:
            chosenBonus = "Full House"
            if 3 in FilledInLower:
                print("Deze is al eeder toegevoed!")
            else:
                if chosenBonus == resultLowerHalf:
                    FinalLowerScores[2] = AmountLowerHalf
                    FilledInLower.append(3)
                    break
                else:
                    FinalLowerScores[2] = 0
                    FilledInLower.append(3)
                    break
        elif inputKeepLower == 4:
            chosenBonus = "Kleine Straat"
            if 4 in FilledInLower:
                print("Deze is al eeder toegevoed!")
            else:
                if chosenBonus == resultLowerHalf:
                    FinalLowerScores[3] = AmountLowerHalf
                    FilledInLower.append(4)
                    break
                else:
                    FinalLowerScores[3] = 0
                    FilledInLower.append(4)
                    break
        elif inputKeepLower == 5:
            chosenBonus = "Grote Straat"
            if 5 in FilledInLower:
                print("Deze is al eeder toegevoed!")
            else:
                if chosenBonus == resultLowerHalf:
                    FinalLowerScores[4] = AmountLowerHalf
                    FilledInLower.append(5)
                    break
                else:
                    FinalLowerScores[4] = 0
                    FilledInLower.append(5)
                    break
        elif inputKeepLower == 5:
            chosenBonus = "Grote Straat"
            if 5 in FilledInLower:
                print("Deze is al eeder toegevoed!")
            else:
                if chosenBonus == resultLowerHalf:
                    FinalLowerScores[4] = AmountLowerHalf
                    FilledInLower.append(5)
                    break
                else:
                    FinalLowerScores[4] = 0
                    FilledInLower.append(5)
                    break
        elif inputKeepLower == 6:
            chosenBonus = "Yahtzee!"
            if 6 in FilledInLower:
                print("Deze is al eeder toegevoed!")
            else:
                if chosenBonus == resultLowerHalf:
                    FinalLowerScores[5] = AmountLowerHalf
                    FilledInLower.append(6)
                    break
                else:
                    FinalLowerScores[5] = 0
                    FilledInLower.append(6)
                    break
        elif inputKeepLower == 7:
            chance = 0
            chosenBonus = "Chance!"
            if 7 in FilledInLower:
                print("Deze is al eeder toegevoed!")
            else:
                for positie in range(0,5):
                    chance += rolledDice[positie]
                FinalLowerScores[6] = chance
                FilledInLower.append(7)
                break

        elif inputKeepLower == 10:
            break
        else:
            print("Als je hier geen opties kan maken had je het niet moeten kiezen lol geen zorgen vul 10 in dan stopt het")

#De functie om het scorenboard te maken

def ScoreBoard():
    global FinalUpperScores
    global FinalLowerScores
    #Maakt/Berekent de bovenste helft en text
    UpperScores =  []
    UpperScores += FinalUpperScores
    for z  in range (len(UpperScores)):
        z -=1
        if UpperScores[z] == " ":
            UpperScores[z] = 0  
    TotalUpper = 0
    ExtraBonus = 0
    for z in range(0,6):
        TotalUpper += UpperScores[z]
    if TotalUpper >= 63:
        ExtraBonus = 35
    
    SubTotalUpper = TotalUpper + ExtraBonus
    BovensteHelftText = """
---------------------------------------------
ENEN                  |{0} 
TWEEËN                |{1} 
DRIEËN                |{2} 
VIEREN                |{3} 
VIJFEN                |{4} 
ZESSEN                |{5} 
TOTAAL                |{6} 
EXTRA BONUS           |{7} 
TOTAAL BOVENSTE HELFT |{8} 
(Als het totaal 63 is krijg je 35 punten)
---------------------------------------------""".format(FinalUpperScores[0], FinalUpperScores[1],FinalUpperScores[2], FinalUpperScores[3],FinalUpperScores[4], FinalUpperScores[5], TotalUpper,ExtraBonus,SubTotalUpper)
    #Maakt/Berekent de onderste helft en text
    LowerScores = []
    LowerScores += FinalLowerScores
    for z in range(len(LowerScores)):
        z -= 1
        if LowerScores[z] == " ":
            LowerScores[z] = 0
    TotalLower = 0
    for z in range(0,6):
        TotalLower += LowerScores[z]

    OndersteHelftText = """Three of a Kind     |{0}
Four of a Kind      |{1}
Full House          |{2}
Kleine Straat       |{3}
Groote Straat       |{4}
Yahtzee             |{5}
Chance              |{6}
---------------------------------------------""".format(FinalLowerScores[0], FinalLowerScores[1], FinalLowerScores[2], FinalLowerScores[3], FinalLowerScores[4],FinalLowerScores[5],FinalLowerScores[6])
    #Berekent Subtotal en maakt Text
    SubTotal = TotalLower + SubTotalUpper
    SubTotalText = """TOTAL UPPER = {}
TOTAL LOWER = {}
---------------------------------------------
SUBTOTAL = {}""".format(SubTotalUpper, TotalLower, SubTotal)
    #Output van de gemaakte Texten
    print(BovensteHelftText)
    print(OndersteHelftText)
    print(SubTotalText)






#Hier is de start van de Game


rondes = 0
while " " in FinalUpperScores or " " in FinalLowerScores:
    rondes += 1
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

        resultUpperHalf, TextUpperHalf = upperHalfScore(rolledDice)
        resultLowerHalf, AmountLowerHalf = lowerHalfScore(rolledDice)

        inputUpperOrLower = input("Wilt u iets toevoegen aan de bovenste of ondeste helft?|upper or lower|: ")
        if inputUpperOrLower.lower() == 'upper':
            FillUpper()
        elif inputUpperOrLower.lower() == 'lower':
            if resultLowerHalf != "":
                print("je hebt een bonus! " + resultLowerHalf)
            else:
                print("je hebt geen bonus")
            FillLower()
                
        print(FinalUpperScores)
        print(FinalLowerScores)
    else:
        break

ScoreBoard()