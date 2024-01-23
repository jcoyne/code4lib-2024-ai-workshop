import os
import csv

directory = '_posts/'
delimeter = '---'

with open('data.csv', 'w', newline='') as out:
  writer = csv.writer(out)
  for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(filename)
    delimeter_count = 0
    title = ''
    description = ''
    with open(directory + filename, 'r') as input_file:
      for line in input_file:
        if line.startswith('title: '):
          _, title = line.rsplit('title: ')
        if delimeter_count > 1:
          description += line
        if line == '---\n':
          delimeter_count += 1    
    writer.writerow([title.strip(' "\n'), description.strip()])
        
      