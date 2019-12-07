#This line of code helps to open a file to read-only
f = open("C:/Users/s527998/Documents/Data Mining project/H1B.csv","r")
#This line of code helps open  the file to write
o = open("C:/Users/s527998/Documents/Data Mining project/mapper.txt", "w")
index = 0
#For each line of data we are splitting them by commas and then putting the calue 1 at the end of each output
for line in f:
    data = line.strip().split(",")
    if len(data) == 15 and len(data[3])>0:
        o.write("{0},{1}\n".format(data[3].strip(), 1))
        index = index + 1
       #These two lines of code helps to print 15 values
        if index < 15:
                print("{0},{1}\n".format(data[3], 1))
#This line of code helps close the file
f.close()
#This line of code helps close the file
o.close()