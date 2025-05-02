SYMBOLS =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while True:
    print("enter encrypt or decrypt")
    while True:
        mode = input("Select E/D :")
        if mode.lower().startswith('e'):
            mode = 'encrypt'
            break
        elif mode.lower().startswith('d'):
            mode ='decrypt'
            break
        else:
            print("enter valid choise")
            continue


    print("select a number between 1 to ",len(SYMBOLS))
    while True:
        key = input(">Enter a num :")
        if key.isdecimal():
            key = int(key)
            break
        elif key > 0 and key <len(SYMBOLS):
            key = int(key)
            break
        else:
            print("enter a valid number")
            continue

    message = input(">Enter the message to encrypt or decrypt :")

    for char in message:
        if char.upper() in SYMBOLS:
            char = char.upper()
            num = SYMBOLS.index(char)
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key   

            if num < 0:
                num = num + len(SYMBOLS)
            elif num > len(SYMBOLS)+1:
                num = num - len(SYMBOLS)

            print(SYMBOLS[num],end = '')
        else:
            print(char,end='')

    res = input(">press q to quit")
    if res.lower() == 'q':
        break
    else:
        continue
