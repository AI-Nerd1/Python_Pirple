Favorite_List = []
Leftovers = []

def pushLeftover(songs):
    Leftovers.append(songs);

def Song_Push(songs):

    try:
        Favorite_List.index(songs)
        pushLeftover(songs)
        return False
    except:
        Favorite_List.append(songs)
        return True

Song_Push("Not Afraid")
Song_Push("Coming Home")
Song_Push("Monsters")
print(Favorite_List)
Song_Push("Venom")
Song_Push("Cheers")
print(Favorite_List)
print(Leftovers)