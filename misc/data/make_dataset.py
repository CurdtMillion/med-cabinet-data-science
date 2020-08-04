# Scripts to download or generate data


#make the data PostgreSQL friendly
df["Description"] = df["Description"].str.replace("'", '')
df.replace(np.nan, '', inplace=True)

# TO DO: 
# input raw cannabis.csv >> output processed cannabis_clean.csv
