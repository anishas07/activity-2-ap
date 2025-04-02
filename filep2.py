#read a File
file = open("Codingal1.txt", "r")
print(file.read())
file.close()

#write a file
file1 = open("Codingal1.txt", "w")
print(file1.write("hello, this is write mode."))
file1.close()

#append a file
file2 = open("Codingal1.txt", "a")
file2.write("This file is in append mode.")
file2.close()