import random
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#cls()
loop = True
go = True
count = 0
low = 1
high = 100
check = ""
print("Please think of a number between 1 and 100. I will try to guess it, and 
you'll let me know if I'm too high, low, or correct!")
print("\nFor this game, please enter your responses using h, l, or c.\n")
guess = random.randint(low,high)
print("I guess: ",guess,"\n")
while(go):
  while(loop):
    answer = input()
    if(answer == "h" or answer == "H"):
      count+=1
      high = guess
      high-=1
      guess = random.randint(low,high)
      print("I guess: ",guess,"\n")
    elif(answer == "l" or answer == "l"):
        count+=1
        low = guess
        low+=1
        guess = random.randint(low,high)
        print("I guess: ",guess,"\n")
    elif(answer == "c" or answer == "C"):
      print("\nI got it! It took me: ",count," tries!\n")
      print("\nWould you like to play again?")
      check = input()
      if(check == "yes" or check == "Yes"):
        cls()
        print("Please think of a number between 1 and 100. I           will try to 
guess it, and you'll let me know if I'm            too high, low, or correct!")
        print("\nFor this game, please enter your responses            using h, l, 
or c.\n")
        guess = random.randint(low,high)
        print("I guess: ",guess,"\n")
        
        continue
      else:
        cls()
        print("\nThanks for playing!")
        go = False
        break