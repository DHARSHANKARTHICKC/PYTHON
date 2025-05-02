while True:
    while True:
        num = input("> Enter a number :")
        if num.isdecimal():
            num = int(num)
            break
        elif int(num) < 0:
            continue
        else:
            continue

    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = num*3+1
        
        print(num,',',end ="")

    res = input(">Enter q to quit")
    if res.lower()=='q':
        break
    else:
        continue
