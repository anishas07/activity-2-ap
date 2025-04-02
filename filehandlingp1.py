file = open('Codingal.txt', 'r')
print(file.read())
file.close()

file = open('Codingal.txt', 'r')
print(file.read(10))
file.close()

file1 = open('Codingal.txt', 'a')
file1.write("Here is some information about the beach.")
file1.close()