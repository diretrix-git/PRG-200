usd_amount = float(input("Enter earned amount in USD: "))
exchange_rate = 150
service_rate = float(input("Enter the service rate: "))

nrp_amount = usd_amount * exchange_rate
deduction = (service_rate / 100) * nrp_amount
net_amount = nrp_amount - deduction

print(f"Actual earning in NRP: {nrp_amount}")
print(f"Deduction: {deduction}")
print(f"You will receive: {net_amount}")

yearly_gross = nrp_amount * 12
yearly_deduction = deduction * 12
yearly_net = yearly_gross - yearly_deduction

print(f"Total one year deduction: {yearly_deduction}")
print(f"Total one year receiving amount: {yearly_net}")