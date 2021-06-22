# =======================================================================
#                       Assignment on Lists
#  ========================================================================
My_unique_list = []
My_leftovers = []


def leftover(x):
    My_leftovers.append(x)
    return False


def addition(x):
    if x not in My_unique_list:
        My_unique_list.append(x)
        return True

    else:
        leftover(x)

        print(My_unique_list)
        print(My_leftovers)


addition(67)
addition(5)
addition(10)
addition(7)
addition(24)
addition(6)
addition(10)






