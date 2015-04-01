count = 0
total = 0

while True:
    str_num = raw_input('Enter a number: ') 
    try:
        if str_num == 'inf' or str_num == '-inf' or str_num == 'nan':
            print 'Invalid input'
            continue
        elif str_num == 'done':
            break
        else:
            num = float(str_num)
            count = count + 1
            total = total + num 
    except:
        print 'Invalid input'
print "Total:" , total
print "Count:" , count        
print "Average:" , total/count