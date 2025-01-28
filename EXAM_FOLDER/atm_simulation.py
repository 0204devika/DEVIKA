dct={
    '1234':10000,
    '4567':30000,       # created a dictionary with account number as key and balance as value.
    '7890':250
}
def check_balance(account_number):        #this is the function used to check balance
        if account_number in dct:
            return f"the balance is {dct[account_number]}"
        else:
            return "account not found"
def deposit(account_number,amount):      #this function is used to deposit money                  
    if account_number in dct:
        if amount>0:
            dct[account_number]+=amount
            return f"deposit successful, new balance is {dct[account_number]}"
def withdraw(account_number,amount):        #this function is used to withdraw money from the account
    if account_number in dct:
        if amount>0:
            if dct[account_number]>=amount:
                dct[account_number]-=amount
                return f"withdrawal successful, new balance is {dct[account_number]}"
            else:
                return "insufficient funds"
while True:
    print("1. Check Balance")                #these are the four choices, that user can select
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        account_number = input("Enter your account number: ")
        print(check_balance(account_number))
    elif choice == 2:
        account_number = input("Enter your account number: ")
        amount = int(input("Enter the amount to deposit: "))
        print(deposit(account_number,amount))
    elif choice == 3:
        account_number = input("Enter your account number: ")
        amount = int(input("Enter the amount to withdraw: "))
        print(withdraw(account_number,amount))
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please choose a valid option.")

        
    
        
