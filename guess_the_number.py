from random import randint


print("Welcome to the Game of Guess The Number!")
def guessnum():                                                             
    def get_difficulty():                  
        while True:
            difficulty = input("Enter the difficulty of the game: ").lower().replace(" ", "")
            difficulties = {"easy", "hard", "normal"}
            if difficulty in difficulties:
                return difficulty
            else:
                print("Invalid Input. Enter (easy) or (normal) or (hard)")
        
    difficulty = get_difficulty()

    match difficulty:
        case "easy":
            number_of_attempts = 10
            max_num = 50
        case "normal":
            number_of_attempts = 5
            max_num = 100
        case "hard":
            number_of_attempts = 5
            max_num = 200
            
    r = randint(1 , max_num + 1)
    def getnatnum():
        while True:
            try:
                n = int(input("Enter your Guess: "))
                if 1 <= n <=max_num :
                    return n
                else:
                    print(f"Enter only a natural number (between 1 and {max_num}).")
            except ValueError:
                print("Enter only a natural number (an integer).")

    def game(count = 1):
        if count == number_of_attempts + 1:
            print("You Ran Out of Attempts. Better luck next time!")
            return 0
        choice = getnatnum()
        
        if choice == r:
            print(f"You guessed it right! I had chosen the number {r}")
            print(f"Number of trials: {count}! (not factorial)")
        else:
        
            diff = abs(r - choice)
        
            if diff > 20:
                if r > choice:
                   print("Too low!")
                else:
                   print("Too high!")
            elif diff <= 10:
                if r > choice:
                   print("Very Close! Try a Higher Number")
                else:
                   print("Very Close! Try a Lower Number")
            elif diff <= 20:
                if r > choice:
                   print("A bit low!")
                else:
                   print("A bit high!")
        
        
            print(f"Number of attempts remaining: {number_of_attempts-count}")
            print("However, you can try again!" if number_of_attempts-count>0 else "")
            
            game(count + 1)

    game()
    print("Do you want to play once again?")
    def get_decision():                  
        while True:
            decision = input("Yes or No? : ").lower().replace(" ", "")
            decisions = {"no", "yes"}
            if decision in decisions:
                return decision
            else:
                print("Invalid Input. Enter (easy) or (normal) or (hard)")
    decision=get_decision()
    match decision:
        case "yes":
            guessnum()
        case "no":
            print("Have a Nice Day.")
guessnum()




                                      