first_contribution = float(input("Enter first person's contribution amount: "))
second_contribution = float(input("Enter second person's contribution amount: "))
third_contribution = float(input("Enter third person's contribution amount: "))

total_expense = first_contribution + second_contribution + third_contribution
share_per_person = total_expense / 3

print(f"Total Trip Expense: {total_expense}")
print(f"Each person has to contribute: {share_per_person}")
print(f"First person has contributed {first_contribution - share_per_person}")
print(f"Second person has contributed {second_contribution - share_per_person}")
print(f"Third person has contributed {third_contribution - share_per_person}")