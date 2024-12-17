import requests
import pandas as pd

# API endpoint and headers
url = "https://linkedin-data-scraper.p.rapidapi.com/search_jobs"
headers = {
    "x-rapidapi-key": "7bbaa81c63msh190363b3189eb05p10f6d2jsne405b9c1ded2",
    "x-rapidapi-host": "linkedin-data-scraper.p.rapidapi.com",
    "Content-Type": "application/json"
}

# List of job keywords to search
job_keywords = ["Data Scientist", "Data Analyst", "Data Engineer"]

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
                    "Keyword": keyword,
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
df.to_csv("JOBETL1//S3//linkedin_jobs.csv", mode='a', index=False, header=not pd.io.common.file_exists("JOBETL1//S3//linkedin_jobs.csv"))

print("Job data saved to linkedin_jobs.csv")
