purchase_amount = 6000
is_loyalty_member = True

# Determine the base discount percentage
if purchase_amount < 1000:
    discount_pct = 0.0
elif purchase_amount < 5000:
    discount_pct = 0.05
elif purchase_amount < 15000:
    discount_pct = 0.10
else:
    discount_pct = 0.20

# Calculate amount after the initial discount
discounted_amount = purchase_amount * (1 - discount_pct)

# Apply extra 5% loyalty discount on the remaining amount if applicable
if is_loyalty_member:
    final_amount = discounted_amount * 0.95
else:
    final_amount = discounted_amount

print(f"Final payable amount: NPR {final_amount:.2f}")