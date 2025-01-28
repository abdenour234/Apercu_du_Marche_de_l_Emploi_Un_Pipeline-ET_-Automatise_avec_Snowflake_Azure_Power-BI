import numpy as pd 
import pandas as pd 
from utilities import *
df = pd.read_csv("JOBETL1/S3/jobs.csv")
df['Cloud_Providers']=df['Description'].apply(extract_cloud_providers)
df['frameworks_libraries']=df['Description'].apply(extract_frameworks_libraries)
df['big_data_tools']=df['Description'].apply(extract_bigdata)

df["programming_languages"]=df["Description"].apply(extract_programming_languages)
df["data_tools"]=df["Description"].apply(extract_data_tools)
df["DevopsTools"]=df["Description"].apply(extract_devops_tools)
df["DataBases"]=df["Description"].apply(extract_databases)
df["city"] = df['Location'].apply(get_moroccan_city)
df["Role"] =df["Job Title"].apply(categorize_job_title)

df.to_csv("JOBETL1/S3/jobs_with_features.csv", index=False)

