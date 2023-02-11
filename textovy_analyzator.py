# textovy_analyzator.py: první projekt do Engeto Online Python Akademie
# author: Patrik Oslizlok
# email: oslizlokpatrik@gmail.com
# discord: patasosel
users = {"bob":"123", "ann":"pass123", "mike":"password123", "liz":"pass123"}
rozdelovac = ("-"*40)
title_words = 0
upper_words = 0
lower_words = 0
digits = 0
digits_sum = 0
word_lenght = {}
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
user = input("username: ")
password = input("password: ")
if user in users and users[user] == password:
    print(f"""{rozdelovac}
Welcome to the app,{user} 
We have 3 texts to be analyzed.
{rozdelovac}""")
    user_input = input("Enter a number btw. 1 and 3 to select: ")
    print(rozdelovac)
    if user_input.isdigit() == False:
        print("Digits only. Quit...")
        quit()
    elif int(user_input)<1 or int(user_input)>3:
        print("Only 1 to 3 to select. Quit...")
        quit()
    else:
        total_words = len(TEXTS[int(user_input)-1].split())
        for word in (TEXTS[int(user_input)-1].split()):
            if word.istitle():
                title_words += 1
            elif word.isupper():
                upper_words += 1
            elif word.islower():
                lower_words += 1
            elif word.isdigit():
                digits += 1
                digits_sum += int(word)
                    
        print(f"""There are {total_words} words in the selected text.
There are {title_words} titlecase words.
There are {upper_words} uppercase words.
There are {lower_words} lowercase words. 
There are {digits} numeric strings.
The sum of all the numbers {digits_sum}
{rozdelovac}""")
        print("LEN|  OCCURENCES  |NR.")
        print(rozdelovac)
        for word1 in (TEXTS[int(user_input)-1].split()):
            if len(word1.strip(",.")) not in word_lenght:
                    word_lenght[len(word1)] = 1
            elif len(word1.strip(",.")) in word_lenght:
                    word_lenght[len(word1.strip(",."))] = word_lenght[len(word1.strip(",."))] + 1
        for pismen, pocet in sorted(word_lenght.items()):
            hvezda = "*"*pocet
            print(f"{pismen:>3}|{hvezda}|{pocet}")
else:
    print("unregistered user, terminating the program..")
    quit()
                
                

        
        