from rockpapercisor import rpc
def winner() :
  userwin=0
  computerwin=0
  while userwin<2 or computerwin<2:
    result=rpc()
    if result=="user w":
      userwin=userwin+1 
    else:
      computerwin=computerwin+1
  if userwin==2:
     winner="user win"
  else:
      winner="computer win"
      
  return winner
print (winner())