#Pre-defined account balance
balance = 1000.00

# Function to handle ATM withdrawal
def atm_withdrawal():
    global balance  
    
    print(f"Current balance: ${balance:.2f}")
    
    try:
        withdrawal = float(input("Enter withdrawal amount: $"))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return  # Exit the function if input is invalid
    
    if withdrawal > balance:
        print("Insufficient funds.")
    elif withdrawal == balance:
        balance = 0
        print("Balance will be 0.")
    elif withdrawal < balance:
        balance -= withdrawal
        print("Withdrawal successful.")
    
    print(f"New balance: ${balance:.2f}")

# Call the function
atm_withdrawal()
