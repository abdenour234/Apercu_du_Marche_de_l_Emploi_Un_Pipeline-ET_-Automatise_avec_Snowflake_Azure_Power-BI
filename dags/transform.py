import numpy as pd 
import pandas as pd 
from utilities import *
df = pd.read_csv("JOBETL1/S3/jobs.csv")
df['Cloud_Providers']=df['Description'].apply(extract_cloud_providers)
df['frameworks_libraries']=df['Description'].apply(extract_frameworks_libraries)
df['big_data_tools']=df['Description'].apply(extract_bigdata)