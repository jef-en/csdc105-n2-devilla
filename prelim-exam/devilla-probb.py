# Author          : Jefen B. De Villa
# Course and Year : BS Information Technology
# Filename        : devilla-probb.py
# Description     : A program that will print Fibonacci Sequence based on the users input
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

test_case = int(input())                             # accepts the number of test cases

i = 0                                                # initialize the variable to zero(0)
while i < test_case:                                 # loop that will run based on the test_case
    number = int(input())                            # this will ask the user for the number that will manipulated
    i += 1                                           # increment until it satisfies the "test_case"

    first_number, second_number = 0, 1               # initialize the value of the first and second number
    third_number = 0                                 # initialize the value of the next number 
    j = 0                                            # initialize the variable to zero(0)
    print ("Case {}:".format("hello"), end = " ")          # print statement for printing the "Cases"
    while ( j <= number):                            # this loop will terminate if the j = 0, becomes equal to the "number"
        print(third_number, end = " ")               # every run this will print the changes made to the third number
        first_number = second_number                 # assign the value of the first number to the second number
        second_number = third_number                 # assign the value of the second number to the third
        third_number = first_number + second_number  # to get the next number add the previous 2 number
        j += 1                                       # increment until it satisfies the "number"
    print ()                                         # print function to print all 