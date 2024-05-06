"""
Exercises "Functions"
"""

"""
### Function Definition / Execution ###

Define a function called "bark()". When executed, "Woof" should get printed to the console.
Execute the function after its definition and run the program!
"""

# def bark():
#     print("Woof!")
#
# bark()

"""
### Function with 1 Argument, additional logic ###

Write a program that asks the user to enter an animal. The program should respond with the corresponding animal sound.
Define a function called "makeSound(animal)". The function should use the given input to print the correct animal sound.
Add functionality for at least 3 animals and print the right sounds.
If the animal doesn't exists in the program, print "???".
Use a loop to repeatedly ask the user to enter another animal.
Make sure that upper- and lowercase letters both work when entering an animal.

Examples:
    Please enter an animal: >> dog
    Woof
    Please enter an animal: >> Cat
    Meow
    ...
"""

# def make_sound(animal : str):
#     animal = animal.lower()
#     if animal == "dog":
#         print("Woof!")
#     elif animal == "cat":
#         print("Meow!")
#     elif animal == "pig":
#         print("Quieeek!")
#     else:
#         print("???")
# #
# # with loop in case of wrong input:
#
#
# animal = input("Please enter an animal: ").lower()
# while animal != "dog" and animal != "cat" and animal != "pig":
#     make_sound(animal)
#     animal = input("Please enter an animal: ").lower()
#
#
# make_sound(animal)

# # make_sound("CAT")  # would be hard coded but we don't want this in this example
#
# if we wanted to make it run 5 times:

# i = 0
# while i < 5:
#     animal_input = input("enter an animal: ").lower()
#     make_sound(animal_input)
#     i += 1
#
#
# # make it run 5 times with for range thingy:
#
# for i in range(0,5):  # (0 is inclusive, 5 is exclusive) !!
#     animal_input = input("enter an animal: ").lower()
#     make_sound(animal_input)
#     i += 1


# we did something else here but I didn't remember the rest:
# result = make_sound(animal_input)
# if result == "???":
#     continue
# else:
#     break


"""
### Function with 2 Arguments ###

Write a function named print_many_times(text, times), which takes a string and an integer as arguments. 
The integer argument specifies how many times the string argument should be printed out.

Example:
    print_many_times("Gimme Five!", 5)
    Gimme Five!
    Gimme Five!
    Gimme Five!
    Gimme Five!
    Gimme Five!

Additional Task:
Instead of "hard coding", let the user enter the text and the number of times to print it!
Ask the user repeatedly using a loop.
"""

# def print_many_times(text: str, times: int):
#       print(f"{text} \n" * times) # or:
#       # print((text + "\n") * times) # or:
#       # for i in range(times):
#       #     print(text)  # or:
#       # i = 0
#       # while i < times:
#       #     print(text)
#       #     i += 1
# #
# # hard coding: (not right solution in this example)
# print_many_times("Gimme Five!", 5)
# print_many_times("Gimme Three!", 3)

# let user enter text and number of times and loop used to ask repeatedly:
# while True:
#     text = input("Enter a text: ")
#     times = int(input("Enter a number of times: "))
#     print_many_times(text, times)


"""
### Return Values ###

Define a function named greatest_number, which takes three arguments. The function returns the greatest in value of the 
three. Use the already defined function "print_greatest" and pass the return value of your function to it!

Example:
    return_value = greatest_number(3, 4, 1)
    print_greatest(return_value)
    The greatest number is 4!
    
Additional Task:
Add a type hint to the return value of the function!
"""

# def print_greatest(number : float):
#     print(f"The greatest number is {number}!")
#
# def greatest_number(a: int, b: int, c: int) -> int: # if the assessment says use type hints then yes, otherwise not necessary
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     elif c > a and c > b:
#         return c
# #
# return_value = greatest_number(3, 4, 1)  # (a=3, b=4, c=1) would be the same
# print_greatest(return_value)
#
# # or:
# print_greatest(greatest_number(3, 4, 1))


# Additional task:

# just add "-> int" here
# def greatest_number(a: int, b: int, c: int) -> int:

"""
### Type Hints ###

Refactor your programs from above and add type hints to all function arguments and return values (if available)!
"""

# No code here, refactor the programs above!
# Note to self: not all functions I defined above have arguments or return values!

"""
### Named arguments ###

Define a function named super_print which takes two arguments, a string and a boolean value.
If the boolean value is false, print the text as it was. If its True, print it in all upper case.
Use named arguments to use a different order of the arguments. First, use the string as first argument. For the second
call, use the boolean value as the first argument. Also, make use of type hints for the function arguments.

Example Outputs:
    HELLO WORLD
    hello world
"""

# def super_print(x : str,y : bool):
#     if y == False:
#         print(x)
#     else:
#         x = x.upper()
#         print(x)
#
# super_print(x="Bye", y=False)
#
# super_print(y=True, x="Hello")

"""
### Default Values ###

Define a simple function greet() that takes one argument "name". The function should print a greeting for the entered 
name. Ask the user for his/her name and execute the greet function, passing the name as an argument.
If nothing was entered, use a default value for the name to greet "Unknown".

Hint: An empty string is still a value you can pass, be careful :-)

Example:
    Please enter your name: >> René
    Hello René!
    Please enter your name: >> 
    Hello Unknown!
"""

# def greet(name="Unknown"):
#     print("Hello " + name + "!")
#
# name = input("Please enter your name: ")
# if name == "":
#     greet()
#
# else:
#     greet(name)



# tried something out here:

# def greet(name):
#     if name == "":
#         print("???")
#     print("Hello, ", name)
#     return
#
# name = input("Type in a name: ")
# greet(name)

string = "hi there"
print(string[2:4])