boodschappenLijste = {'wat':[], 'hoeveel':[]}

def listMaker():
    while True:
        wat = input('Wat wil je van de winkel (quit): ')
        if wat.lower() == 'quit':
            break
        if wat in boodschappenLijste['wat']:
            hoever = boodschappenLijste['wat'].index(wat)
            getal = boodschappenLijste['hoeveel'][hoever]
            getal = getal + 1
            print(getal)
            boodschappenLijste['hoeveel'][hoever] = getal

            return listMaker()
        boodschappenLijste['wat'].append(wat)
        hoeveel = int(input('Wat hoeveel wil je hier van: '))
        boodschappenLijste['hoeveel'].append(hoeveel)
    return boodschappenLijste

print(listMaker())

