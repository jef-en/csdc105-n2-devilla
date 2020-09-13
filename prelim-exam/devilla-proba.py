# Author          : Jefen B. De Villa
# Course and Year : BS Information Technology 2nd Year
# Filename        : devilla-proba.py
# Description     : A program that prints a pyramid based on the users input. 
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

test_case = int(input())                 # accepts the number of test cases

i = 0                                    # initialize the variable to zero(0)
while i < test_case:                     # this will continue running based on test_case
    rows, character = input().split()    # ask the user of the height as well as symbol for the pyramid
    rows = int(rows)                     # 14-15. assign to another variable the user input, in which case;
    character = str(character)           # the rows and the character
    i += 1                               # increment until it satisfies the "test_case"
    
    j = 0                                # initialize the variable to zero(0)
    print ("Case {}:".format(i))         # print statement for printing the "Cases"
    for j in range (0, rows):            # a loop that will go through, from 0 to the user input (rows)
        for k in range (0, rows-j-1):    # row-j-1 to decrease the space, then;
            print(end = " ")             # a print function that prints the space based from (rows-j-1)
        for k in range (0, 2*j+1):       # multiply then add 1 so that it makes odd, then;
            print (character, end = "")  # a print function that will print the character that the user inputs
        print()                          # print function that prints all
    