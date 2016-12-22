# open file in write mode
file = open('listfile.txt', 'w')

#TODO: create the list
n= 1
for n in range(5):
    file.write(input('SPEAK! ') + '\n')
n= +1

#close file
file.close()