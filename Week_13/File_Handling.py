file1 = open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_13\Input_File.txt", "r")   #opening input file in read mode
file2 = open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_13\Output_File.txt", "w")  #opening output file in write mode to write contents into it
for line in file1:                              #looping through each line
    file2.write(line)                           #writing each line to the output file

file1.close()                                   #closing input file
file2.close()                                   #closing output file

file2 = open(r"C:\Users\user\Desktop\Sayur Learning\Sowmiya\Week_13\Output_File.txt", "r")  #opening output file in read mode to read the contents
print(file2.read())                              #printing the contents of the output file
file2.close()                                    #closing the output file


"""
Hello. This is an input file to copy and write the contents in this file to another file.
"""