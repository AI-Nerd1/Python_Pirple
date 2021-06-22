a = 10*5
b = 2*(2/4)*a
x = ((a*2)/b)*(b/2)
c = x


def equality(a, b, c):
    ab = False
    ac = False
    bc = False
    if a == b:
        ab = True

    if a == c:
        ac = True

    if b == c:
        bc = True

    if(ab == True and ac == True
        or ab == True and bc == True
        or bc == True and ac == True
       ):
        print('True')
    else:
        print('False')


equality(a, b, c)





