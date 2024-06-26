import math

"""
Write a program which asks the user for a string and an amount.
The program then prints out the string as many times as specified by the amount.
The printout should all be on one line, with no extra spaces or symbols added.

Example:
    Please type in a string: >> hey
    Please type in an amount: >> 4
    heyheyheyhey
"""
# string = input("Please type in a string: ")
# amount = int(input("Please type in an amount: "))
#
# print(string * amount)

"""
Write a program which asks the user for two strings and then prints out whichever is the longer of the two - 
that is, whichever has the more characters. If the strings are of equal length, the program 
should print out "The strings are equally long".

Examples:

    Please type in string 1: >> hello
    Please type in string 2: >> world
    The strings are equally long
    
    Please type in string 1: >> hey
    Please type in string 2: >> world
    world is longer
"""

# string1 = input("Please type in string 1: ")
# string2 = input("Please type in string 2: ")
#
# if len(string1) > len(string2):
#     print(f"{string1} is longer")
#
# elif len(string1) < len(string2):
#     print(f"{string2} is longer")
#
# else:
#     print("The strings are equally long")

"""
Write a program which asks the user for a string. The program then prints out the input string in reversed order, 
from end to beginning. Each character should be on a separate line.
Try to solve this example in 2 ways:
    * once using positive indeces
    * once using negative indeces
"""
## using negative indeces:
#
# string = input("Please type in a string: ")
#
# a = -1
#
# while a >= -len(string):
#     print(string[a])
#     a -= 1
#
#
## using positive indeces:
#
# string = input("Please type in a string: ")
#
# a = len(string) - 1
#
# while a >= 0:
#     print(string[a])
#     a -= 1

## solved with for loop:

# string = input("String here: ")

# using negative indeces:

# for i in range(-1, -len(string) - 1, -1):  # start, stop (not included), step
#     print(string[i])
#
# using positive indeces:
#
# for i in range(len(string) - 1, - 1, - 1):
#     print(string[i])


"""
Write a program which asks the user for a string. 
The program then prints out a message based on whether the second character and the second to last character 
are the same or not. See the examples below.

Examples:
    Please type in a string: >> python
    The second and the second to last characters are different
    
    Please type in a string: >> pascal
    The second and the second to last characters are a
"""
# string = input("Please type in a string: ")
#
# if string[1] == string[-2]:
#     print(f"The second and the second to last characters are {string[1]}")
#
# else:
#     print("The second and the second to last characters are different")

"""
Write a program which prints out a line of hash characters, the width of which is chosen by the user.

Examples:
    Width: >> 8
    ########
    
    Width: >> 2
    ##
"""
# width = int(input("Choose width: "))
#
# print(width * "#")


"""
Modify the previous program so that it also asks for the height, and prints out a rectangle of hash characters accordingly.

Example:
    Width: >> 10
    Height: >> 3
    ##########
    ##########
    ##########
"""
# width = int(input("Choose width: "))
# height = int(input("Choose height: "))
#
# i = 1
#
# while i <= height:
#     print(width * "#")
#     i += 1

"""
Write a program which asks the user for a string and then prints it out so that exactly 20 characters are displayed. 
If the input is shorter than 20 characters, the beginning of the line is filled in with * characters.

You may assume the input string is at most 20 characters long.

Examples:
    Please type in a string:hello
    ***************hello
    
    Please type in a string:helloworld
    **********helloworld 
"""
# string = input("Please type in a string: ")
#
# if len(string) >= 20:
#     print(string[:20])
#
# else:
#     print("*" * (20 - len(string)) + string)



"""
Please write a program which asks the user for a string and then prints out a frame of * characters with the word in the centre.
The width of the frame should be 30 characters. You may assume the input string will always fit inside the frame.

If the length of the input string is an odd number, you may print out the word in either of the two possible centre locations.

Examples:
    Word: >> testing

    ******************************
    *          testing           *
    ******************************

    Word: >> python

    ******************************
    *           python           *
    ******************************
"""
# string = input("Word: ")

