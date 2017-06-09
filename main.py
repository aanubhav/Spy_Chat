from spy_details import spy,Spy,ChatMessage,friends
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored, cprint

import colorama

STATUS_MESSAGES = ['Busy', 'On a misson', 'AFK','Urgent Calls only','Do not Disturb']
SPECIAL_WORDS = ['SOS', 'SAVE ME','FIRING','KILL','HELP','ALERT','PRESIDENT','MISSILE','CRITICAL','COUP','WAR']
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
			menu_choices = "\nWhat do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
			menu_choice = raw_input(menu_choices)

			if len(menu_choice) > 0:
				menu_choice = int(menu_choice)

				if menu_choice == 1:
					current_status_message = add_status(current_status_message)
					print "updated message :"+current_status_message
				elif menu_choice == 2:
					number_of_friends = add_friend()
					print 'You now have %d friends' % (number_of_friends)
					print "\n"
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


def add_status(current_status_message):
	# initialising varaible
	updated_status_message = None

	#check for current status(if any)
	if current_status_message != None:
		print 'Your current status message is %s \n' % (current_status_message)
	else:
		print 'You don\'t have any status message currently \n'


	default = raw_input("Do you want to select from the older status (y/n)? ")

	if default.upper() == "N":
		new_status_message = raw_input("What status message do you want to set? ")

		if len(new_status_message) > 0:
			STATUS_MESSAGES.append(new_status_message)
			updated_status_message = new_status_message

	elif default.upper() == 'Y':
		#display list of saved status messages
		item_position = 1
		for message in STATUS_MESSAGES:
			print '%d. %s' % (item_position, message)
			item_position = item_position + 1

		#selecting from the saved staus messages		
		message_selection = int(raw_input("\nChoose from the above messages "))


		if len(STATUS_MESSAGES) >= 	message_selection:
			updated_status_message = STATUS_MESSAGES[message_selection - 1]

	else:
		print 'The option you chose is not valid! Press either y or n.'

	if updated_status_message:
		print 'Your updated status message is: %s' % (updated_status_message)
	else:
		print 'You currently don\'t have a status update'

	return updated_status_message


def add_friend():
	# initialising spy object
	friend = Spy('','', 0,0)
	# getting credentials
	friend.name= raw_input("Input a new friend name : ")
	friend.salutation = raw_input("Is new friend Mr. or Ms.  :")
	friend.age = int(raw_input("Input his age  :"))
	friend.rating = float(raw_input("Input his rating  :"))

	# Checking Validity of new friend
	if len(friend.name)>0 and 18<=friend.age<=40 and spy.rating<=friend.rating<=5.0:

		friends.append(friend)
		print "\n"+friend.salutation+" "+friend.name+" with age "+str(friend.age)+" and rating "+str(friend.rating)+" added to your friend\'s list\n"

	else :
		print "This man is not qualified enough to be a friend. \n"	

	return len(friends)	


def send_message():
	friend_choice = select_a_friend()
	#path for file to encode 
	original_image = "input.jpg"
	#path for file which will store message
	output_path = "output.jpg"
	text = raw_input("What do you want to say? ")
	#encoding image
	Steganography.encode(original_image, output_path, text)
	#new object for ChatMessage class
	new_chat = ChatMessage(text,True)
	#adding chat information to chat list(maintained as object to Spy class )
	friends[friend_choice].chats.append(new_chat)
	print "Your secret message image is ready!"

def select_a_friend():
	item_number = 0
	# searching for a friend in friend's list
	for friend in friends:
		print "%d. %s aged %d with rating %.2f is online" % (item_number +1,friend.name,
													friend.age,
													friend.rating)
		item_number = item_number + 1

	# Input friend choice	
	friend_choice = raw_input("Choose from your friends ")

	friend_choice_position = int(friend_choice) - 1
	if friend_choice_position+1 >len(friends):
		print "no such friend found"
		quit()

	else :
		return friend_choice_position

def read_message():
	sender = select_a_friend()
	#path for file to decode
	output_path = "output.jpg"
	#decoding secret text
	secret_text = Steganography.decode(output_path)
	if len(secret_text)>0:
		#new chat object
		new_chat = ChatMessage(secret_text,False)
		#adding chat to chats(maintained in Spy class)
		friends[sender].chats.append(new_chat)

		text = secret_text.split()
		#to keeep track of words spoken by sender
		friends[sender].word_count += len(text)

		#initialize colorama
		colorama.init()
		text1 = (secret_text.upper()).split()
		counter = 0
		for urgent in SPECIAL_WORDS:
			if urgent in text1:
				counter += 1
		if counter>0:
			cprint("Mission CRITICAL !!\nDispatch Support NOW\n",'red')	
			print "%s\'s  message : %s"%(friends[sender].name,secret_text)
		else :
			print "%s\'s  message : %s"%(friends[sender].name,secret_text)
	else :
		print "no message found"				



def read_chat():
	friend_select = select_a_friend()

	for chat in friends[friend_select].chats:
		if chat.sent_by_me == True :
			print "sent by me\n"
			print "Sent at "+chat.time.strftime("%d %B %Y")
			print "message  :"+chat.message
		else :
			print "\nsent by "+friends[friend_select].name
			print "Sent at "+chat.time.strftime("%d %B %Y")
			print "message  :"+chat.message+"\n"




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
