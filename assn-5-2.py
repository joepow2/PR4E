largest = None
smallest = None

while True:
    str_num = raw_input('Enter a number: ') 
    try:
        if str_num == 'inf' or str_num == '-inf' or str_num == 'nan':
            print 'Invalid input'
            continue
        elif str_num == 'done':
            break
        else:
            num = int(str_num)
            if smallest is None or largest is None:
                smallest = num
                largest = num
            elif largest < num:
                largest = num
            elif smallest > num:
                smallest = num  
    except:
        print 'Invalid input'
        
print "Maximum is" , largest
print "Minimum is" , smallest 