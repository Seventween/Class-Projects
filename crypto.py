""" crypto.py
    Implements a simple substitution cypher
"""
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"
def menu():
  print("Super Secret Menu!")
  print("0) Quit")
  print("1) Encode")
  print("2) Decode")
  print("What is your choice? \n")
  response = input()
  return response
def encode(plain):
  plain = plain.upper()
  encode = ""
  for x in plain:
    counter = 0
    for y in alpha:
      if (x == y):
        encode+=(key[counter:(counter+1)])
      else:
        counter+=1
  return encode
def decode(coded):
  coded = coded.upper()
  deco = ""
  for z in coded:
    count = 0
    for i in key:
      if (z == i):
        deco+=(alpha[count:(count+1)])
      else:
        count+=1
  return deco
      
  
def main():
  keepGoing = True
  while keepGoing:
    response = menu()
    if response == "1":
      plain = input("\ntext to be encoded: ")
      print(encode(plain))
      print("\n")
    elif response == "2":
      coded = input("\ncode to be decyphered: ")
      print (decode(coded))
      print("\n")
    elif response == "0":
      print ("Thanks for doing secret spy stuff with me.")
      keepGoing = False
    else:
      print ("I don't know what you want to do...")