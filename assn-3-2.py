try:
    str_hours = raw_input("Enter Hours:")
    hours = float(str_hours)
    str_rate = raw_input("Enter Rate:")
    rate = float(str_rate)
except:
    print "Error, please enter numeric input"
    quit()

if hours > 40:
    pay = (40*rate) + ((hours-40) * rate*1.5)
else:
    pay = hours * rate

print pay