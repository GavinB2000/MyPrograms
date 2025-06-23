"""
This is a simple banking program I made
It was made by me, Gavin Birk on August 24th 2024 at 9:15PM
This program uses Python loops, functions, and checks to make sure deposit amounts are valid

"""
import random
deposit = float(0)
# Function for creating a username
def username():
# This loop turns the input into uppercase letters (if there are any) and raises an error if the critera isn't met
    while True:
        try:
            username = input("Enter a five digit username: ").upper()
# Critera for username
            if len(username) != 5 or username == "":
                raise ValueError
        except ValueError:
            print("Please enter a username that is 5 characters!\n")
        else:
            print("Your username is accepted \n")
# Break continues the next line
            break
    return username

# Function for creating a password
def password():
#Checks to see if password is alpha numeric, then returns the password or has user recreate one if it doesn't meet the criteria
    while True:
        try:
            password = input("Please enter a password that contains both letters and numbers and that is at least eight digits long: ")
# Criteria for password
            if len(password) < 8 or password.isalnum() == False:
                raise ValueError
        except ValueError:
            print("Password doesn't meet the intended criteria\n")
        else:
            print("Your password is accepted\n")
            break
    return password

#Creates the initial account balance
def initialdeposit():
    while True:
        try:
            initialdeposit = float(input("Enter the initial deposit into your account: $"))
            initialdeposit = round(initialdeposit, 2)
            if initialdeposit <= 0 or float(initialdeposit) == False:
                raise ValueError
        except ValueError:
            print("Invalid deposit, please make sure it's a number greater than 0 and do not add a dollar sign ($) to your deposit \n")
        else:
            print("Initial deposit accepted! \n")
            print(initialdeposit)
            global deposit
            deposit = initialdeposit
            return
        
# Sets username and password functions to variables
username = username()
password = password()
#Calls function to import first deposit for account
initialdeposit()
# Generates a rando account and routing number
accountnumber = random.randint(10000000, 99999999)
routingnumber = random.randint(100000000, 999999999)

print("Your banking account is now set up! \n")

# Allows user to add money to their account
def depositmoney():
# Verifies deposit amount is floating integer and that it's greater than zero
    while True:
        try:
            money = float(input("\nHow much would you like to deposit?"))
            if money <= 0:
                raise ValueError
            elif money > 0:
                global deposit
                deposit = deposit + money
                deposit = round(deposit, 2)
                print("\nYour balance is now: $")
                print(deposit)
                makeselection()
        except ValueError:
            print("Your deposit can not be less than $0 \n")
        else:
            makeselection()

# Allows user to make a withdraw
def withdraw():
# Verifies amount being withdrawn is greater than 0 and less than the total amount in the account
    global deposit
    while True:
        try:
            print("Your current balance is: $ \n")
            print(deposit)
            money = float(input("How much would you like to withdraw? "))
            if money <= 0 or money > deposit:
                raise ValueError
            elif money > 0 and money <= deposit:
                deposit = deposit - money
                deposit = round(deposit, 2)
                print("Your balance is now: $ \n")
                print(deposit)
                makeselection()
        except ValueError:
                print("Your withdraw can not exceed your account balance \n")
        else:
            makeselection()

#Allows user to see their account information
def accountinfo():
    print("\nYour current balance is: $")
    print(deposit)
    print("Your username is: ")
    print(username)
    print("Your password is: ")
    print(password)
    print("Your account number is: ")
    print(accountnumber)
    print("Your routing number is: ")
    print(routingnumber)
    print("\n")
    makeselection()

# Method for all choices in program
def makeselection():
    while True:
        print("\nWelcome to the ATM!")
        print("Press 1 to make a deposit")
        print("Press 2 to make a withdraw")
        print("Press 3 to see your account information")
        print("Press 4 to log out")
        userinput = int(input("Please make a selection "))
        if userinput == 1:
            depositmoney()
        elif userinput == 2:
            withdraw()
        elif userinput == 3:
            accountinfo()
        elif userinput == 4:
            print("Goodbye!")
            quit()
    
    
# Main method that inherits the username and password
def main(username, password):
# Checks and validates username and password
    while True:
        try:
# Sets all letters to uppercase and removes spaces in password
            typedusername = input("\n Welcome to the banking program, please enter your username: ")
            typedusername = typedusername.upper()
            typedusername = typedusername.replace(" ", "")
# Prints error if password isn't correct or is null
            if typedusername != username or typedusername == "":
                raise ValueError
        except ValueError:
            print("Invalid username, please try again \n")
        else:
            break
# See above comments, validates if password is correct
    while True:
        try:
            typedpassword = input("\nPlease enter your password: ")
            typedpassword = typedpassword.replace(" ", "")
            if typedpassword != password or typedpassword == "":
                raise ValueError
        except ValueError:
            print("Invalid password, please try again \n")
        else:
            break
        
## Calls main method
main(username, password)
makeselection()
    
    
         
    
      
    
