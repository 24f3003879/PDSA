# Creating a file name 'write.txt" inside the folder "week-1/file_handling/write/write.txt" 

f = open("week-1/file_handling/write/write.txt", 'w')
lines = ['one', 'two', 'three', 'four', 'five', 'six']
for line in lines:
    f.write(line + '\n')
f.close()
