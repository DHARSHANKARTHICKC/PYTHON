
while True:
    num = input("Enter the number to find the factors :")
    if not num.isdecimal():
        continue
    elif int(num) < 0:
        continue
    else:
        num = int(num)
        break

factors = []
for i in range(1,num+1):
    if num % i ==0:
        factors.append(i)
    else:
        continue

for i,factor in enumerate(factors):
    if i != 0:
        print(",",end='')
    print(factor,end='')
