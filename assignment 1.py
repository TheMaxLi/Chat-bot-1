# a simple chat bot with questions and responses
# for computer science 10


import random

input1 = input("how was your day?")
response = ["sounds good, lets get something to eat", "alright lets have some fun then", "boring, mine was cooler"]
print (random.choice(response))

input2 = input("where do you want to go?")
response2 = ["okay lets go!", "i don't want to go there sorry", "good place!"]
print (random.choice(response2))

input3 = input ("what places do you like?")
response3 = ["terrific!", "me too", "how did you find that place?"]
print (random.choice(response3))
