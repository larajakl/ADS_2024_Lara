"""
Write a program that prints out the message "hello world!" and then asks "shall we continue?"
until the user inputs "no". Then the program should print out "okay then" and finish.

Example:
    hello world!
    shall we continue? >> yes
    hello world!
    shall we continue? >> oui
    hello world!
    shall we continue? >> jawohl
    hello world!
    shall we continue? >> no
    okay then
"""
# print("hello world!")
# answer = input("shall we continue? ")
#
# while answer != "no":
#   print("hello world!")
#   answer = input("shall we continue? ")
#
#
# print("okay then")

"""
Write a program which asks the user for integer numbers.

- If the number is below zero, the program should print out the message "invalid number".
- If the number is above zero, the program should print out the square root of the number using the Python sqrt function.
- In either case, the program should then ask for another number.
- If the user inputs the number zero, the program should stop asking for numbers and exit the loop.

To use the `sqrt` function in python add the following to the top of your file: 
    from math import sqrt
Then use it like:
    print(sqrt(9))
    
Example:
    Please type in a number: >> 16
    4.0
    Please type in a number: >> 4
    2.0
    Please type in a number: >> -3
    invalid number
    Please type in a number: >> 1
    1.0
    Please type in a number: >> 0
    Exiting...
"""
# number = 1
#
# while number != 0:
#   number = int(input("Please type in a number: "))
#   if number < 0:
#     print("invalid number")
#   elif number > 0:
#     print(sqrt(number))
#
# print("Exiting...")

"""
This program should print out a countdown. However, the program doesn't quite work. Please fix it.
Hint: you can use the debugger of PyCharm to see how the program is executing.
"""
# Fix the code
number = 5
print("Countdown!")
while True:
  print(number)
  number = number - 1
  if number > 0:
    break

print("Now!")

# solution:
# Fix the code
# number = 5
# print("Countdown!")
# while True:
#   print(number)
#   number = number - 1
#   if number == 0:
#     break
#
# print("Now!")

# solved without while True loop:
# number = 5
# print("Countdown!")
# while number != 0:
#   print(number)
#   number = number - 1


# print("Now!")

"""
Write a program which asks the user for a year, and prints out the next leap year.
If the user inputs a year which is a leap year (such as 2024), the program should print out the following leap year.

Examples:
    Year: >> 2023
    The next leap year after 2023 is 2024
    
    Year: >> 2024
    The next leap year after 2024 is 2028
"""
# year = int(input("Year: "))
#
# while year > 0:
#     if year % 4 == 0:
#         if year % 100 != 0 or year % 400 == 0:
#             print(f"The next leap year after {year} is {year + 4}")
#         else:
#             print(f"The next leap year after {year} is {year + 4 - (year % 4)}")
#     else:
#         print(f"The next leap year after {year} is {year + 4 - (year % 4)}")
#     year = int(input("Year: "))

"""
Please write a program which keeps asking the user for words. 
If the user types in end, the program should print out the story the words formed, and finish.

Example:
  Please type in a word: >> Once
  Please type in a word: >> upon
  Please type in a word: >> a
  Please type in a word: >> time
  Please type in a word: >> there
  Please type in a word: >> was
  Please type in a word: >> a
  Please type in a word: >> girl
  Please type in a word: >> end
  Once upon a time there was a girl
"""
# story = ""
# word = ""
#
# while True:
#     word = input("Please type in a word: ")
#     if word == "end":
#         break
#     else:
#         story += word + " "
#
#
# print(story)

"""
Change the program above so that the loop ends also if the user types in the same word twice in a row.
"""
# story = ""
# word = ""
# previous_word = ""
#
# while True:
#   previous_word = word
#   word = input("Please type in a word: ")
#   if word == "end" or word == previous_word:
#     break
#   else:
#     story += word + " "
#
# print(story)

