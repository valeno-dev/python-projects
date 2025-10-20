import random

def compare(x, y):
    #tie
    if x == y:
        return "It's tie 👏"
    
    else:
        #win
        if (x == "r" and y == "s") or (x == "p" and y == "r") or (x == "s" and y == "p"):
            return "You win 🥇"
        
        #lose
        elif (x == "r" and y == "p") or (x == "p" and y == "s") or (x == "s" and y == "r"):
            return "You lose 😢"



def rock_papper_scissors():
    object = ["r", "p", "s"]
    bot_choice = random.choice(object)
    user_input = input("\nChoose Rock(R)/ Papper(P)/ Scissors(S): ").lower()
    
    result = compare(user_input, bot_choice)
    print(f"\n{result}, user: ({user_input.upper()}), bot: ({bot_choice.upper()})\n")


rock_papper_scissors()