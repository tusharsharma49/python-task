import os
os.system('tput setab 6')
os.system('tput setaf 7')
print('\n\t\t\tWelcome to my page\n\t*******************************************************')

while True:
	print('\n\n\t\tPress 1: for basic Linux Commands\n\t\tPress 2: Hadoop Setup\n\t\tPress 3: For Exit')
	c1 = int(input('enter your choice: '))

	if c1 == 1:
		print('Entering setup for basic linux commands......\n\n\tPress 1: for Date & Time\n\tPress 2: for Calender')
		c2 = int(input('Enter your Choice for date or calander: '))
		
		if c2 == 1:
			print('\nRunning Date command.....\n\nYour Date and Time is:')
			os.system('date')
		elif c2 == 2:
			print('\nRunning cal Command......\n\nHere is your Calander')
			os.system('cal')
		else:
			os.system('tput setaf 1')
			print('enter correct number')
			os.system('tput setaf 7')

	elif c1 == 2:
		print('Initializing Hadoop setup.......\n')
		os.system('tput setaf 3')
		print('press 1: to Install Hadoop\npress 2: Modify Hadoop')
		c3 = int(input('Enter your choice : '))
		if c3 == 1:
			print('Initializing Hadoop installation.......\n\tSearching for hadoop package.....')
			os.system('./install.sh')
		elif c3 == 2:
			print('Modifying hadoop......\npress 1: to add a new file to hadoop\nPress 2: for see an uploaded file\nPress 3: to get report')
			c4 = int(input("\tEnter your choice:"))
			if c4 == 1:
				os.system('./modify.sh 1')
			elif c4 == 2:
				os.system('./modify.sh 2')
			elif c4 == 3:
				os.system('./modify.sh 3')
		else:
			print('Enter correct number')
		os.system('tput setaf 7')

	elif c1 == 3:
		break	


	else:
		os.system('tput setaf 1')
		print('enter correct number')
		os.system('tput setaf 7')
os.system('tput init')