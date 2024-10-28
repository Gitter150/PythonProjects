import random

print("\n\nWelcome to the game of Rock, Paper and Scissors.\nRules:\nThere will be 3 rounds.\nIf you win 2 out of the 3 rounds, you win. Otherwise, you lose.")

choices = ['Rock','Paper','Scissors']
win_condition = {
   'Rock':'Scissors',
   'Paper':'Rock',
   'Scissors':'Paper'
}

def get_choice(choices):
   while True:
      x = input("Enter your Choice: ").capitalize()
      if x in choices:
         return x
      else:
         print("Invalid Choice! Enter Rock, Paper or Scissors")

def get_playagain():
   while True:
      x = input("Yes, or No? : ").capitalize()
      if x in {"Yes","No"}:
         return x
      else:
         print("Invalid Choice! Enter either Yes or No")

def startGame(choices, win_condition, wins=0, losses=0):
   for i in range(1,4):
      print(f"\n-------ROUND {i}-------\n")
      UC = get_choice(choices)  #UC = USER CHOICE, CC= COMPUTER CHOICE
      CC = random.choice(choices)
      if win_condition[UC]==CC:
         wins+=1
         print(f"My Choice: {CC}\n\n{UC} beats {CC}, You Win this round!") 
      elif UC == CC:
         print(f"My Choice: {CC}\n\nThat's A Tie!")  
      else:
         losses+=1
         print(f"My Choice: {CC}\n\n{CC} beats {UC}, You Lose this round!")
      print(f"No. Of Wins: {wins} | No. Of Losses: {losses}")
   
   print(f"\nFinal Scores:\nWins: {wins} | Losses: {losses}")
   if wins! = losses:
      print("You Won The Game!" if wins>losses else "You Lost The Game!")
   else:
      print("The match is a draw!")         
   print("\nDo You Wish To Play Again?")
   
   if get_playagain() == "Yes":
      startGame(choices, win_condition, wins, losses)
   else:
      print("\nThanks For Playing! Exiting...")

startGame(choices, win_condition)
