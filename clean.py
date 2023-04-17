import pandas as pd
import seaborn as sns
import numpy as np
import os

# to clean 33, 39, 43, 52

COLOUMN_NAMES = ['ts','uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'proto',
'service',	'duration',	'orig_bytes', 'resp_bytes', 'conn_state', 'local_orig',
'local_resp', 'missed_bytes', 'history', 'orig_pkts', 'orig_ip_bytes', 
'resp_pkts', 'resp_ip_bytes', 'tunnel_parents', 'label', 'detailed-label']

# df = pd.read_csv("extract_dataset/Mal33-1.csv",header=0,names=COLOUMN_NAMES,low_memory=False)

#Files to read
# 'Honey4-1.csv', 'Mal20-1.csv', '.DS_Store', 'Mal21-1.csv', 'Mal3-1.csv', 'Honey5-1.csv', 'Honey7-1.csv', 
# 'Mal1-1.csv', 'Mal42-1.csv', 'Mal60-1.csv', 'Mal7-1.csv', 'Mal44-1.csv', 'Mal48-1.csv', 'Mal9-1.csv', 
# 'Mal36-1.csv', 'Mal34-1.csv', 'Mal8-1.csv', 'Mal17-1.csv', 'Mal49-1.csv', 'Mal35-1.csv'

# No. of lines
# Honey4-1.csv     449
# Mal20-1.csv      3208
# Mal21-1.csv      3285
# Mal3-1.csv       156102
# Honey5-1.csv     1373
# Honey7-1.csv     129
# Mal1-1.csv       1008747
# Mal42-1.csv      4425
# Mal60-1.csv      3581027
# Mal7-1.csv       11454713
# Mal44-1.csv      236
# Mal48-1.csv      3394337
# Mal9-1.csv       6378292
# Mal36-1.csv      13645097
# Mal34-1.csv      2527
# Mal8-1.csv       10402
# Mal17-1.csv      18464775
# Mal49-1.csv      5410560
# Mal35-1.csv      10447786


os.chdir("extract_dataset")
files = os.listdir()
print(files)

for file in files :
    if file == ".DS_Store":
        continue
        
        df = pd.read_csv(file,names=COLOUMN_NAMES,header=0,low_memory=False)
        print(file)
        print(df['tunnel_parents'].unique())
        print (df.head())
        df.drop(df.tail(2).index,inplace=True)  #Removed last two redundant lines
        df.to_csv(file)   #Save modified csv file
        print(df.shape[0])  #Display no. of lines in dataset
        print(df.isnull().sum()) #Display number of duplicate rows in dataset

        for col in df.columns :
            print(file, col)
            unique_values = df[col].unique()
            value_counts = df[col].value_counts()
            print(f"\n{col} value counts:\n{value_counts}") #Number of unique values in each column
