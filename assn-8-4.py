fname = raw_input("Enter file name: ")
try:
    if len(fname) == 0:
        fname = "romeo.txt"
    fhandle = open(fname)
except:
    print 'File cannot be opened:' , fname
    exit()

lst = list()
for line in fhandle:
	split_line = line.rstrip().split()
	for word in split_line:
		if word not in lst:
			lst.append(word)
	lst.sort()

print lst