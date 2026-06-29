# opening and reading a file

f = open('week-1/file_handling/example.txt', 'r')
for line in f:
    print(line, end='')
f.close()

# creating a file and writing in it

w = open('week-1/file_handling/write.txt', 'w')
w.write('Shubh')
w.write('\n')
w.write('Ankit')
w.write('\n')
w.write('Rajni')
w.write('\n')
w.write('Ishu')
w.write('\n')
w.write('Samar')
w.close()


