# Author          : Jefen B. De Villa
# Course and Year : BS Information Technology 2nd Year
# Filename        : devilla_e3.py
# Description     : Command Line Arguments and Branching Statements
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

import sys

first_argument = 0
second_argument = 0

if len(sys.argv) == 3:
	program_name = sys.argv[0]
	first_argument = sys.argv[1] 
	second_argument = sys.argv[2]
else:
	print ('Usage: python3 {program name} <activity or sector> <quarantine classification>')
	exit ()

while True:
	if first_argument.lower() == 'people':
		if second_argument.lower() == 'ecq':
			print ('100% stay at home; Exception for workers in offices or industries permitted to operate')
			exit ()
		elif second_argument.lower() == 'mecq':
			print ('100% stay at home; Restricted movement, only for accessing essential goods and services; Exception for workers in offices or industries permitted to operate; Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home')
			exit ()
		elif second_argument.lower() == 'gcq':
			print ('Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home')
			exit ()
		elif second_argument.lower() == 'mgcq':
			print ('Persons below twenty-one (21) years old, sixty (60) years old and above or those at high risk for contracting the COVID-19 disease are required to stay home')
			exit ()

	elif first_argument.lower() == 'transport':
		if second_argument.lower() == 'ecq':
			print ('No domestic flights, with limited international flights; Public transportation is not allowed; Shuttle services for employees of permitted offices or establishments, as well as point-to-point transport service, granted permission to operate by the government, with healthcare workers and other frontliners given priority')
			exit()
		elif second_argument.lower() == 'mecq':
			print ('No domestic flights, with limited international flights; Controlled inbound flights; No inter-island travel; Public transportation is not allowed; Private transportation such as company shuttles and personal vehicles allowed subject to the guidelines provided by the Department of Transportation (DOTr); Biking and non-motorized transport encouraged')
			exit()
		elif second_argument.lower() == 'gcq':
			print ('Public transport is allowed with strict social distancing; Inter-island travel from GCQ to GCQ allowed with safety protocols.')
			exit()
		elif second_argument.lower() == 'mgcq':
			print ('Public transport is allowed with strict social distancing Inter-island travel from GCQ to GCQ allowed with safety protocols.')
			exit()

	elif first_argument.lower() == 'gatherings':
		if second_argument.lower() == 'ecq': 
			print ('Mass gatherings are not allowed; Only mass gatherings that are essential for the provision of government services or authorized humanitarian activities permitted')
			exit()
		elif second_argument.lower() == 'mecq':
			print ('Highly restricted (maximum of 5); Non-essential work gatherings are prohibited')
			exit()
		elif second_argument.lower() == 'gcq':
			print ('Gatherings are limited to not more than ten (10) persons; Non-essential work gatherings are prohibited')
			exit()
		elif second_argument.lower() == 'mgcq':
			print ('Fifty percent (50%) of the seating or venue capacity for movie screenings, concerts, sporting events, and other entertainment activities, religious services, and work conferences')
			exit()

	elif first_argument.lower() == 'schools':
		if second_argument.lower() == 'ecq': 
			print ('School premises are closed')
			exit()
		elif second_argument.lower() == 'mecq':
			print ('School premises are closed')
			exit()
		elif second_argument.lower() == 'gcq':
			print ('Skeletal workforce permitted in schools; Face-to-face or in-person classes are suspended')
			exit()
		elif second_argument.lower() == 'mgcq':
			print ('Limited face-to-face or in-person classes may be conducted; strict compliance with minimum public health standards and consultations with local government units (LGUs) and guidelines set by the Commission on Higher Education (CHED)')
			exit()

	elif first_argument.lower() == 'work':
		if second_argument.lower() == 'ecq':
			print ('Select industry workers permitted')
			exit()
		elif second_argument.lower() == 'mecq':
			print ('Essential industries permitted to work at full capacity, with others operating at a fifty percent (50%) capacity; Work-from-home and other flexible work arrangements encouraged')
			exit()
		elif second_argument.lower() == 'gcq':
			print ('Alternative work arrangements')
			exit()
		elif second_argument.lower() == 'mgcq':
			print ('Full operating capacity for work in all public and private offices; Alternative work arrangements for persons who are sixty (60) years old and above, or those with other health risks')
			exit()

	elif first_argument.lower() == 'government':
		if second_argument.lower() == 'ecq':
			print ('Skeletal workforce onsite; Work from home arrangements')
			exit()
		elif second_argument.lower() == 'mecq':
			print ('Skeletal workforce onsite; Work from home arrangements')
			exit()
		elif second_argument.lower() == 'gcq':
			print ('Work in all government offices under alternative work arrangements')
			exit()
		elif second_argument.lower() == 'mgcq':
			print ('Work in all government offices under alternative work arrangementsWork in all government offices under alternative work arrangements')
			exit()
	
	else:
		print ('Invalid input')
		exit()
	
	break

print ('Invalid input')
exit()
