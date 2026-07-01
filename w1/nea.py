previous_meter = float(input("Enter the previous month meter reading: "))
current_meter = float(input("Enter the current month reading: "))
units_used = current_meter - previous_meter

unit_rate = 13
service_charge = 10
consumption_cost = unit_rate * units_used
total_bill = consumption_cost + service_charge

print(f"Total Bill: {total_bill}")