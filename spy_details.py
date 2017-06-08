from datetime import datetime


# Contains spy class and details of default spy
class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name

        self.age = age

        self.salutation = salutation

        self.rating = rating

        self.spy_is_online = True

        self.chats = []

        self.current_status = None

        self.word_count = 0


# A class for chat messages
class ChatMessage:

    def __init__(self, message, sent_by_me):
        # Assigning the message
        self.message = message

        # Assigning the timestamp
        self.time = datetime.now()

        # Assigning the sender
        self.sent_by_me = sent_by_me



# declaring a default spy
spy = Spy("James Bond", "Mr. ", 22, 4.0)

# Making a friends list




friends = [Spy('Akshay', 'Mr.', 27, 4.9), Spy('Jane Baeur', 'Ms.', 21, 4.39), Spy('Who', 'Dr.', 37, 4.95)]