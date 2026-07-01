cost_per_plate = float(input("Enter the cost per plate of the momo: "))
selling_price = float(input("Enter the selling price per plate: "))
plates_sold = int(input("Enter the total number of plates sold: "))

total_revenue = selling_price * plates_sold
total_cost = cost_per_plate * plates_sold
profit = total_revenue - total_cost
profit_margin = (profit / total_revenue) * 100

print(f"Total Revenue Generated: {total_revenue}")
print(f"Total Cost: {total_cost}")
print(f"Total Profit: {profit}")
print(f"Profit Margin: {profit_margin} %")