import csv
from db import db
import HuggingfaceInferenceApi
from dotenv import load_dotenv
load_dotenv()

def load_data():
    with db() as conn:
        cursor = conn.cursor()
        # Write code to load data from harvest/data.csv
        with open("harvest/data.csv") as infile:
            reader = csv.reader(infile)
            for row in reader:
                embedding = HuggingfaceInferenceApi.query({"inputs": row[1] })
                cursor.execute("INSERT INTO courses (title, description, embedding) VALUES (%s, %s, %s)",
                               (row[0], row[1], embedding))
                print(" " + row[0])
        conn.commit()

load_data()
