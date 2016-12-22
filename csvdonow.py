import csv


# open file in write mode
csvfile= open('donow.csv', 'w')

# create the csv writer
csvwriter = csv.writer(csvfile, delimiter=',')

for x in range(5):
    csvwriter.writerow([1,2,3,4,5])
  
    for y in range(5):
        csvwriter.writerow([1,2,3])

csvfile.close()