Length = 10
tab = '0'
result = 1
x = 1
y = 1
row = 19
column = 20

if column > 160 or row != column - 1 or column % 10 != 0:
    print("False")
    print("Conditions: 1. The number of columns must be < or = 160.")
    print("            2. The number of rows must be 1 less than the number of columns")
    print("            3. The number of columns must be a multiple of 10 to obtain a standard table ")

else:
    for x in range(row):
        if x % 2 == 0:
            for y in range(column):
                if y % 2 == 1:
                    if y != row:
                        print(" ", end="")
                    else:
                        print(" ")
                else:
                    print('|', end="")
        else:
            print('=' * row)
print("True")
