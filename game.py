import random

def check(comp,user):
  if comp==user:
    return "Draw"
  elif comp==0 and user ==1:
    return "You WON"
  elif comp==0 and user ==2:
    return "You LOSS"
  elif comp==1 and user==0:
    return "You LOSS"
  elif comp==1 and user==2:
    return "You WON"
  elif comp==2 and user==0:
    return "YOU WON"
  elif comp==2 and user ==1:
    return "You LOSS"


user=int(input('''Enter a number 
if Rock==0 or paper ==1 or sessior ==2 :'''))
comp=random.randint(0,2)
print("The your choice is {} and computer choice is {}".format(user,comp))
print(check(comp,user))
