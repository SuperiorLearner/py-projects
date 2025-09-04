import random

computer = random.choice([-1,0,1])
user_choice = input("Enter your choice (s/w/g) : ").lower()

user_dict = {"s":1, "w":-1, "g":0}
user = user_dict[user_choice]
convert = {1:"Snake", -1:"Water", 0:"Gun"}

print(f"You choose {convert[user]},\nComputer choose {convert[computer]}")

if(user_choice == computer):
    print("It's a draw")
else:
    if(user == 1 and computer == -1):
        print("You win!")
    elif(user == -1 and computer == 1):
        print("You lose!")
    elif(user == 0 and computer == 1):
        print("You win!")
    elif(user == 1 and computer == 0):
        print("You lose!")
    elif(user == -1 and computer == 0):
        print("You win!")
    elif(user == 0 and computer == -1):
        print("You lose!")
    else:
        print("Something went wrong")
    
#Alternative : This is a shortcut logic taken on the basis of the value computer – user
    # if((computer - user) == -1 or (computer - user) == 2):
    #     print("You lose!")
    # else:
    #     print("You win!")