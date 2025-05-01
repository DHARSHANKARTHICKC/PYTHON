import time,random

print("WELCOME")
while True:
    print("Wait!!")
    time.sleep(random.randint(30,50)/10)
    print("press")
    timepressed = time.time()
    input()
    timeelapssed = time.time() - timepressed

    if timeelapssed < 0.01:
        print("pressed before time")
    elif timeelapssed > 0.3:
        print("too slow ",timeelapssed) 
    else:
        print("you won!! ",timeelapssed)

    res = input("q to quit :")
    if res.lower() == 'q':
        break
    else:
        continue

