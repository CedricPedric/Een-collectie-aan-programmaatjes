import random

listLenght = 24
while True:
    letter_upper_lenght = random.randrange(2,6)
    letter_lower_lenght = random.randrange(8,15)
    special_length = 3
    digits_lenght = random.randrange(4,7)
    
    total = letter_upper_lenght + letter_lower_lenght + special_length + digits_lenght
    
    if total == listLenght:
        break

password = []

special_characters = ['@', '#', '$', '%', '&', '_', '?']
digits = ['0','1','2','3','4','5' , '6', '7' ,'8','9']
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(letter_upper_lenght):
    random_upper = random.choice(letters)
    password.append(random_upper)

for i in range(letter_lower_lenght):
    random_lower = random.choice(letters)
    random_lower = random_lower.lower()
    password.append(random_lower)

for i in range(special_length):
    random_special = random.choice(special_characters)
    password.append(random_special)

for i in range(digits_lenght):
    random_digit = random.choice(digits)
    password.append(random_digit)


while True:
    random.shuffle(password)
    if password[0] in special_characters or password[24] in special_characters:
        print()
    if password[0] in digits or password[1] in digits or password [2] in digits:
        print()
    else:
        print("".join(password))
        break
    


