"""
Write a program that asks the user for a number.
The program then determines if the number is even or odd and prints out an appropriate message.

Hint: For checking if the number is even or odd, use the Modulo operator:
remainder = number % 2

Example:

    Enter a number: >> 17
    The number 17 is odd.
"""
#number = int(input("Enter a number: "))
#is_even = number % 2 == 0
#is_uneven = number % 2 != 0

#if is_even == True:
#    print(f"The number {number} is even.")
#
#elif is_uneven == True:
#    print(f"The number {number} is odd.")




"""
Write a program that asks the user for their exam grade (as a percentage). 
The program then prints out the following message:

* If the grade is below 50%: "Unfortunately, you failed the exam."
* If the grade is 60% or above: "You passed the exam!"
* If the grade is higher or equal to 90: "You are excellent!"

Example:

    Enter your exam grade: >> 63
    You passed the exam!
"""
grade = input("What is your exam grade? ")

#if float(grade) < 50:
 #   print("Unfortunately, you failed the exam.")

#elif float(grade) >= 60 and float(grade) < 90:
 #   print("You passed the exam!")

#elif float(grade) >= 90:
 #  print("You are excellent!")

#or like this (because program goes through all if statements and only goes to elif statement if the if statements don't apply):

#if float(grade) < 50:
 #   print("Unfortunately, you failed the exam.")

#if float(grade) >= 90:
  #  print("You are excellent!")

#elif float(grade) >= 60:
   # print("You passed the exam!")

"""
Write a program that simulates a simple lunch ordering system. 

1. Ask the user if they want a sandwich, salad, or wrap.
2. If they want a sandwich, ask what kind (chicken, beef, veggie).
3. If they want a salad, ask what dressing (vinaigrette, ranch, caesar).
4. If they want a wrap, ask if they want it toasted.
5. Print a confirmation of their order choice.

Hint: You don't need to verify the user input. But if you want a challenge, try to repeat reading the user input
in case of invalid input. To do so, you might need to research a little bit about "loops" which will be 
covered later in this course :-)

Example:

    Would you like a sandwich, salad, or wrap? >> salad
    What kind of dressing would you like: vinaigrette, ranch, or caesar? >> ranch
    Your order: Salad with ranch dressing
"""
#main_order = str(input("Would you like a sandwich, salad, or wrap? "))

#sandwich = main_order or salad = main_order or wrap = main_order


#main_order = main_order1 or main_order2 or main_order3


#if main_order = salad:
  #  print("What kind of dressing would you like: vinaigrette, ranch, or caesar? ")



