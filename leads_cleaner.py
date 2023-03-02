import csv
import os

blacklist = set()

with open('blacklist.txt', 'r') as f:
    for line in f:
        blacklist.add(line.strip())

with open('leads.csv', 'r') as f, open('output.csv', 'w', newline='') as out_f:
    reader = csv.reader(f)
    writer = csv.writer(out_f)
    header = next(reader)
    writer.writerow(header) # write header to output file
    for row in reader:
        if not any(banned_word in row[2] for banned_word in blacklist):
            writer.writerow(row)

# remove original file
os.remove('leads.csv')

# rename output file to original file name
os.rename('output.csv', 'leads.csv')
