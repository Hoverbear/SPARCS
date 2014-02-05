def draw_board(board):
    """
    Accepts a list of lists which makes up the board.
    Assumes the board is a list of rows. (See my_board)
    """
    # Draw the column indexes.
    print("    ", end="")
    for index, col in enumerate(board):
        # Print the index of each column.
        # Note: sep="", end="" prevent python from creating a new line.
        print("  C" + str(index) + " ", sep="", end="")
    print("") # Creates a line break.
    for index, row in enumerate(board):
        # Print the row border.
        print("    " + ("+----" * 8) + "+", sep="")
        # Print the row index.
        print("R" + str(index) + "  ", sep="", end="")
        # Print each cell
        for cell in row:
            print("| " + str(cell) + " ", sep="", end="")
        print("|") # Finishes the row.
    # Print the end border.
    print("    " + ("+----" * 8) + "+", sep="")
            
my_board = [
    ["br", "bk", "bb", "bq", "bk", "bb", "bk", "br"],
    ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
    ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
    ["wr", "wk", "wb", "wq", "wk", "wb", "wk", "wr"]
]

draw_board(my_board)