"""
Please write a program which asks the user for integer numbers. 
The program should keep asking for numbers until the user types in 0.

After reading the numbers the program should 
  - print out how many numbers were typed in
  - the sum of numbers entered
  - the mean of numbers entered
  - the number of positive and negative numbers entered
  
Example output
  Numbers typed in 4
  The sum of the numbers is 34
  The mean of the numbers is 8.5
  Positive numbers 3
  Negative numbers 1
"""
# number = 0
# amount_of_numbers = 0
# sum = 0
# positive_numbers = 0
# negative_numbers = 0
#
# while True:
#   number = int(input("Please type in an integer number: "))
#   if number == 0:
#     break
#   else:
#     sum += number
#     amount_of_numbers = amount_of_numbers + 1
#     if number > 0:
#       positive_numbers = positive_numbers + 1
#     elif number < 0:
#       negative_numbers = negative_numbers + 1
#
# print(f"Numbers typed in: {amount_of_numbers}")
# print(f"The sum of the numbers is: {sum}")
#
# if sum != 0:
#   print(f"The mean of the numbers is: {sum / (amount_of_numbers)}")
#
# print(f"Positive numbers: {positive_numbers}")
# print(f"Negative numbers: {negative_numbers}")

"""
Largest Number

Write a program which asks the user for float numbers.
The program should keep asking for numbers until the user types in 0 or a negative number.
The program should then print the largest number.
If the first number entered is less than or equals to 0, the program should quit and print "no number entered".

DO NOT USE LISTS TO SOLVE THIS EXERCISE!

Examples:
  Number 1: >> 3
  Number 2: >> 4.67
  Number 3: >> 120.5
  Number 4: >> 70
  Number 5: >> 0
  The largest number is 120.5
  
  Number 1: >> -1.11
  No number entered.
"""
# largest_number = float("-inf")
# number = float(input("Number: ")) # need to ask for number input outside the loops because I need 2 different print statements for 2 conditions
#
# if number == 0 or number < 0:
#     print("No number entered.")
#
# else:
#     previous_number = number
#     while number > 0:
#         if number > largest_number:
#             largest_number = number
#         previous_number = number
#         number = float(input("Number: "))
#     print(largest_number)

# Solved without the variable "previous_number" which might be unnecessary:

# largest_number = float("-inf")
# number = float(input("Number: ")) # need to ask for number input outside the loops because I need 2 different print statements for 2 conditions
#
# if number == 0 or number < 0:
#     print("No number entered.")
#
# else:
#     while number > 0:
#         if number > largest_number:
#             largest_number = number
#         number = float(input("Number: "))
#     print(largest_number)

# Solved with number count in console going up:

# largest_number = float("-inf")
# number_count = 1  # Variable to keep track of the number count
#
# while True:
#     number = float(input(f"Number {number_count}: "))
#     if number <= 0:
#         break  # Exit the loop if the entered number is 0 or negative
#     if number > largest_number:
#         largest_number = number
#     number_count += 1  # Increment the number count for the next iteration
#
# if number_count == 1:
#     print("No number entered.")
# else:
#     print(f"The largest number is {largest_number}")

"""
Write a program that reads in an integer number (number of lines) and generates the subsequent output using 
two loops on the console (see below). 
If the input of numbers is smaller or equal to 0 an error message should be printed.

Examples:
  n: >> 4
  1
  2 3
  4 5 6
  7 8 9 10
  
  n: >> -1
  Invalid number!
"""
# n = int(input("n: "))
#
# if n == 0 or n < 0:
#     print("Invalid number!")
#
# else:
#     start_number = 1
#     current_row = 1
#     while current_row <= n: # make sure only n rows are printed (1, 2, 3, 4)
#       current_column = 1 # we want to start printing in the first column at each row
#       while current_column <= current_row: # so that 1 number is printed in row 1, 2 numbers are printed in row 2 and so on
#         print(start_number, end=" ")
#         start_number += 1 # increase the printed number in every inner loop
#         current_column += 1 # move one column further after every number printed.
#       print()
#       current_row += 1

