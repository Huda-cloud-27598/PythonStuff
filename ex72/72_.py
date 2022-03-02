# Use the file name mbox-short.txt as the file name
#Count these lines and extract the floating point
#values from each of the lines and compute the average
#of those values and produce an output as shown below.
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    nums = line.find("0")
    fltval = float(line[nums: ])
    count = count + 1
    total = total + fltval

avg = total/count
print("Average spam confidence: ",avg)
