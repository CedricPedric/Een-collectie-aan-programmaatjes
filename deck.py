import random

deck = ['harten 2', 'harten 3', 'harten 4','harten 5','harten 6','harten 7', 'harten 8','harten 9','harten 10', 'harten vrouw' ,'harten heer','harten boer','harten aas',
'klaveren 2', 'klaveren 3', 'klaveren 4', 'klaveren 5', 'klaveren 6', 'klaveren 7', 'klaveren 8','klaveren 9','klaveren 10', 'klaveren vrouw', 'klaveren heer', 'klaveren boer', 'klaveren aas',
'schoppen 2', 'schoppen 3', 'schoppen 4', 'schoppen 5', 'schoppen 6', 'schoppen 7', 'schoppen 8', 'schoppen 9', 'schoppen 10', 'schoppen vrouw', 'schoppen heer', 'schoppen boer', 'schoppen aas', 
'ruiten 2', 'ruiten 3', 'ruiten 4', 'ruiten 5', 'ruiten 6', 'ruiten 7', 'ruiten 8' , 'ruiten 9', 'ruiten 10', 'ruiten vrouw', 'ruiten heer', 'ruiten boer', 'ruiten aas',
'joker', 'joker']

random.shuffle(deck)
print(deck[0:7])
for x in range(0, 7):
    deck.pop(x)

print(str(len(deck))+ str(deck))