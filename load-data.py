import psycopg2
import csv
from HuggingFace import HuggingFace

print('hey dood')
# conn = psycopg2.connect(database="ai",
#                         host="db",
#                         user="root",
#                         password="password",
#                         port="5432")
# cursor = conn.cursor()

# with open("mydata.csv") as infile:
#     cursor.copy_expert("COPY books (id, author, description) FROM stdin WITH CSV HEADER", infile)
#     conn.commit()
#     cursor.close()

hugging_face = HuggingFace('hf_xxxxx') # Token HERE
print(hugging_face.embedding("for real"))

print("all good")