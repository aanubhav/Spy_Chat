from datetime import datetime


# Class to record spy details (deafult and new (if made))
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


# Class to record chats
class ChatMessage:

    def __init__(self, message, sent_by_me):
        # Assigning the message
        self.message = message

        # Assigning the timestamp
        self.time = datetime.now()

        # Assigning the sender
        self.sent_by_me = sent_by_me


# declaring a default spy
spy = Spy("James Bond", "Mr. ", 32, 4.2)

# Friends list
friends = [Spy('John Wick', 'Mr.', 35, 4.6), Spy('Jane Bond', 'Ms.', 28, 4.5), Spy('Alec Leamas', 'Mr.', 38, 4.8),Spy('Jack Ryan','Mr.', 33,4.0)]