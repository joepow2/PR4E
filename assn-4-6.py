def computepay(h,r):
    if h > 40:
        p = (40*r) + ((h-40) * r*1.5)
    else:
        p = h * r

    return p

str_hours = raw_input("Enter Hours:")
try:
    hours = float(str_hours)
except:
    print 'Error, please enter numeric input'
    exit()
    
str_rate = raw_input("Enter Rate:")
try:
    rate = float(str_rate)
    
    print computepay(hours,rate)
    
except:
    print 'Error, please enter numeric input'
    exit()

