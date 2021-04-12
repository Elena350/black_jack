
from play import play
money = int(input("How many chips do you have?"))

while money > 0:
  play_bj = input("Let's play? print 'space' for yes or 'n'")
  if play_bj == "n":
    print("You left the game")
    break
  if play_bj == " ":
    money += play()
    print(f"You have {money} chips.") 
  else:
    print("Error. Please print 'space' or 'n'")



 

