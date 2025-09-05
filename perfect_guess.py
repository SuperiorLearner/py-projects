import random

while True:
    n = random.randint(1, 100)
    a = 1

    print("Welcome to the perfect guess")

    while True:
        try:
            y = int(input("Your guess: "))
            
            if (y < 1 or y > 100):
                print("Enter number between 1-100")
                continue
                
            if (y < n):
                print("Higher number please: ")
                a += 1
            elif (y > n):
                print("Lower number please: ")
                a += 1
            else:
                print(f"Correct! Number was {n}")
                print(f"Attempts: {a}")
                break
                
        except:
            print("Enter valid number!")

    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break


