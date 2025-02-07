import datetime
import pandas as pd
from utilities import upload_dataframe_to_blob

def load(**kwargs):
    # Pull the DataFrame from XCom
    ti = kwargs['ti']
    df_json = ti.xcom_pull(key='transformed_data')
    
    # Convert the JSON string to DataFrame using StringIO as recommended in the warning
    from io import StringIO
    df = pd.read_json(StringIO(df_json))
    
    # Drop specified columns
    df = df.drop(columns=["Job Title", "Description", "Location"])
    
    # Convert any list columns to strings before dropping duplicates
    for column in df.select_dtypes(include=['object']).columns:
        if df[column].apply(lambda x: isinstance(x, list)).any():
            df[column] = df[column].apply(lambda x: str(x) if isinstance(x, list) else x)
    
    # Now drop duplicates safely
    df = df.drop_duplicates()
    
    # Upload to blob storage
    upload_dataframe_to_blob(
        df,
        connection_string="DefaultEndpointsProtocol=https;AccountName=myaccount123xyz;AccountKey=xhK3fQlCsEhvhkYeB4T4R2i6+kKB9vNPNKCkELyp87bo4BYnf9ZiZAWWXf0XeyhgKY3c1CZtK6jL+AStQynDEg==;EndpointSuffix=core.windows.net",
        container_name="gold",
        blob_name=f"data/data_gold_{datetime.datetime.now()}.csv"
    )
    
    return df