# bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie
# author: Patrik Oslizlok
# email: oslizlokpatrik@gmail.com
# discord: patasosel

import random
number = []
while len(number) < 4:
    x = str(random.randint(1,9))
    if x not in number:
        number.append(x)  
        
pokusy = []
oddelovac = "-" * 47

print(f"""Hi there!
{oddelovac}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{oddelovac}
Enter a number:
{oddelovac}""")

while True:
    bulls = 0
    cows = 0
    pokus = input(">>> ")
    if len(pokus) != 4 and pokus.isdigit():
        print("4 digits please!")
    elif len(pokus) != len(set(pokus)):
        print("No duplicates please!")
    elif not pokus.isdigit():
        print("Numbers only please!")
    elif pokus[0] == "0":
        print("Number cannot start with 0")
    else:
        pokusy.append(pokus)
        for i in range(len(pokus)):
            if pokus[i] == number[i]:
                bulls += 1
            elif pokus[i] in number:
                cows += 1
        if bulls == 1 and cows == 1:   
            print(f"""{bulls} bull, {cows} cow
{oddelovac}""")
        elif bulls == 1 and cows != 1:
            print(f"""{bulls} bull, {cows} cows
{oddelovac}""")
        elif bulls != 1 and cows == 1:
            print(f"""{bulls} bulls, {cows} cow
{oddelovac}""")
        elif bulls == 4 and len(pokusy) <= 4:
            print(f"""Correct, you've guessed the right number
in {len(pokusy)} guesses          
{oddelovac}""")
            break
        else:
            print(f"""{bulls} bulls, {cows} cows
{oddelovac}""")

if len(pokusy) <= 4:
    print("That's amazing")
elif 4 < len(pokusy) <= 10:
    print("That's average")
else:
    print("That's not so good")  
        
    
        
               