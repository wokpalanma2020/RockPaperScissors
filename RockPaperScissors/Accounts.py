print("----------------------------")
print("Rock, Paper, Scissors Account information and setup")
print("Version 2.0")
print("----------------------------")

while True:
    username = input("Pick a username: ")
    password = input("Pick a password: ")
    password_confirm = input("Please confirm your password: ")

    if password != password_confirm :
        print("Your passwords do not match. Please enter it again.")

    if password == password_confirm:
        print("Your account has been made and verified!")
        # Open function parameter ,a, will append text to the inputted file
        text_file = open("accounts.txt", "a")

        # Python functions for writing text to documents. This writes the users account info to the specified document
        text_file.write("\n")
        text_file.write(username)
        text_file.write("\n")
        text_file.write(password)
        text_file.close()
        break
