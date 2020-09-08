# Author          : Jefen B. De Villa
# Course and Year : BS Information Technology 2nd Year
# Filename        : devilla_e2.py
# Description     : Creating a dictionary then printing what's inside
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

data = { 
	'Name': 'Jefen B. De Villa', 
	'Animal': 'Whale,', 
	'Reason': 'Im self aware and Im realistic',
	'Hobby': 
		['* Study drawing and painting', '* Ride a bike around the neighborhood, and;',
		 '* Play mobile and computer games'],
	'Dream': 'Scientist'
	}

print('I am', (data['Name']))
print('My spirit animal is', (data['Animal']))
print('because', data['Reason'])
print('When not in school, I love too:', *(data['Hobby']), sep = '\n')
print('I dream of being a', (data['Dream']), 'in the future')
