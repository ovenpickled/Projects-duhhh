print("Hello and Welcome to the Quiz created by Aryan")
a = input("Please enter your name: ")
print("Is " + a + " the correct name that you have entered?")
playing = input()
score = 0

if playing.lower() != "no":

    print("Okay! I welcome you!")
else:
    input("Enter your name again: ")

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct answer!")
    score = score + 1
else:
    print("wrong Answer!")

answer = input("How many time zones are there in Russia? ")
if answer.lower() == "11":
    print("Correct answer!")
    score = score + 1
else:
    print("wrong Answer!")

answer = input("What’s the capital of Canada? ")
if answer.lower() == "ottawa":
    print("Correct answer!")
    score = score + 1
else:
    print("wrong Answer!")

answer = input("Name the longest river in the world? ")
if answer.lower() == "nile":
    print("Correct answer!")
    score = score + 1
else:
    print("wrong Answer!")

answer = input("How many keys does a classic piano have? ")
if answer.lower() == "88":
    print("Correct answer!")
    score = score + 1
else:
    print("wrong Answer!")

answer = input("Where was the first modern Olympic Games held? ")
if answer.lower() == "athens":
    print("Correct answer!")
    score = score + 1
else:
    print("wrong Answer!")

answer = input("Name Disney’s first film? ")
if answer.lower() == "snow white":
    print("Correct answer!")
    score = score + 1
else:
    print("wrong Answer!")

print("You scored a total of " + str(score) + " points")
print("That is a total of " + str((score/7)*100) + "%")

print("Thank you for participating in the Quiz!")