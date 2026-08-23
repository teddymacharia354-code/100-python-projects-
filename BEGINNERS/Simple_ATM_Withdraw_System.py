bbalance = float(1000)  # any amount
initial_transactions = 0
transaction_limit = 3
out_of_transactions = False
while True:
    try:
        withdraw_amount = float(input("Enter the amount you wish to withdraw:"))
        break
    except:
        print("Invalid characters,try again!")
print("You are about to withdraw $", withdraw_amount)
while True:
    confirm_withdrawal = input("are you sure you would like to withdraw $" + str(withdraw_amount) + " Yes/No:").upper()
    if confirm_withdrawal == "YES".upper():
        new_balance = (balance - withdraw_amount)
        print("your new balance is $", new_balance)
        break
        initial_transactions += 1
        
    else:
        print("Withdrawal cancelled")

if initial_transactions < transaction_limit:
    print("Do you want to make another transaction?")
    another_transaction = input("Yes/No:").upper()
    if another_transaction == "YES":
        while True:
            
            try:              
               withdraw_amount2 = float(input("Enter the amount you wish to withdraw:"))
               break
            except:
               print("Invalid characters,try again!")
        print("You are about to withdraw $",withdraw_amount2)
        while True:
           confirm_withdrawal2 = input("are you sure you would like to withdraw $" + str(withdraw_amount2) + " Yes/No:").upper()
           if confirm_withdrawal2 == "YES".upper ():
                new_balance2 = (balance - withdraw_amount)
                print("your new balance is $", new_balance2)
                break
           else:
                print("Withdrawal cancelled")
    else:
        print("Have a nice day")
        exit()
elif initial_transactions == transaction_limit:
    print("You are out of transactions, try again tomorrow")
    exit()

  