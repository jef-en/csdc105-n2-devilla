# Author : De Villa, Jefen B.
# Course and Year : BS Information Technology 2nd Year
# Filename : geometry.py
# Description : A module containing Heron's formula 
# Honor Code : I have not given nor received any unathorized help in
#              completing this exercise. I am also well aware of the
#              policies stipulated in the AdNU student handbook.

def checker (a, b, c):                                                                                   # function for checking if the input is valid or not
    if a + b < c:                                                                                        # if statement for checking wether sum of a and b is less than c
        return False                                                                                     # return false if it satisfies
    else:                                                                                                # else return true
        return True

def perimeter (*side_lengths):                                                                           # function for computing for the semi perimeter
    total_sum = 0                                                                                        # initialize first a container of all the sum to 0
    for s in side_lengths:                                                                               # iterate through all the input 
        total_sum += s                                                                                   # add all and pass the answer to total_sum
    return total_sum / 2                                                                                 # return statement for returning the total sum divided by 2 

def triangle_heronsarea (a, b, c):                                                                       # function for computing the area
    semi_perimeter = perimeter(a, b, c)                                                                  # call the function perimeter inside 
    area = (semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5  # formula for computing the area
    return area                                                                                          # return statement 
    

