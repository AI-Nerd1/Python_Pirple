# print(u'\u2B24')

def table(plat):
    for rows in range(14):
        if rows % 2 == 0:
            prac_row = int(rows/2)
            for columns in range(13):
                if columns % 2 == 0:
                    prac_column = int(columns/2)
                    if columns != 12:
                        print(plat[prac_column][prac_row], end="")
                    else:
                        print(plat[prac_column][prac_row])
                else:
                    print("|", end="")
            else:
                print("-------------")


player = 1
field = [[" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "],
         [" ", " ", " ", " ", " ", " ", " "]]
# print(field)
table(field)
while True:
    print("Player ", player, "'s turn to play ")
    row = int(input("Enter row number: "))-1
    column = int(input("Enter column number: "))-1
    if player == 1:
        if field[row][column] == " ":
            field[row][column] = u'\u2B24'
            player = 2
    else:
        if field[row][column] == " ":
            field[row][column] = 'X'
            player = 1
    table(field)


