import psycopg2
import csv

print('hey dood')
conn = psycopg2.connect(database="ai",
                        host="db",
                        user="root",
                        password="password",
                        port="5432")
cursor = conn.cursor()

with open("mydata.csv") as infile:
    cursor.copy_expert("COPY books (id, author, description) FROM stdin WITH CSV HEADER", infile)
    conn.commit()
    cursor.close()

print("all good")