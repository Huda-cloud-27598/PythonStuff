#9.4 Write a program to read through the mbox-short.txt and figure
#out who has sent the greatest number of mail messages. The program looks for 
#'From ' lines and takes the second word of those lines as the
#person who sent the mail. The program creates a Python dictionary that maps 
#the sender's mail address to a count of the number of times they appear in the file. 
#After the dictionary is produced, the program reads through the dictionary using a 
#maximum loop to find the most prolific committer.

from multiprocessing.sharedctypes import Value


fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
handle = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    print(wds)
    for w in wds:
        #idiom retrieve / create/update counter
        di[w] = di.get(w,0) + 1

print(di)


# now we want to find the most commmon word

largest = -1
theword = None
for k,v in di.items():
    if v> largest :
        largest = v
        theword = k

print("done")

        