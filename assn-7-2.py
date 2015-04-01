# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
try:
    if len(fname) == 0:
        fname = "mbox-short.txt"
    fhandle = open(fname)
except:
    print 'File cannot be opened:' , fname
    exit()
    
total = 0
count = 0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(":")
    number = line[pos+1:]   
    number = float(number)
    
    count = count + 1
    total = total + number
    average = total / count
    
print "Average spam confidence:" , average
