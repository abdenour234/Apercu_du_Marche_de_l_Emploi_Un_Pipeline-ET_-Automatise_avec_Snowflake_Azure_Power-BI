import pandas as pd 
from utilities import upload_dataframe_to_blob, read_dataframe_from_blob
def load(**kwargs) :
    # Pull the DataFrame from XCom
    ti = kwargs['ti']
    df_json = ti.xcom_pull(key='transformed_data')
    df = pd.read_json(df_json)
    
    df = df.drop(columns=["Job Title", "Description", "Location"])
    df = df.drop_duplicates()

    upload_dataframe_to_blob(df ,connection_string="DefaultEndpointsProtocol=https;AccountName=myaccount123xyz;AccountKey=rcdaFz9G/N7oKPqrKVOaotV1uFCcNpQrGuCBXkvRvErT+G/oKPMXO2cWXCda99rfSBNMM2Pd0PyH+AStkThGVQ==;EndpointSuffix=core.windows.net",container_name="gold" ,blob_name="data/data_gold.csv")
    
    return df 