# Solved in a way that the programme keeps asking for numbers

# n = int(input("n: "))
# while True:
#     if n <= 0:
#         break
#     else:
#         start_number = 1
#         current_row = 1
#         while current_row <= n:  # make sure only n rows are printed (1, 2, 3, 4)
#             current_column = 1  # we want to start printing in the first column at each row
#             while current_column <= current_row:  # so that 1 number is printed in row 1, 2 numbers are printed in row 2 and so on
#                 print(start_number, end=" ")
#                 start_number += 1  # increase the printed number in every inner loop
#                 current_column += 1  # move one column further after every number printed.
#             print()
#             current_row += 1
#     n = int(input("n: "))
#
# print("Invalid number")

# Solved with while True loop and in a way that the programme keeps asking for numbers

# while True:
#     n = int(input("n: "))
#     if n == 0 or n < 0:
#         break
#     else:
#         start_number = 1
#         current_row = 1
#         while current_row <= n:  # make sure only n rows are printed (1, 2, 3, 4)
#             current_column = 1  # we want to start printing in the first column at each row
#             while current_column <= current_row:  # so that 1 number is printed in row 1, 2 numbers are printed in row 2 and so on
#                 print(start_number, end=" ")
#                 start_number += 1  # increase the printed number in every inner loop
#                 current_column += 1  # move one column further after every number printed.
#             print()
#             current_row += 1
#
# print("Invalid number")

"""
Write a program that uses loops to create a pyramid of stars '*' on the console. 
The pyramid should have exactly 6 rows.
Example:
       *
      ***
     *****
    *******
   *********
  ***********
"""
# rows = 6
#
# # Outer loop for rows
# i = 1 #  i represents the current row
# while i <= rows:
#     print(" " * (rows - i), end="")
#     # Inner loop for columns
#     j = 1  # j represents the current column. At the beginning of each inner loop, j is 1.
#     while j <= 2*i - 1:  # controls the inner loop, which is responsible for printing the * in each row of the pyramid
#         print("*", end="")  # Print asterisk
#         j += 1
#     print()  # Move to the next line after printing each row
#     i += 1

"""
The other way around it would be:

Example:
***********  # row 1 - 11
 *********  # row 2 - 9
  *******  # row 3 - 7
   *****  # row 4 - 5
    ***  # row 5 - 3
     *  # row 6 - 1

"""
# rows = 6
#
# # Outer loop for rows
# i = rows  # Start from the maximum number of rows
# while i >= 1:  # Reverse the range
#     print(" " * (rows - i), end="")
#     # Inner loop for columns
#     j = 1
#     while j <= 2*i - 1:
#         print("*", end="")
#         j += 1
#     print()
#     i -= 1  # Decrement i to go to the previous row

"""
EXPLANATION:
The condition while j <= 2*i - 1 arises from observing the pattern of stars in each row of the pyramid
and understanding how to generate that pattern programmatically.

To analyze the pattern:
In a pyramid pattern, the number of stars in each row increases by 2 compared to the previous row.  
    Starting from the top row (row 1), there's 1 star.
    In the second row (row 2), there are 3 stars.
    In the third row (row 3), there are 5 stars.
    This continues with 7 stars in row 4, 9 stars in row 5, and so on.

Given this pattern, we need a way to calculate the number of stars for each row programmatically.
That's where the expression 2*i - 1 comes into play.

    i represents the current row number.
    2*i gives us a sequence of numbers: 2, 4, 6, 8, 10, and so on, which are the counts of stars if the pattern were to have an additional star in each row.
    But we want the actual number of stars in each row to be one less than these counts. So, by subtracting 1 (- 1), we get the correct counts of stars for each row: 1, 3, 5, 7, 9, and so on.

Thus, 2*i - 1 gives us the correct number of stars to print in each row,
and the loop condition while j <= 2*i - 1 ensures that the loop runs until
the correct number of stars are printed in the current row.
"""

