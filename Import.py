import random as x
import time
import math
# Rand_Integer = x.randint(8, 11)
# print(Rand_Integer)
#
# rand_float = x.random()
# print(rand_float)
#
# rand_uni = x.uniform(100, 200)
# print(rand_uni)
# List = [1, 3, 5, 6, 7, 8, 9]
# picker = x.choice(List)
# print(picker)
# x.shuffle(List)
# print(List)
# starting_time = time.clock()
# print('Hello World!!!')
# Finish_time = time.clock()
# time_taken = starting_time -  Finish_time
# print('Starting time =' + starting_time)
# print('Finish time =' + Finish_time)
# print('Time Taken =' + time_taken)
# temp = math.floor(3.97)
#
# temp = math.exp(5)
# print(temp)


# Python program to display calendar using import-calendar module
import calendar

# Printing the calendar of the specified month of a specified year.
print("Calendar of specific month of the year")
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
print(calendar.month(yy, mm))

# Printing the complete calendar of a specified year
print("Calendar of specific year")
x = int(input("Enter year: "))
print("The calender of year 2021 is : ")
print(calendar.calendar(x, 1, 1, 5))

# Determining the number of leap years between two specified years
print("Finding the number of leap years between two years ")
year_one = int(input("Enter first year: "))
year_two = int(input("Enter second year: "))
print("The leap year between", year_one, " and ", year_two, "are : ", end="")
print(calendar.leapdays(year_one, year_two))


