import random
def leet(mes):
    charmap = {'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'],'f': ['ph'], 'h': [']-[', '|-|'], 'i': ['1', '!', '|'], 'k': [']<'],'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'],'v': ['\\/']}
    leets = ''
    for char in mes :
        if char.lower() in charmap and random.random() <= 0.70:
            replace = charmap[char.lower()]
            leetreplace = random.choice(replace)
            leets = leets + leetreplace 
        else:
            leets  = leets + char

    return leets


mes =  input("enter the message :")
l = leet(mes)
print(l)