str_hours = raw_input("Enter Hours:")
str_rate = raw_input("Enter Rate:")

hours = float(str_hours)
rate = float(str_rate)

if hours > 40:
    pay = (40*rate) + ((hours-40) * rate*1.5)
else:
    pay = hours * rate

print pay