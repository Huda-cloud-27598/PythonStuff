# 8.4 Open the file romeo.txt and 
# read it line by line. For each line, 
# split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to
# see if the word is already in the list and if not append it to the list.
# When the program completes, sort and print the resulting words in alphabetical order.


fname = input("Enter file name: ") # Entering the data
fh = open(fname) #giving python some access 
lst = list() # creates the var turns it into list that will have eveything perfect in terms of directions
#print(lst) # should be empty 
for line in fh: # goes through each line in the file
    line = line.rstrip() #takes away all the whitespace and /n
    words = line.split() # var words is now a list of all the words in the file 
    # print(words)  # should be every word w/o spaces 
    for things in words:  #going though the list of all words now        
        if things not in lst: #puting everything in the empty list - satisfying the req of making sure repeated words dont come up
            lst.append(things) # appending only if not alr there
            lst.sort() #sorting in alphabetic
print(lst) #shuld have right