# if len(string) <= 30:
#     print("*" * 30)
#     print(f'*{int(math.ceil((30 - len(string) - 2) / 2)) * " "}{string}{int(((30 - len(string) - 2) / 2)) * " "}*')
#     print("*" * 30)
#
# math.ceil to round up a number (for example 4.3 becomes 5)

# solved without the math.ceil thing:

# if len(string) <= 30 and len(string) % 2 == 0:
#     print("*" * 30)
#     print(f'*{int(((30 - len(string) - 2) / 2)) * " "}{string}{int(((30 - len(string) - 2) / 2)) * " "}*')
#     print("*" * 30)
#
# elif len(string) <= 30 and len(string) % 2 != 0:
#     print("*" * 30)
#     print(f'*{int(((30 - len(string) - 2) / 2) + 1) * " "}{string}{int(((30 - len(string) - 2) / 2)) * " "}*')
#     print("*" * 30)


"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which begin with the first character, 
from the shortest to the longest. Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    te
    tes
    test
"""
# string = input("Please type in a string: ")
#
# print(len(string))
# a = 0
# while a <= len(string): # the right side of the [] is exclusive, that's why we need a <= len() and not a < len()!
#     print(string[0:a])
#     a += 1


"""
Write a program which asks the user to type in a string. 
The program then prints out all the substrings which end with the last character, from the shortest to the longest. 
Have a look at the example below.

Example:
    Please type in a string: >> test
    t
    st
    est
    test
"""
# string = input("Please type in a string: ")
#
# a = len(string) - 1
# while a >= 0:
#     print(string[a:len(string)])
#     a -= 1

"""
Write a program which asks the user to input a string. The program then prints out different messages if the string 
contains any of the vowels a, e or o.

You may assume the input will be in lowercase entirely. Have a look at the examples below.

    Please type in a string: >> hello there
    a not found
    e found
    o found
    
    Please type in a string: >> hiya
    a found
    e not found
    o not found
"""
# string = input("Please type in a string: ")
#
#
# if "a" in string:
#     print("a found")
# else:
#     print("a not found")
#
# if "e" in string:
#     print("e found")
# else:
#     print("e not found")
#
# if "o" in string:
#     print("o found")
# else:
#     print("o not found")



"""
Write a program which asks the user to type in a string and a single character. The program then 
prints the first three character slice which begins with the character specified by the user. 
You may assume the input string is at least three characters long. The program must print out three characters, 
or else nothing.

Pay special attention to when there are less than two characters left in the string after the first occurrence of 
the character looked for. In that case nothing should be printed out, and there should not be any indexing errors 
when executing the program.

Examples:

    Please type in a word: >> mammoth
    Please type in a character: >> m
    mam
    
    Please type in a word: >> banana
    Please type in a character: >> n
    nan
    
    Please type in a word: >> python
    Please type in a character: >> n
"""
# string = input("Please type in a string: ")
# single_character = input("Please type in a character: ")
#
# if single_character in string:
#     if string.find(single_character) <= (len(string) - 3):
#         print(string[string.find(single_character):(string.find(single_character) + 3)])



"""
Write a program which finds the second occurrence of a substring. If there is no second (or first) occurrence, 
the program should print out a message accordingly.

In this exercise the occurrences cannot overlap. For example, in the string aaaa the second occurrence of the 
substring aa is at index 2.

Examples:

    Please type in a string: >> abcabc
    Please type in a substring: >> ab
    The second occurrence of the substring is at index 3.
    
    Please type in a string: >> methodology
    Please type in a substring: >> o
    The second occurrence of the substring is at index 6.
    
    Please type in a string: >> aybabtu
    Please type in a substring: >> ba
    The substring does not occur twice in the string.
"""
# string = input("Please type in a string: ")
# substring = input("Please type in a substring: ")
#
# first_occurrence = string.find(substring)
# if first_occurrence == -1:
#     print("The substring does not occur in the string at all.")
# else:
#     second_occurrence = string.find(substring, first_occurrence + len(substring)) # thing behind the comma indicates where searching starts
#     if second_occurrence == -1:
#         print("The substring does not occur twice in the string.")
#     else:
#         print(f"The second occurrence of the substring is at index {second_occurrence}")



