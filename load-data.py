import csv
from db import db

with db() as conn:
    cursor = conn.cursor()
    # Write code to load data from harvest/data.csv
    with open("harvest/data.csv") as infile:
        reader = csv.reader(infile)
        for row in reader:
            cursor.execute("INSERT INTO courses (title, description) VALUES (%s, %s)",
                           (row[0], row[1]))
            print(" " + row[0])
    conn.commit()