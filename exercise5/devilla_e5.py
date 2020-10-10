# Author : De Villa, Jefen B.
# Course and Year : BS Information Technology 2nd Year
# Filename : devilla_e5.py
# Description : driver program that will print the Dice sides and the random number of sides. 
# Honor Code : I have not given nor received any unathorized help in
#              completing this exercise. I am also well aware of the
#              policies stipulated in the AdNU student handbook.

from dice import Dice, Tetrahedron   # imported the module dice 

d = Dice()                           # create a new instance of class Dice
print(d)                             # since we have the __str__ method we can easily print it like so, and it will print whatever return value the method have.
for i in range(5):                   # loop that will iterate 5 times; 
	d.roll()                         # through the method roll().

d = Dice(10)                         # create a new instance of the class dice that has 10 as the arguments
print(d)                             # we can easily print(d) since we have created the __str__ method.
for i in range(5):                   # loop that will iterate 5 times in;
    d.roll(10)                       # the method roll() with 10 as the passed argument

t = Tetrahedron(4)                    # created a new instance of the class Tetrahedron with 4 as arguments 
print(t)                             # same thing with the class Dice we create a __str__ method, we can easily print the object 't'
for i in range(10):                  # loop that will iterate 10 times;
    t.roll(4)                        # through the method roll() with 4 as argument