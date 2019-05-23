#Attention users Imput required
#Starting balance is $500.25
# type 'B' for balance
# type 'W' to withdraw amd type amount you wish to withdraw
# type 'D' to deposit amd then amount

#starting balance that the whole script will pull from 
account_balance = float(500.25)
#print statement to show th starting balance
def printbalance():
  print("Your current balance: %2g" % account_balance)
#function to add more to current balance
def deposit():
    #User input for the amount they would like to deposit, adding to the current balance
  deposit_amount = float(input()) 
  balance = account_balance + deposit_amount
  #manage after decimal cout using %.2f
  print('Deposit was $%.2f, current balance is $%2g' %(deposit_amount, balance))

#function to subtract from current balance
def withdraw():
    #user input for the withdrawal amount, subtracting from the current balance
  withdrawal_amount = float(input())
  if(withdrawal_amount > account_balance):
    print("$%.2f is greater than your account balance of $%.2f\n" %(withdrawal_amount, account_balance))  
  else: 
    balance = account_balance - withdrawal_amount
    print("Withdrawal amount was $%.2f, current balance is $%.2f" % (withdrawal_amount, balance))

#user input that dictates whether it is a Withdrawal, Depost, or Balance check
userchoice = input ("What would you like to do? \n")
# utilize if, elif, and else statements to use the withdraw, deposit, and print balance functions
if (userchoice == 'D'):
  print('How much would you like to deposit today?')
  deposit ()
elif (userchoice == 'W'):
  print('How much would you like to withdraw today?')
  withdraw()
elif (userchoice == 'B'):
  printbalance()
else:
  print('Thank you for banking with us.')
