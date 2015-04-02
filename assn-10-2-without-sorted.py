#Without bulit-in function sorted() in tuple

fname = raw_input("Enter file name: ")
try:
    if len(fname) == 0:
        fname = "mbox-short.txt"
    fhandle = open(fname)
except:
    print 'File cannot be opened:' , fname
    exit()

dic = dict()
for line in fhandle:
    if not line.startswith("From") or line.startswith("From:") : continue
    time = line.split()[5]
    hour = time.split(":")[0]
    dic[hour] = dic.get(hour,0) + 1

lst = list()
for key, val in dic.items():
	lst.append( (key,val))

lst.sort()

for k, v in lst:
	print k , v 