import pandas as pd
from db_connection import get_engine
import os

engine = get_engine()
recent_file = str()
folder_path = "./raw_data/"

files = os.listdir(folder_path)
for file in files:
    print(file)
    recent_file = file

#load csv
df = pd.read_csv(f"raw_data/{recent_file}") 

#write data to postgres
df.to_sql("listening_history", engine, if_exists="replace", index=False)
print("Data loaded into PostgreSQL successfully!")
