import sys

for x in range(100): # 0 to 99
	output = "" # output string 

	# x+1 shifts range to 1 to 100
	if (x+1) % 3 == 0: 
		output += "Crackle" # if multiple of 3, print Crackle
	if (x+1) % 5 == 0: 
		output += "Pop" # (inclusive) if multiple of 5, print Pop
	if output == "": 
		output += str(x+1) # if neither of above conditions met, print number
	
	if len(sys.argv) > 1 and sys.argv[1] == "test": # if test flag passed from command line
		print(str(x+1) + ": " + output) # test code
	else:
		print(output) # normal output