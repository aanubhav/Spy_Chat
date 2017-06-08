from spy_details import spy

def spy_reception(name):
	if spy.rating > 4.5:

		print "I\'ve heard stories  they can\'t all be true\n"

	elif 3.5 <= spy.rating <= 4.5:

		print " The man. The myth. The legend , welcome "+name

	elif 2.5 <= spy.rating <= 3.5:

		print "You are an average grunt spy"

	else:

		print "You are a poor meatshield better buy a body armour :)"

	print "Welcome. You are now online!"

	# print "Your name is " + spy.name + "\nYour age is " + str(spy.age) + "\nYour rating is " + str(spy.rating)

	print "Your name is %s\nYour age is %d\nYour rating is %f" % (spy.name, spy.age, spy.rating)


print "Hello! Let\'s get started\n"
print "Welcome to SpyTalks \n "
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)
if existing == 'N' or 'n':
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
		print "Login Failure \nRun the program again !"

	spy.age = int(raw_input("Input your age\n"))

	spy.rating = float(raw_input("Input your spy rating.\n"))

	if 18 < spy.age <= 40  and 0.0 <= spy.rating <= 5.0:

		print "Welcome to the SpyTalks - a community to share your experience with fellow spies"

		spy_reception(temp)

		start_chat()

	else:

		print "You're not eligible according to the information provided. Please try again!"	