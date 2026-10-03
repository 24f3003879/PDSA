# Creating a file name 'write.txt" inside the folder "week-1/file_handling/write/write.txt" 

file = open("week-1/file_handling/write/write.txt", 'w')
lines = ['one', 'two', 'three', 'four', 'five', 'six']
numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10']
for line in lines:

    file.write(line + '\n')

for num in numbers:
    if int(num)%2 == 0:
        file.write(num + '\n')


file.close()
