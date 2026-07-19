balance = 45000
daily_withdrawn = 10000
amount = 5500

# 1. Check if the amount is a multiple of 500
if amount % 500 != 0:
    print("Invalid amount. Must be a multiple of NPR 500.")

# 2. Check daily limit
elif daily_withdrawn + amount > 50000:
    print("Daily withdrawal limit reached.")

# 3. Check account balance
elif amount > balance:
    print("Insufficient balance.")

# 4. If all rules pass, execute withdrawal
else:
    balance = balance - amount
    print("Withdrawal successful.")
    print(f"Your current balance after withdrawal: NPR {balance}")