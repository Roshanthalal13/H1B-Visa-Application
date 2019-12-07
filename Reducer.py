# This line of code will open a input file to read only
input = open("C:/Users/s527998/Documents/Data Mining project/sorted.txt","r")
# This line of code will open output file to write only
output = open("C:/Users/s527998/Documents/Data Mining project/reducer.txt","w")
# These multiple lines of code will iterate through each line of input and calculate the total number of the common value
thisKey = ""
thisValue = 0
index=0
for line in input:
    #This line of code will split the csv record to a tuple by comma
    record = line.strip().split(",")
    if len(record) == 2:
        soc_code, value = record
        if soc_code.strip() != thisKey:
            if thisKey:
                #These lines of code will give the last key value pair as an Output
                output.write(thisKey.strip() + '\t' + str(thisValue)+'\n')
                index=index+1
                #This line of code will run if the index is below 15
                if index <  15:
                    print(thisKey.strip() + '\t' + str(thisValue)+'\n')
            #This line of coe will help the app to start over when changing keys
            thisKey = soc_code.strip()
            thisValue = 0
        thisValue += float(value)
#These lines of code will output the final entry
output.write(thisKey.strip() + '\t' + str(thisValue)+'\n')
input.close()
output.close()