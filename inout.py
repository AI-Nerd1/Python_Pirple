from pathlib import Path
name = input(str("Enter then name of your file: "))
if Path(name+".txt").is_file():
    print('Choose what you want to do to the file: '
          '\n A - To Read the file '
          '\n B - To delete the file and .start over '
          '\n C - To Append the file')
    choice = input('Type your choice: ')
    if choice == "A" or choice == 'a':
        existing_file = open(name + ".txt", "r+")
        print(existing_file.read())
        existing_file.close()

    if choice == "B" or choice == 'b':
        existing_file = open(name + ".txt", "w")
        text = input("Warning!! The file is going to be over-written"
                     "\n Type the content you want to write to the file here: ")
        existing_file.write(text)
        existing_file.close()

    if choice == "C" or choice == 'c':
        existing_file = open(name + ".txt", "a")
        text = input("Type the content you want to append to the file here: ")
        existing_file.write(text)
        existing_file.close()

else:
    new_file = open(name + ".txt", "w")
    text = input("Type the content of the file here: ")
    new_file.write(text)
    new_file.close()
