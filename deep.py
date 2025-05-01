import random,time
LEFT = 30
GAP = 30
WIDTH = 70
while True:
    RIGHT = WIDTH - LEFT - GAP
    time.sleep(0.1)
    print("#"*LEFT +' '*GAP+"#"*RIGHT)

    num = random.randint(1,6)
    if num == 1 and LEFT > 0:
        LEFT = LEFT - 1
    elif num == 2 and LEFT + GAP < WIDTH -1:
        LEFT = LEFT + 1
    else:
        continue
    

