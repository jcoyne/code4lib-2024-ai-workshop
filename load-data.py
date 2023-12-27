import csv
from db import db

with db() as conn:
    cursor = conn.cursor()
    # Write code to load data from mydata.csv
    # with open("mydata.csv") as infile:
    #   ...
    #   conn.commit()