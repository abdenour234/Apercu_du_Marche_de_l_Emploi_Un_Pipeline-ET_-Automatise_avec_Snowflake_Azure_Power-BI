import pandas as pd
from utilities import *
df=pd.read_csv("JOBETL1\S3\jobs.csv")

df["programming_languages"]=df["Description"].apply(extract_programming_languages)
df["data_tools"]=df["Description"].apply(extract_data_tools)
df["DevopsTools"]=df["Description"].apply(extract_devops_tools)
df["DataBases"]=df["Description"].apply(extract_databases)