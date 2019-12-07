#This line of command will open mapper.txt file in read only mode
Mappedinput = open("C:/Users/s527998/Documents/Data Mining project/mapper.txt", "r")
#This line of code will open a txt file in write only mode
Sortedoutput = open("C:/Users/s527998/Documents/Data Mining project/sorted.txt", "w")
#This line of code will read the each lines of code
lines = Mappedinput.readlines()
#This line of code will sort the data
lines.sort()

for line in lines:
	Sortedoutput.write(line)
#This line of code will close the Mappedinput file
Mappedinput.close()
#This line of code will close the Sortedoutput file
Sortedoutput.close()

