file = open("week-1/file_handling(CSV)/readcsv.csv", 'r')
for line in file:
    print(line.strip())
file.close()


# print the chem marks of each student
# we need to deal with the header first


f = open("week-1/file_handling(CSV)/readcsv.csv", 'r')
header = f.readline()
# The file object has finished reading the first line
# It is now ready to read from the second line onwards

for line in f:
    line = line.strip()
    columns = line.split(',')
    chem_marks = int(columns[2])
    print(chem_marks)
f.close()