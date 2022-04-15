print("\033[91m {}\033[00m".format("\t\t\t\tWelcome to Python Bank ATN","\n"))
restart = ('Y')
chances = 3
balance = 1000

while chances >= 0:
    pin = int(input('\n Please Enter Your 4 digit Pin (Only 3 Tries) :'))
    if pin == (1234):
        print("\033[92m {}\033[00m".format("You Pin is Correct, Welcome!\n"))
        print("\033[93m {}\033[00m".format("\t\t\t\t\tPlease press '1' for your Balance"))
        print("\033[94m {}\033[00m".format("\t\t\t\t\tPlease press '2' To make a Withdrawl"))
        print("\033[95m {}\033[00m".format("\t\t\t\t\tPlease press '3' To Pay In"))
        print("\033[96m {}\033[00m".format("\t\t\t\t\tPlease press '4' To Return Card \n "))


        while chances >= 0:
            option = int(input("What Would you like to Choose?:"))
            if option == 1:
                print("Your Balance is $", balance,'\n')
                back = input('\n'"Would you like go back? (NO/YES) : ")
                if back in ('yes','YES','Y','y'):
                    print("THANK YOU , SEE YOU AGAIN!")
                    break
                elif back in ('no'):
                    option

            elif option == 2:
                withdrawl = float(input("How much Would you like to withdraw?, '10','20','40','60','80','100'"))
                if withdrawl in [10,20,40,60,80,100]:
                    balance = balance - withdrawl
                    print("\n Your balance is now $", balance,'\n')
                    back = input('\n'"Would you like to go back? (NO/YES) : ")
                    if back in ('yes','YES','Y','y'):
                        print("THANK YOU , SEE YOU AGAIN!")
                        break
                    elif back in ('no'):
                        option
                elif withdrawl != [10,20,40,60,80,100]:
                    print('Invalid Command, please enter correct ')

            elif option == 3:
                    pay_in = float(input("How much would you like to pay for you card: "))
                    balance = balance + pay_in
                    print("Your balance is now $", balance,'\n')
                    back = input('\n'"Would you like go back? (NO/YES):   ")
                    if back in ('yes', 'YES', 'Y', 'y'):
                        print("THANK YOU , SEE YOU AGAIN!")
                        break
                    elif back in ('no','NO','No','n'):
                        option

            elif option == 4:
                    print("Please wait till card is returned")
                    print("THANK YOU FOR USING OUR SERVICE")
                    break
            else:
                print("Please enter a correct number")
                restart =('y')

    elif pin != (1234):
        print("Incorrect Password","\n")
        chances = chances-1
        if chances == 0:
            print("\n","You have already tried 3 times, No more Tries")
            break



