import time
print("Made by Winston Okpalanma. For source code and more info visit https://github.com/wokpalanma2020")
print("Version 2.0")
lose = ("You have lost the bout of Rock Paper Scissors! The computer reigns supreme!")
win = ("Congratulations young grasshopper ... your skills in the art of Rock Paper Scissors has resulted in victory!")
lives = 5
score = 0
drew = 0
computer_lives = 7

password_list = []

while True:
    print("To begin fill in the information below. ")
    username = input("Please enter your username: ")
    password = input("Please eneter your password: ")

    # Looks for account file in directory and reads the information inside with "r" command
    searchFile = open("accounts.txt" , "r")

    for line in searchFile:
        password_list.append(line.strip())
        if username and password in password_list:
            print("Access Granted!")
            time.sleep(.5)
            print("Loading .")
            time.sleep(1)
            print("Loading ..")
            time.sleep(2)
            print("Loading ...")
            time.sleep(3)
            print("Loading Complete!")
            time.sleep(3)
            print("—————————————————————————————————————————————————————————————————————————————————— ")
            print("—————————————————————————————————————————————————————————————————————————————————— ")
            print("	  __                 ___________________       _________________________         _________________________      ________        ____")
            print("	|   |               |                   |     |                         |       |                         |    |        |      /   / ")
            print(" /—————————————-----     |       _____       |     |        __________       |       |         ________________|    |        |     /   / ")
            print("/           \       |    |      |     |      |     |       |          |      |       |        |                     |        |    /   /  ")
            print("|        ————————---     |      |_____|      |     |       |          |      |       |        |                     |        |___/   /  ")
            print("|	    ————————---     |               —-        |       |          |      |       |        |                     |               /  ")
            print("|           \       |    |        | \     \        |       |          |      |       |        |                     |                \ ")
            print("|        ————————---     |        |  \     \       |       |__________|      |       |        |_________________    |        |\       \         ___   ___   ___   ___ ")
            print("|        ————————---     |        |   \     \      |                         |       |                          |   |        | \       \       |   | |   | |   | |   | ")
            print("|           \       |    |________|    \_____\     |_________________________|       |__________________________|   |________|  \_______\      |   | |   | |   | |   | ")
            print("|        ————————---                                                                                                                           |   | |   | |   | |   |  ")
            print(" \       ————————---                                                                                                                      ___  |   | |   | |   | |   | ")
            print("  \         \      /   _____________       _________________       _______________      __________________       ________________        |   | |   | |   | |   | |   | ")
            print("   \————————————--/   |    _____    |     |      ______     |     |     ______    |    |                  |     |                |       |   | |   | |   | |   | |   | ")
            print("                      |   |     |   |     |     |      |    |     |    |      |   |    |        __________|     |      ___       |       |   | |   | |   | |   | |   | ")
            print("                      |   |_____|   |     |     |______|    |     |    |______|   |    |       |                |     |   |      |       |   | |   | |   | |   | |   | ")
            print("                      |     ________|     |      ______     |     |     __________|    |       |_________       |     |___|    _ |        \                          / ")
            print("                      |    |              |     |      |    |     |    |               |        _________|      |              \           \                        / ")
            print("                      |    |              |     |      |    |     |    |               |       |__________      |       |\      \           \                      / ")
            print("                      |    |              |     |      |    |     |    |               |                  |     |       | \      \           \                    /                                                             ____")
            print("                      |____|              |_____|      |____|     |____|               |__________________|     |_______|  \______\           \_________________ /                                                            /    / ")
            print("                                                                                                                                                                                                                           /    / ")
            print("  _____________________        _______________________        _____        _____________________     ______________________       ________________     ______________       ______________________                       /     / ")
            print(" |       ______________|      |                       |      |     |     |        ______________|   |        ______________|     |                |   |              |     |        ______________|     ________       /    /  ")
            print(" |      |                     |       ________________|      |     |     |       |                  |       |                    |      _____     |   |     ___      |     |       |                  /             /     /  ")
            print(" |      |______________       |       |                      |     |     |       |_____________     |       |______________      |     |     |    |   |    |   |     |     |       |_____________    |           /     / ")
            print(" |_______________      |      |       |                      |     |     |_______________      |    |_______________       |     |     |     |    |   |    |___|  __ |     |_______________      |   |         /     / ")
            print("                 |     |      |       |                      |     |                     |     |                    |      |     |     |     |    |   |           \                       |      |   |      /     __________________ ")
            print("                 |     |      |       |_______________       |     |                     |     |                    |      |     |     |_____|    |   |    |\      \                      |      |   |                              | ")
            print("   ______________|     |      |                       |      |     |      _______________|     |     _______________|      |     |                |   |    | \      \       ______________|      |   |             _________________| ")
            print("  |____________________|      |_______________________|      |_____|     |_____________________|    |______________________|     |________________|   |____|  \______\     |_____________________|   |____________| ")
            print(" —————————————————————————————————————————————————————————————————————————————————— ")
            print(" —————————————————————————————————————————————————————————————————————————————————— ")

            print("These are the rules of the ancient art of Rock Paper Scissors ...")
            print("You start with ", lives, " lives")
            print("If you win a bout, you are rewarded an extra life")
            print("If you lose a bout, a life is snatched away!")
            print("If you draw, there is no consequence")
            print("-------------------------------------")
            print("-------------------------------------")
            print("To hear the rules again, simply type: rules")
            print("-------------------------------------")
            print("At any point, type: exit , in order to exit the match")
            print("-------------------------------------")
            print("Your opponent, the computer, has lives as well")
            print("Can you defeat the champion in Rock Paper Scissors??")
            print(" We shall see ... Your bout starts now!")
            print("-------------------------------------")

            while True:
                rps = input("Rock, Paper, or Scissors? ")
                import random
                computer = ("rock", "paper", "scissors")
                computer = random.choice(computer)

                # if statements for rock user input
                if rps.lower() == "rock" and computer == "paper":
                    print("Your opponent has thrown ...", computer, "!")
                    print(lose)
                    lives -= 1
                if rps.lower() == "rock" and computer == "rock":
                    print("Your opponent has thrown ...", computer, "!")
                    print("Equal force has been applied, there is no victor!")
                    drew += 1
                if rps.lower() == "rock" and computer == "scissors":
                    print("Your opponent has thrown ...", computer, "!")
                    print(win)
                    score += 1

                # if statements for paper user input
                if rps.lower() == "paper" and computer == "scissors":
                    print("Your opponent has thrown ...", computer, "!")
                    print(lose)
                    lives -= 1
                if rps.lower() == "paper" and computer == "paper":
                    print("Your opponent has thrown ...", computer, "!")
                    print("Equal force has been applied, there is no victor!")
                    drew += 1
                if rps.lower() == "paper" and computer == "rock":
                    print("Your opponent has thrown ...", computer, "!")
                    print(win)
                    score += 1

                # if statements for scissors user input
                if rps.lower() == "scissors" and computer == "rock":
                    print("Your opponent has thrown ...", computer, "!")
                    print(lose)
                    lives -= 1
                if rps.lower() == "scissors" and computer == "scissors":
                    print("Your opponent has thrown ...", computer, "!")
                    print("Equal force has been applied, there is no victor!")
                    drew += 1
                if rps.lower() == "scissors" and computer == "paper":
                    print("Your opponent has thrown ...", computer, "!")
                    print(win)
                    score += 1

                # System rules
                if rps == "rules" :
                    print("****************************")
                    print("These are the rules of the ancient art of Rock, Paper, Scissors :")
                    print("****************************")
                    print("Rock CRUSHES Scissors, but gets SWAMPED by Paper")
                    print("Scissors SLICES Paper, but gets MAULED by Rock")
                    print("Paper OVERWHELMS Rock, but gets CARVED by Scissors")
                    print("****************************")

                if rps == "display lives":
                    print(lives)
                if rps == "display score":
                    print(score)

                # Lives function
                if lives == 0 or rps == "test":
                    print("You have been bested by the computer and now Artificial Intelligence will proceed to take over all human life !")
                    print("You were able to win ", score, " times against the computer")
                    print("There were ", drew, " times where there was no victor")
                    stop = input("Press enter to exit.")

                    # Import in time library and its functions
                    exit()

                if computer_lives == 0:
                    print("You were able to best the computer! The entire human race thanks you for saving the world! Congratulations!")
                    print("Thank you for playing!")
                    print("You were able to win ", score, " times against the computer")
                    print("There were ", drew, " times where there was no victor")
                    stop = input("Press enter to exit.")

                    
                    time.sleep(900)

                # Exit the game
                if rps == "exit":
                    break

        else:
            print("Your username or password is incorrect. ")
            print("..........................")
