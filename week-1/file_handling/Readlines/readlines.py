#Python also provides a way to read the file and store it as a list of lines:

file = open("week-1/file_handling/Readlines/readlines.txt", 'r')
lines = file.readlines()
for line in lines:
    print(line.strip())
file.close

