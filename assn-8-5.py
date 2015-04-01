fname = raw_input("Enter file name: ")
try:
    if len(fname) == 0:
        fname = "mbox-short.txt"
    fhandle = open(fname)
except:
    print 'File cannot be opened:' , fname
    exit()

count = 0
for line in fhandle:
    if not line.startswith("From") or line.startswith("From:") : continue
    count = count + 1
    lst = line.split()
    email = lst[1]
    print email

print "There were", count, "lines in the file with From as the first word"