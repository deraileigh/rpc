
import random
def rpc() : # rock paper cisor function
  # result variable
  result=""
  # user choice and moves
  moves=["rock","paper","cisor"]
  userchoice = int(input("what is your choice ? 1) rock 2) paper 3)cisor"))
  choice=moves[userchoice-1]
  # computer choice 
  computerchoice=random.choice(moves)
  #comparasion-user choice rock 
  if choice=="rock":
    if computerchoice=="paper": 
      result="computer w"
    elif computerchoice=="cisor":
      result="user w"
    else: 
      result="tie game"
  if choice=="paper":
    if computerchoice=="paper":
      result="tie game"
    elif computerchoice=="cisor": 
      result="computer w"
    else: 
      result="user w"
  if choice=="cisor":
    if computerchoice=="paper": 
      result="user w"
    elif computerchoice=="cisor":
      result="tie game"
    else: 
      result="computer w"

  print(computerchoice)
  return result 





    




