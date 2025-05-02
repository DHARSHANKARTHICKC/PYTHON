b = 0
l = 1


while True:
    num = input("enter the no :")
    if not num.isdecimal():
        continue
    elif int(num) <= 0:
        continue
    else:
        break


if num == '1':
    print(b)
elif num == '2':
    print(b,',',l)
else:
    print(b,',',l,end ='')
    for i in range(int(num) - 2):
        next = l + b
        print(',',next,end='')

        b = l 
        l = next
