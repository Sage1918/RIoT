import pandas as pd
import numpy as np
import os

# Defining the columns in the dataframe
COLOUMN_NAMES = ['ts','uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'proto',
'service',	'duration',	'orig_bytes', 'resp_bytes', 'conn_state', 'local_orig',
'local_resp', 'missed_bytes', 'history', 'orig_pkts', 'orig_ip_bytes', 
'resp_pkts', 'resp_ip_bytes', 'tunnel_parents', 'label', 'detailed-label']

# Read the existing cleaned datasets
os.chdir("clean_dataset") 
filter_files = os.listdir()

# Read the datasets to be cleaned
os.chdir("../extract_dataset")
files = os.listdir()


for file in files :
    # Filter out files that have already been cleaned from those that require cleaning
    # ".DS_Store is a hidden mac file and need to be ignored"
    if file in filter_files or file == ".DS_Store":
        continue

    # User can select files to be cleaned   
    choice = input(file + " -> clean?(Y/N): ")
    if choice == "Y" or choice == "y" :
        df = pd.read_csv(file,names=COLOUMN_NAMES,header=None,low_memory=True)

        # Drop the redundant columns from the dataset 
        df = df.drop("ts", axis = 1)
        df = df.drop("uid", axis = 1)
        df = df.drop("id.orig_h", axis = 1)
        df = df.drop("id.resp_h", axis = 1)
        df = df.drop("tunnel_parents", axis = 1)
        df = df.drop("local_orig", axis = 1)
        df = df.drop("local_resp", axis = 1)

        # Remove all duplicate rows from the dataset
        print("No. of duplicates(before cleaning) : ", len(df)-len(df.drop_duplicates()))
        df=df.drop_duplicates()
        print("No. of duplicates(after cleaning) : ", len(df)-len(df.drop_duplicates()))

        # Store the modified dataset
        print(df.head().to_string())
        df.to_csv("../clean_dataset/" + file)
    else :
        continue
    
os.chdir("../clean_dataset")

# Combine the datasets into a single file
combined_df = pd.read_csv("Mal43-1.csv",header=None,low_memory=False)
print("Mal43-1.csv")

for file in filter_files :
    if file == ".DS_Store" or file == "Mal43-1.csv" :
        continue
    
    else : 
        print(file)
        df = pd.read_csv(file,header=None,low_memory=True)
        # Concatenate the dataset to the combined dataset
        combined_df = pd.concat([combined_df, df])

print(combined_df.head().to_string())
# df.to_csv("../combined_dataset.csv") # If the intermediate file needs storing

os.chdir("..")

# Clean the combined dataset by removing any duplicate rows
print("No. of duplicates(before cleaning) : ", len(combined_df)-len(combined_df.drop_duplicates()))
df=df.drop_duplicates()
print("No. of duplicates(after cleaning) : ", len(combined_df)-len(combined_df.drop_duplicates()))
df.to_csv("final_dataset.csv")