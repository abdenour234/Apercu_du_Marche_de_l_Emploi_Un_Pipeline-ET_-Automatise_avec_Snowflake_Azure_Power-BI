import numpy as pd 
import pandas as pd 
from utilities import *
def transform(**kwargs):

   # Pull the DataFrame from XCom
    ti = kwargs['ti']
    df_json = ti.xcom_pull(key='extracted_data')
    df = pd.read_json(df_json)


    df['Cloud_Providers']=df['Description'].apply(extract_cloud_providers)
    df['frameworks_libraries']=df['Description'].apply(extract_frameworks_libraries)
    df['big_data_tools']=df['Description'].apply(extract_bigdata)
    df["programming_languages"]=df["Description"].apply(extract_programming_languages)
    df["data_tools"]=df["Description"].apply(extract_data_tools)
    df["DevopsTools"]=df["Description"].apply(extract_devops_tools)
    df["DataBases"]=df["Description"].apply(extract_databases)
    df["level"] = df["Description"].apply(classify_job_level)
    df["city"] = df['Location'].apply(get_moroccan_city)
    df["Role"] =df["Job Title"].apply(categorize_job_title)

    upload_dataframe_to_blob(df,connection_string="DefaultEndpointsProtocol=https;AccountName=myaccount123xyz;AccountKey=xhK3fQlCsEhvhkYeB4T4R2i6+kKB9vNPNKCkELyp87bo4BYnf9ZiZAWWXf0XeyhgKY3c1CZtK6jL+AStQynDEg==;EndpointSuffix=core.windows.net",container_name="silver",blob_name="data/data_silver.csv")
    # Push the transformed DataFrame to XCom
    ti.xcom_push(key='transformed_data', value=df.to_json())
    return df



