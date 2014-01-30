#A simple chess game

def draw(b):
    print("-----------------")
    print(" A  B  C  D  E  F  G  H")
    c = 0
    for i in b:
        for j in i:
            print(" "+j+" ",end=''),
        print(" "+str(c+1))
        c+=1
    print("-----------------")

   
def setup_board(b):
    b[0][0] = 'R'
    b[0][1] = 'N'
    b[0][2] = 'B'
    b[0][3] = 'Q'
    b[0][4] = 'K'
    b[0][5] = 'B'
    b[0][6] = 'N'
    b[0][7] = 'R'
    b[1][0] = 'P'
    b[1][1] = 'P'
    b[1][2] = 'P'
    b[1][3] = 'P'
    b[1][4] = 'P'
    b[1][5] = 'P'
    b[1][6] = 'P'
    b[1][7] = 'P'

    b[7][0] = 'r'
    b[7][1] = 'n'
    b[7][2] = 'b'
    b[7][3] = 'q'
    b[7][4] = 'k'
    b[7][5] = 'b'
    b[7][6] = 'n'
    b[7][7] = 'r'
    b[6][0] = 'p'
    b[6][1] = 'p'
    b[6][2] = 'p'
    b[6][3] = 'p'
    b[6][4] = 'p'
    b[6][5] = 'p'
    b[6][6] = 'p'
    b[6][7] = 'p'

    return b

def move(i, f, b):
    init = (ord(i[0])-97,int(i[1]))
    fin = (ord(f[0])-97,int(f[1]))

    print(init)
    print(fin)
    sym = b[init[0]][init[1]] 
    b[init[0]][init[1]] = '_'
    b[fin[0]][fin[1]] = sym

    return b

def main():
    board = [["_"]*8, ["_"]*8, ["_"]*8, ["_"]*8, ["_"]*8, ["_"]*8, ["_"]*8, ["_"]*8]
    board = setup_board(board)
    draw(board)
    while(True):
        print("Enter the location of the piece to move ('a8' or 'b7')")
        resp1 = input(">>> ")
        print("Enter the location to move the piece ('a7' or 'b5'")
        resp2 = input(">>> ")
        move(resp1, resp2, board)

main()