"""
Write a program to calculate the average grade. The console reads in grades between 1 and 5 
until the number 0 is entered. If an invalid grade is entered, an error message is displayed, 
the grade is not counted and the prompt progresses. It is assumed that only integers are entered. 
At the end of the input, the grade average and the number of negatives (grade = 5) are output.

Example:
  Mark 1: >> 5
  Mark 2: >> 3
  Mark 3: >> 10
  Invalid mark!
  Mark 3: >> 1
  Mark 4: >> 5
  Mark 5: >> 0
  Average: 3.50
  Negative marks: 2
"""
# mark = -1  # because it is outside the valid range of grades (so won't be counted) and ensures that the loop will start
# grades_sum = 0
# number_grades_entered = 0
# grade_average = 0
# number_of_5s = 0

# while True:
#     mark = int(input("Mark: "))
#     if mark > 5 or mark < 0:
#         print("Invalid mark!")
#         continue
#     elif 1 <= mark <= 5:
#         grades_sum += mark
#         number_grades_entered += 1
#         if mark == 5:
#             number_of_5s += 1
#     else:  # mark == 0
#         break
#
# if number_grades_entered != 0:
#     grade_average = grades_sum / number_grades_entered
#     print(f"Average: {grade_average}")  # or write print(f"Average: {grade_average: .2f}") to display the average with 2 decimal places
#     print(f"Negative marks: {number_of_5s}")


# solved without endless loop (without while True loop):

# while mark != 0:
#     mark = int(input("Mark: "))
#     if mark > 5 or mark < 0:
#         print("Invalid mark!")
#         continue
#     elif 1 <= mark <= 5:
#         grades_sum += mark
#         number_grades_entered += 1
#         if mark == 5:
#             number_of_5s += 1
#
# if number_grades_entered != 0:
#     grade_average = grades_sum / number_grades_entered
#     print(f"Average: {grade_average}")  # or write print(f"Average: {grade_average: .2f}") to display the average with 2 decimal places
#     print(f"Negative marks: {number_of_5s}")



# # line break and making tabs:

# print("\tHelloWorld!\n\n")
# print("Next line")

# # how to make a line break after arithmetic operations inside a print command:
# print(str(2 + 2) + "\n")
# print(f"{2 + 2} \n")
# print("Next line")


# # no line change:

# print("Hi ", end="")
# print("there!")
# --> Hi there!

# # find out length of a variable / check if list is empty:

# len()
# len(tasks)

# # round a number:
# Round returns a floating point number that is a rounded version of the specified number,
# with the specified number of decimals. When no number of decimals is specified,
# the default is 0 so you get the nearest integer number.

# number = 3.3333333
# print(str(round(number, 2)))
# --> 3.33

# # .lower() to convert input to lowercase
# fruit = input("Enter a fruit: ").lower()
# print(fruit)


# assessment 1

"""
OrderOfNumbers
"""

while True:
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))
    if n1 < n2 < n3:
        print("numbers are ascending")
    elif n1 > n2 > n3:
        print("numbers are descending")
    else:
        if n1 % 2 == 0 and n2 % 2 == 0 and n3 % 2 == 0:
            print("no specific order, but all even")
        elif n1 % 2 != 0 and n2 % 2 != 0 and n3 % 2 != 0:
            print("no specific order, but all odd")
        else:
            print("no specific order")




"""
SumUp
"""
n1 = int(input("n1: "))
n2 = int(input("n2: "))


if n2 <= 0 and n1 <= 0:
    print("n1 and n2 need to be > 0")

elif n1 <= 0:
    print("n1 needs to be > 0")

elif n2 <= 0:
    print("n2 needs to be > 0")

elif n2 < n1:  # I didn't include  "n1 > 0 and n2 > 0" in this statement because it's already checked for before
    print("n2 needs to be > n1")


else:
    i = 0
    while n1 + i <= n2:
        print(n1 + i, " ", end="")
        i += 1

