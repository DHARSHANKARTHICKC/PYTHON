ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
blank =' '
X,O ='X','O'


def get():
    board = {}
    for i in ALL_SPACES:
        board[i] = blank
    return board

def string(board):
    print(''' 
{} | {} | {}      1 | 2 | 3
------------     -----------
{} | {} | {}      4 | 5 | 6
------------     -----------
{} | {} | {}      7 | 8 | 9       
          '''.format(board['1'],board['2'], board['3'],
                    board['4'], board['5'], board['6'],
                    board['7'], board['8'], board['9']))
    
def isempty(board,space):
    return space in ALL_SPACES and board[space] == blank

def full(board):
    for i in ALL_SPACES:
        if board[i] == blank:
            return False
    return True

def update(board,space,sign):
    board[space] = sign

def iswinner(board,player):
    b , p = board , player
    return ((b['1'] == b['2']==b['3']==p)or
            (b['4'] == b['5']==b['6']==p)or
            (b['7'] == b['8']==b['9']==p)or
            (b['1'] == b['4']==b['7']==p)or
            (b['2'] == b['5']== b['8']==p)or
            (b['3'] == b['6'] == b['9']==p)or
            (b['1'] == b['5'] == b['9']== p)or
            (b['3'] == b['5'] == b['7']==p))

game =get()

p1,p2 = X,O
while True:
    print(string(game))
    move = ''
    while not isempty(game,move):
        move = input("ENTER POS:")
    update(game,move,p1)

    if full(game):
        print(string(game))
        print("tie!")
        break
    if iswinner(game,p1):
        print(string(game))
        print(p1,' won')
        break

    p1,p2 = p2,p1
    

