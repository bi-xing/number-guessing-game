import random

# to be revamped with other features, like:
# A. guess hints for higher/lower guesses
# B. a guess counter (like 3 guesses left)

def end_game(number,won):
    if won:
        print(f"\nCongrats, you got the right number, it was {number}.")
    else:
        print(f"\nYou ran out of guesses /(ㄒoㄒ)/~~, it was {number}.")

    print("\nWould you like to play again? (Y/N)")
    while True:
        play_again=input("\nInput: ")
        if play_again.upper()=="Y":
            return "Y"
        elif play_again.upper()=="N":
            print("\nThank you for using the program.")
            exit()
        else:
            print("\nInvalid input, please try again.")

def main():
    print("Welcome to the Number Guessing Program.\n")
    print("The program will choose a number and you must guess that number.\n")
    print("If you would like to exit the program, please type 'Exit', thank you.\n")

    print("Choose your difficulty:\n")
    difficulties={
        "1": "Easy (1-10, 1 guess)",
        "2": "Medium (1-50, 5 guesses)",
        "3": "Hard (1-100, 10 guesses)",
        "4": "Impossible (1-1000, 1 guess)",
        "5": "Custom"
    }
    for difficulty_num,difficulty_text in difficulties.items():
        print(f"{difficulty_num}. {difficulty_text}\n")

    while True:
        difficulty=input("\nEnter the number corresponding to your difficulty level: ")
        if difficulty=="1":
            number=random.randint(1,10)
            print("\nThe number has been chosen, you may guess once.")
            while True:
                try:
                    answer=int(input("\nEnter your guess: "))
                    break
                except ValueError:
                    print("\nInvalid input, please enter a number.")
            if answer==number:
                end_game(number,True)
            else:
                end_game(number,False)

        elif difficulty=='2':
            number=random.randint(1,50)
            store=""
            print("\nThe number has been chosen, you may guess 5 times.")
            for i in range(5):
                while True:
                    try:
                        answer=int(input("\nEnter your guess: "))
                        break
                    except ValueError:
                        print("\nInvalid input, please enter a number.")
                if answer==number:
                    store=end_game(number,True)
                    break
                else:
                    print("\nWrong guess, try again.")
                    continue
            if store.upper()!="Y":
                end_game(number,False)

        elif difficulty=='3':
            number=random.randint(1,100)
            store=""
            print("\nThe number has been chosen, you may guess 10 times.")
            for i in range(10):
                while True:
                    try:
                        answer=int(input("\nEnter your guess: "))
                        break
                    except ValueError:
                        print("\nInvalid input, please enter a number.")
                if answer==number:
                    store=end_game(number,True)
                    break
                else:
                    print("\nWrong guess, try again.")
                    continue
            if store.upper()!="Y":
                end_game(number,False)
        
        elif difficulty=='4':
            number=random.randint(1,1000)
            print("\nThe number has been chosen, you may guess ONLY ONCE, no second chances.")
            while True:
                try:
                    answer=int(input("\nEnter your guess: "))
                    break
                except ValueError:
                    print("\nInvalid input, please enter a number.")
            if answer==number:
                end_game(number,True)
            else:
                end_game(number,False)

        elif difficulty=='5':
            custom=int(input("\nEnter the maximum number for your guessing range: "))
            number=random.randint(1,custom)
            print("\nThe number has been chosen, you may guess as many times as you want.")
            while True:
                answer=input("\nEnter your guess: ")
                if answer.lower()=="return":
                    print(f"\nThe number was {number}. Returning to the main menu.")
                    break
                try:
                    answer=int(answer)
                except ValueError:
                    print("\nInvalid input, please enter a number.")
                    continue
                if answer==number:
                    end_game(number,True)
                    break
                else:
                    print("\nWrong guess, try again, or type 'return' to go back to the main menu.")
                    continue

        elif difficulty.lower()=="exit":
            print("\nThank you for using the program.")
            exit()
        else:
            print("\nInvalid input, please try again.")
            continue
        continue

main()
