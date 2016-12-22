# csvwriting.py
# import csv module
import csv
import math
# open file in write mode
csvfile = open('triangles.csv', 'w')

# create the csv writer
csvwriter = csv.writer(csvfile, delimiter=',')

# write to the file
# create a header
csvwriter.writerow(['a', 'b', 'hypotenuse'])


# for each value of a:
for a in range(1,1001):
    csvwriter.writerow([a])
  
    # get each value of b
    for b in range(a,1001):
        hypotenuse= math.sqrt(a**2 + b**2)
        csvwriter.writerow([a,b])

# close file
for a in range(1,1001):
    csvfile.close()