import requests
import pandas as pd
from utilities  import upload_dataframe_to_blob 
def extract_(**kwargs):
    # API endpoint and headers
    url = "https://linkedin-data-scraper.p.rapidapi.com/search_jobs"
    headers = {
    'x-rapidapi-key': "4083d477c6msh3cbfbf8d7897306p1e7ec5jsn175d96ebac63",
    'x-rapidapi-host': "linkedin-data-scraper.p.rapidapi.com",
    'Content-Type': "application/json"
}

    # List of job keywords to search
    job_keywords = ["Data Scientist", "Data Analyst", "Data Engineer","Cloud Engineer", "Software Developer", "Software Engineer", "DevOps Engineer", "Cloud Architect"]

    # Initialize an empty list to store the results
    all_jobs = []

    # Loop through each keyword and make API requests
    for keyword in job_keywords:
        payload = {
            "keywords": keyword,
            "location": "Morocco",
            "count": 50
        }
        response = requests.post(url, json=payload, headers=headers)
        
        # Check if the request was successful
        if response.status_code == 200:
            jobs = response.json().get("response", [])
            
            # Extract relevant fields and store them in the list
            for job_group in jobs:  # Jobs are nested
                for job in job_group:
                    job_title = job.get("title", "N/A")
                    company_name = job.get("companyName", "N/A")
                    job_description = job.get("jobDescription", "N/A")
                    formatted_location = job.get("formattedLocation", "N/A")
                    
                    all_jobs.append({
                        
                        "Job Title": job_title,
                        "Company Name": company_name,
                        "Location": formatted_location,
                        "Description": job_description.replace("\n", " "),
                    })
        else:
            print(f"Failed to fetch jobs for keyword: {keyword}, Status Code: {response.status_code}")

    # Convert the list of jobs into a Pandas DataFrame
    df = pd.DataFrame(all_jobs)
    upload_dataframe_to_blob(df,connection_string="DefaultEndpointsProtocol=https;AccountName=myaccount123xyz;AccountKey=rcdaFz9G/N7oKPqrKVOaotV1uFCcNpQrGuCBXkvRvErT+G/oKPMXO2cWXCda99rfSBNMM2Pd0PyH+AStkThGVQ==;EndpointSuffix=core.windows.net",container_name="bronze",blob_name="data/data_bronze.csv")
    # Push the DataFrame to XCom
    kwargs['ti'].xcom_push(key='extracted_data', value=df.to_json())
    return df

extract_()
