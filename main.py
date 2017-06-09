from spy_details import spy

STATUS_MESSAGES = ['Busy', 'On a misson', 'AFK','Urgent Calls only','Do not Disturb']

def spy_reception(name):
	if spy.rating > 4.5:

		print "I\'ve heard stories  they can\'t all be true\n"

	elif 3.5 <= spy.rating <= 4.5:

		print "The man. The myth. The legend , welcome "+name+"\n"

	elif 2.5 <= spy.rating <= 3.5:

		print "You are average,better get trained again"+"\n"

	else:

		print "How do you continue being a spy in the first place"+"\n"

	print "Welcome. You are now online!\n"

	print "Your name : %s\nYour age : %d\nYour rating : %1.1f" % (spy.name, spy.age, spy.rating)
	print "\n"

def start_chat(spy_name, spy_age, spy_rating):

	current_status_message = None
	if spy_age > 18 and spy_age < 40:

		#print "Authentication complete. Welcome " + spy_name + " age: " + str(spy_age) + " and rating of: " + str(spy_rating) + " Proud to have you onboard"

		show_menu = True

		while show_menu:
			menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
			menu_choice = raw_input(menu_choices)

			if len(menu_choice) > 0:
				menu_choice = int(menu_choice)

				if menu_choice == 1:
					current_status_message = add_status()
					print "updated message :"+current_status_message
				elif menu_choice == 2:
					number_of_friends = add_friend()
					print 'You have %d friends' % (number_of_friends)
				elif menu_choice == 3:
					send_message()
				elif menu_choice == 4:
					read_message()
				elif menu_choice == 5:
					read_chat()    
				else:
					show_menu = False
	else:
		print 'Sorry you are not of the correct age to be a spy'	


def add_status():
	# method to display statuses
	print spy.current_status

	default = (raw_input("Do you want to select from the old statuses (Y/N)?:\n")).upper()

	if default.upper() == "N":

		new_status_msg = raw_input("Set a new status message\n")

		if len(new_status_msg) > 0:

			spy.current_status = new_status_msg
			# Appending new status to status list
			STATUS_MESSAGES.append(new_status_msg)

		else:

			print "Invalid Status Message!"

	elif default.upper() == "Y":
		item_pos = 1
		# default statuses
		for status in STATUS_MESSAGES:
			print "%d. %s" % (item_pos, status)

			item_pos = item_pos + 1

		msg_choice = int(raw_input("Enter the status index of you choice :\n"))

		# Update current status
		spy.current_status = STATUS_MESSAGES[msg_choice - 1]

	else:
		print "Wrong choice!"
		quit()

	return spy.current_status




# execution begins
print "Hello! Let\'s get started\n"
print "Welcome to SpyTalks \n "
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
answer = (raw_input(question)).upper()

if answer == 'Y':
	spy_reception(spy.name)
	start_chat(spy.name,spy.age,spy.rating)

else :
	spy.name = raw_input("Input your name?\n")

	spy.age = 0

	spy.rating = 0.0

	spy.spy_is_online = False

	#length of spy's name
	string_length = len(spy.name)

	# Condition Check if name entered

	if string_length > 0:

		spy.salutation = raw_input("Should I call you Mr. or Ms.\n")

		spy.name = spy.salutation + " " + spy.name
		temp = spy.name#temporary variable to pass information to method spy_reception()

		print "Hello " + spy.name + "!"
	else:
		print "Login Failure \nEnter a  name !"

	spy.age = int(raw_input("Input your age\n"))

	spy.rating = float(raw_input("Input your spy rating.\n"))

	if 18 < spy.age <= 40  and 0.0 <= spy.rating <= 5.0:

		print "Welcome to the SpyTalks - a community to share your experience with fellow spies"

		spy_reception(temp)

		start_chat(temp,spy.age,spy.rating)

	else:

		print "Error Try Again !"	
