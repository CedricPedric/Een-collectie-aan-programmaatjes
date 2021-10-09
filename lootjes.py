import random
from typing import List

ListNames = []
OGLM = []
while True:
    naam = input('Vul je naam in (Q if done): ')
    if naam in ListNames:
        print('Deze naam is al opgegeven')
    elif naam != 'Q':
        ListNames.append(naam)
    else:
        break

aantal = len(ListNames)
aantal = aantal - 1

OGLM = OGLM + ListNames
random.shuffle(ListNames)


while aantal > 0:
    if OGLM[aantal] == ListNames[aantal]:
        random.shuffle(ListNames)
        aantal = len(ListNames)
        aantal = aantal -1
    else:
        aantal = aantal - 1


newaantal = len(ListNames) 
printAantal = len(ListNames) -1

for x in range(newaantal):
    print((OGLM[printAantal]) + ' Heef lootje ' + (ListNames[printAantal]) )
    printAantal = printAantal - 1
