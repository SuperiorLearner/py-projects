import random

while True:
    computer = random.choice([-1, 0, 1])
    
    try:
        user_choice = input("Enter your choice (s/w/g): ").lower()
        user_dict = {"s": 1, "w": -1, "g": 0}
        user = user_dict[user_choice]
        convert = {1: "Snake", -1: "Water", 0: "Gun"}
        
        print(f"You choose {convert[user]},\nComputer choose {convert[computer]}")
        
        if user == computer:
            print("It's a draw")
        else:
            if (user == 1 and computer == -1) or (user == 0 and computer == 1) or (user == -1 and computer == 0):
                print("You win!")
            else:
                print("You lose!")
                
    except KeyError:
        print("Invalid input! Please enter 's', 'w', or 'g'.")
        continue
    
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
        
#Alternative : This is a shortcut logic taken on the basis of the value computer – user
    # if((computer - user) == -1 or (computer - user) == 2):
    #     print("You lose!")
    # else:
    #     print("You win!")

    