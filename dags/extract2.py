import requests
import pandas as pd

# API endpoint and headers
url = "https://linkedin-data-scraper.p.rapidapi.com/search_jobs"
headers = {
    'x-rapidapi-key': "4083d477c6msh3cbfbf8d7897306p1e7ec5jsn175d96ebac63",
    'x-rapidapi-host': "linkedin-data-scraper.p.rapidapi.com",
    'Content-Type': "application/json"
}

# List of job keywords to search
job_keywords = ["Cloud Engineer", "Software Developer", "Software Engineer", "DevOps Engineer", "Cloud Architect"]

# Initialize an empty list to store the results
all_jobs = []

# Loop through each keyword and make API requests
for keyword in job_keywords:
    payload = {
        "keywords": keyword,
        "location": "Morocco",
        "count": 100
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

# Save the DataFrame to a CSV file
csv_path = "JOBETL1//S3//jobs.csv"
df.to_csv(csv_path, mode='a', index=False, header=not pd.io.common.file_exists(csv_path))

print("Job data saved to linkedin.csv")
