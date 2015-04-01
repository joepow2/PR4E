fname = raw_input("Enter file name: ")
try:
    if len(fname) == 0:
        fname = "mbox-short.txt"
    fhandle = open(fname)
except:
    print 'File cannot be opened:' , fname
    exit()

email_dic = dict()
for line in fhandle:
    if not line.startswith("From") or line.startswith("From:") : continue
    lst = line.split()
    mail = lst[1]
    email_dic[mail] = email_dic.get(mail,0) + 1

bigCount = None
bigWord = None
for word,count in email_dic.items():
	if bigCount is None or count > bigCount:
		bigWord = word
		bigCount = count

print bigWord,bigCount