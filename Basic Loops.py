# print('hello world')
# World = "Now you see me"
# letters=[]
# for x in World:
#     print(x)
#     if x == "e":
#         print('I see, I saw')
#     letters.append(x)
#
# print(letters)
#
# number = 20
# if number%2 == 0:
#     print("Even")
# if number%2 == 1:
#      print("Odd")
#
# # for x in condition:
# #     action
# #
# # while (condition):
# #     action
#
# # counter = 1
# # sum = 0
# # while (counter <=100):
# #     print(counter)
# #     sum = sum + counter
# #     counter = counter + 1
#
# # print (sum)
# # index = 0
# Letters = ['a', 'b', 'c', 'd', 'e', 'f']
# print(len(Letters))
# # while (index < len(Letters)):
# #     print(index)
# #     print(Letters[index])
# #     index = index + 1
#
#
# height = 5000
# time = 0
# velocity = 100
#
# while (height>0):
#     height =  (height - velocity)
#     time = time + 1
#     print('Distance covered after ', time, 'sec = ', 5000-height, 'meters')
#
#
# print('Current height = ', height)
# print('Total time taken = ', time, 'sec')


# students = ['Logan', 'Adele', 'Paul', 'Leo', 'Rex', 'Zuleim']
# index = 0
# Position = 1
#
#
# for name in students:
#     if name == 'Zuleim':
#         break
#     index = index + 1
#     Position = index + 1
# print(name)
# print(index)
# print(Position)
# index = 0
# friends = ['Tolu', 'Precious', 'Wale', 'Tife', 'Preye']
# for guy in friends:
#     if index == 3:
#         break
#     index = index + 1
#     Position = Position = 1
# print(guy)
# print(index)
# print(Position)
#
#
# X = 'abcd'
# for i in range(len(X)):
#     print(i)


# Program for Fizz-Buzz game

num = 1
while(num<= 100):
    if (num % 5 == 0 and num % 3 == 0):
        print('FizzBuzz (', num, ')')

    elif(num % 3 == 0):
        print('Fizz (', num, ')')

    elif(num % 5 == 0):
        print('Buzz (', num, ')')

    elif (num % 2 != 0 and num % 3 != 0 and num % 5 != 0):
        print('Prime (', num, ')')
    else:
        print(num)
    num = num + 1


