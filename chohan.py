import random
POT = 5000

while True:
    while True:
        bet = input(">Enter the bet amount :")
        if not bet.isdecimal():
            continue
        elif int(bet) > POT:
            continue
        else:
            bet = int(bet)
            break

    while True:
        choise = input(">Enter Your Choise :")
        choise = choise.lower()
        if(choise.startswith('c')):
            choise = 'cho'
            break
        elif(choise.startswith('h')):
            choise = 'han'
            break
        else:
            continue

    d1 = random.randint(1,6)
    d2 = random.randint(1,6)

    if (d1+d2) % 2 == 0:
        correct = 'cho'
    else:
        correct = 'han'

    if choise == correct:
        print("You Won Rs.",bet)
        print("The dice were",d1,' ',d2)
        POT = POT + bet
    else:
        print("You Lost Rs.",bet)
        print("The dice were",d1,' ',d2)
        POT = POT - bet

    if POT <= 0:
        print("No pot amount")
        break
    
    res = input(">Enter the choise")

    if res.lower() == 'q':
        break
    else:
        continue

