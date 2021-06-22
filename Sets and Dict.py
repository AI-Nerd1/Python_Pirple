Title = "Title"
Released = "Date of release"
Artist = 'Artist'
Musician = 'Eminem'
Album = 'Album'
Genre = 'Genre'
Award = 'Award'
Length = 'Duration'
Writers = 'Writers'
Producer = 'Producer'
Studio = 'Studio'


Fav_music = {
    Title: "Not Afraid",
    Released: 'April 29 2010',
    Artist: 'Eminem',
    Album: 'Recovery',
    Genre: 'Hip-Hop',
    Award: 'MTV Video Music Award for Best Hip-Hop Video.',
    Length: '4:10',
    Producer: 'Boi-1da',
    Writers: 'Marshall Mathers, Jordan Evans.',
    Studio: 'Effigy Studio, Michigan.'
    }
print(Fav_music)
guess = 1


def guess_again():
    guess = str(input('Type the key you wanna guess:  \n'))


def try_again():
    choice = str(input("Try again, YES or NO?\n"))
    if choice == 'Yes' or choice == 'yes' or choice == 'YES':
        guess_again()
    if choice == 'NO' or chioce == 'No' or choice == 'no':
        print('You can always try again later, Good bye ')
        print(exit)
        exit()


guess_again()
if guess == 'Title' or 'title':
    Title_guess = str(input("What is my favorite music: \n"))
    if Title_guess == 'Not Afraid' or 'not afraid':
        print('Correct!!')
        try_again()
    else:
        print("Nice try!!, Not correct")
        try_again()

guess_again()
if guess == 'Release year' or 'Release Year':
    date_guess = int(input("What is the Release year of my favorite music: \n"))
    if date_guess == 2010:
        print('Correct!!')
        try_again()
    else:
        print("Nice try!!, Not correct")
        try_again()

guess_again()
if guess == 'Artist' or 'musician':
    artist_guess = str(input("Who is my favorite musician: \n"))
    if artist_guess == 'Eminem' or 'eminem':
        print('Correct!!')
        try_again()
    else:
        print("Nice try!!, Not correct")
        try_again()

guess_again()
if guess == 'Location' or 'City':
    city_guess = str(input("Where was my favorite music produced: \n"))
    if city_guess == 'Michigan':
        print('Correct!!')
        try_again()
    else:
        print("Nice try!!, Not correct")
        try_again()



