# Author : De Villa, Jefen B.
# Course and Year : BS Information Technology 2nd Year
# Filename : devilla_e4.py
# Description : main program 
# Honor Code : I have not given nor received any unathorized help in
#              completing this exercise. I am also well aware of the
#              policies stipulated in the AdNU student handbook.

from geometry import *                                      # this will get all the functions in the module geometry.py

number = input("Enter the side lenghts of a triangle: ")    # prompt the user to enter 3 numbers
a, b, c = number.split(",")                                 # for the purpose of inputting 3 numbers separated by comma
a = float (a)                                               # line 13 - 15;
b = float (b)                                               # change the value from;
c = float (c)                                               # string to float.

checker_answer = checker(a, b, c)                           # I pass the return value of the function checker() to a variable to be used further
if checker_answer == True:                                  # if statement that will check wether the input is valid or not 
    perimeter_answer = perimeter(a, b, c)                   # pass the return value of the function perimeter() to a variable
    print("Perimeter:", "{:.2f}".format(perimeter_answer))  # print the perimeter of the triangle
    area_answer = triangle_heronsarea(a, b, c)              # pass the return value of the function triangle_heronsarea() to a variable
    print("Area: " "{:.2f}".format(area_answer))            # print the area

else:                                                       # else statement for outputting if the input is invalid
    print ("Invalid Input")                                 # print "Invalid input"




