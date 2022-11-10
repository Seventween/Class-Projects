# Blackbelt Version

# Need to import os in order to make/use our cls().
import os

# Defining cls() function.
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

# Declaring variables and list with the extra jokes.
# Variable x is going to be used as an iterator.
x = 1
jokelist= ["What is the most used language in programming? \nProfanity.", "Why did the programmer quit his job? \nBecause he didn't get array.", "What did the Jave code say to the C code? \n You've got no class!", "What is an algorithm? \nA word used by programmers when they don't want to explain what they did.", "If 0 is false, then 1 is true, right? \n1."]
print("Hello, can I get your name please?")
# Storing user input and assinging it to a variable to call later.
name = input()
# Calling the variable in a print statement.
print("\nNice to meet you " + name)
# Next few lines are printing the first joke, with added input that serves no real purpose, just for the program to seem more interactive.
print("I'm going to tell you a knock knock joke! \n")
print("Knock knock.. \n")
content = input()
print(".........")
print("\n .....")
print("\n ....")
print("\n..Java. \n")
print ("Would you like to hear another joke?\n")
# This will decide if the program continues, or ends here.
content = input()
# If statement containing what happens if user enters yes.
if content == "yes" or content == "Yes" or content == "YES":
  # cls() used to clear the console.
  cls()
  print("\n Awesome! \n")
  # Accessing the list for the first time.
  print(jokelist[0])
  print("\nWould you like to hear another joke? \n")
  content = input()
  # Another chance to end the program, using user input.
  if content == "yes" or content == "Yes":
    # For loop to access the rest of the list.
    for x in range(4):
      x+=1
      print ("\n")
      print(jokelist[x])
      print("\nWould you like to hear another joke?\n")
      content = input()
      # If statement here is used to check if program should be finishing.
      if x == 4:
        # Console clear again to appear more seamless.
        cls()
        print("\nThat's all! Thanks for playing!\n")
      # If else statement used to check if accessing the list should continue.
      if content == "No" or content == "no":
        # Break statement used to exit the loop.
        break
      else:
        # Loop will continue until finished or user enters no.
        continue

 # Closing statement, and clearing the console one more time.
cls()
print("\n Thanks for playing! \n")