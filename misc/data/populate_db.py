import psycopg2
import pandas as pd
import numpy as np # pipenv

# TO DO:
df = pd.read_csv('../data/processed/cannabis_clean.csv', index_col=False)

conn = psycopg2.connect("postgres://arqkjrwiuajibn:7278a6700d672d92eeb3125a6a9fa4185b071cf8ea9ad4a43705ead866e87325@ec2-52-45-14-227.compute-1.amazonaws.com:5432/d2spb1ln3u4n4l")
curs = conn.cursor()


# Add all the strains from the csv file into the database
for row in df.itertuples():
    insert = f'''
        INSERT INTO strain VALUES {row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]};'''
    curs.execute(insert)

conn.commit()
