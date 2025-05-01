b = 0
l = 1

num = input("enter the no :")

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