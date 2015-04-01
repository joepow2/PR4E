fname = raw_input("Enter file name: ")
try:
    if len(fname) == 0:
        fname = "mbox-short.txt"
    fhandle = open(fname)
except:
    print 'File cannot be opened:' , fname
    exit()

domian_dic = dict()
for line in fhandle:
    if not line.startswith("From") or line.startswith("From:") : continue
    mail = line.split()[1]
    domain = mail.split("@")[1]
    domian_dic[domain] = domian_dic.get(domain,0) + 1
print domian_dic
