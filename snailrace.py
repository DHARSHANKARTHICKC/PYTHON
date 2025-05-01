import time,random,sys
MAXLENGTH = 20
MAXSNAILS = 8
FINISH = 20
while True:
    snails = input("enter the no of snails")
    snailname =[]
    for i in range(int(snails)):
        name = input("enter the name :")
        snailname.append(name)


    print("START",' '*(FINISH-len('start')),"FINISH")
    print("|"," "*(FINISH -len('|')),'|')

    snailprogress ={}

    for i in range(int(snails)):
        print(snailname[i])
        print('@v')
        snailprogress[snailname[i]] = 0

    while True:
        for i in range(random.randint(1,int(snails)//2)):
            s = random.choice(snailname)
            snailprogress[s] += 1
            
            if snailprogress[s] == FINISH:
                print(s,' won')
                sys.exit()
        time.sleep(0.2)
        print("\n"*50)
        print("START",' '*(FINISH-len('start')),"FINISH")
        print("|"," "*(FINISH -len('|')),'|')
        for i in snailname:
            spaces = snailprogress[i]
            print(" "*spaces,i)
            print("."*spaces,'@v')
        

