# Author : De Villa, Jefen B.
# Course and Year : BS Information Technology 2nd Year
# Filename : dice.py
# Description : A module that contains the methods of the class Dice and Tetrahedron
# Honor Code : I have not given nor received any unathorized help in
#              completing this exercise. I am also well aware of the
#              policies stipulated in the AdNU student handbook.

import random                                  # imported 'random' since the printing of random numbers will not work without it.

class Dice:                                    # created class Dice
    def __init__(self, sides = 6):             # __init__ method with a parameter 'sides' that has a default value of 6
        self.sides = sides                     # self.sides is the actual attribute of the class Dice 
	
    def roll(self, randomizer = 6):            # method for class Dice that has a parameter 'randomizer' with a default value of 6;
        print(random.randint(1, randomizer))   # will print random numbers from 1, 2 to 6. Or print numbers 1 to n depending on user arguments.
	
    def __str__(self):                         # str method (to string) that will represent the 
        return "DICE: {}".format(self.sides)   # return statement that will output the word "DICE" with the number of sides 

class Tetrahedron(Dice):                       # created a child class 
    def __init__(self, sides):                 # redifining the __init__ method for the class Dice
        self.sides = sides                     # define the attribute 'sides' and set its values by using the parameter 'sides'
        super().__init__(sides)                # call the __init__ method of the parent class (Dice).
