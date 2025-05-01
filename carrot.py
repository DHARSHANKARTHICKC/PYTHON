import random

box1 = "Red box"
box2 = "Gold box"
p1 = input(">Enter player name 1 :")
p2 = input(">Enter player name 2 :")
playernames = p1.center(11)+'     '+p2.center(11)
while True:
    print()
    print("HERE ARE THE BOXES")
    print()


    print('''
|------|       |-------|
{}             {}             '''.format(box1,box2))
    print(playernames)

    n = random.randint(1,2)
    if n == 1:
        carrot = True
    elif n == 2:
        carrot = False

    print(p1," are you ready to see the box ")
    input()
    print(p2," close your eyes")
    input()

    if carrot:
        print('''
                www
            |------|       |-------|
            {}             {}  
            carrot!!                          '''.format(box1,box2))
        print(playernames)
    else:
        print('''
                            www
            |------|       |-------|
            {}             {}  
            No carrot!!                       '''.format(box1,box2))
        print(playernames)
    print(p2," open you eyes\n",p1+'give the choise to '+ p2)
    print("1.Carrot in the box\n2.Carrot not in the box")

    print(p2," would you like to swap the box")
    choise = input(">Enter your choise Y/N: ")
    if choise.upper().startswith('Y'):
        box1,box2 = box2,box1
        carrot = not carrot

    if carrot:
        print('''
              www
            |------|       |-------|
            {}             {}  
                                       '''.format(box1,box2))
        print(playernames)
    else:
        print('''
                              www
            |------|       |-------|
            {}             {}  
                                       '''.format(box1,box2))
        print(playernames)

    if carrot:
        print(p1,"won!!")
    else:
        print(p2,"won!!")