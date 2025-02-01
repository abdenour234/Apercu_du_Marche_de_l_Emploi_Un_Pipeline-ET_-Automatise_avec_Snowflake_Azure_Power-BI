
import numpy as np
from enum import Enum
from typing import Tuple, List
import re
def extract_programming_languages(text):
    """
    Extract programming languages mentioned in the given text.
    
    Args:
        text (str): The input text containing job descriptions.
        
    Returns:
        list: A list of unique programming languages found in the text.
    """
    # Predefined list of programming languages
    programming_languages = [
        "Python", "Java", "R","C","C++", "C#", "JavaScript", "Ruby", 
        "PHP", "Swift", "Go", "Kotlin", "Perl", "SQL", "Scala", "Matlab", 
        "Dart", "TypeScript", "Shell", "Bash", "Rust"
    ]
    
    # Normalize the text (convert to lowercase)
    text_lower = text.lower().split()
    
    # Extract programming languages mentioned in the text
    extracted_languages = [
        lang for lang in programming_languages 
        if lang.lower() in text_lower
    ]
    
    # Return unique programming languages
    return list(set(extracted_languages)) if extracted_languages else np.nan

def extract_data_tools(text):
    """
    Extract data tools mentioned in the given text with improved matching.
    
    Args:
        text (str): The input text containing job descriptions.
        
    Returns:
        list or np.nan: A list of unique data tools found in the text, or NaN if none are found.
    """
    # Predefined list of data tools with their variants
    data_tools = {
        "excel": ["excel", "ms excel"],
        "tableau": ["tableau"],
        "power bi": ["power bi", "powerbi"],
        "snowflake": ["snowflake"],
        "hadoop": ["hadoop"],
        "spark": ["spark"],
        "airflow": ["airflow"],
        "kafka": ["kafka"],
        "looker": ["looker"],
        "qlikview": ["qlikview", "qlik view"],
        "databricks": ["databricks"],
        "domo": ["domo"],
        "alteryx": ["alteryx"],
        "sisense": ["sisense"],
        "redash": ["redash"],
        "metabase": ["metabase"]
    }
    
    # Normalize the text (convert to lowercase)
    text_lower = text.lower()
    
    found_tools = []
    
    # Check for each data tool and its variants
    for main_name, variants in data_tools.items():
        if any(variant in text_lower for variant in variants):
            found_tools.append(main_name)
    
    # Return unique data tools or NaN if none are found
    return list(set(found_tools)) if found_tools else np.nan

def extract_devops_tools(text):
    """
    Extract DevOps tools mentioned in the given text.
    
    Args:
        text (str): The input text containing job descriptions.
        
    Returns:
        list or np.nan: A list of unique DevOps tools found in the text, or NaN if none are found.
    """
    # Predefined list of DevOps tools
    devops_tools = [
    # Containerization and Orchestration
    "Docker", "Kubernetes", "K8s",
    
    # CI/CD Tools
    "Jenkins", "GitLab", "GitLab CI/CD", "CircleCI", "Travis CI", "ArgoCD", 
    "Bamboo", "AWS CodePipeline", "Azure DevOps", "Azure Pipelines",
    
    # Infrastructure as Code (IaC)
    "Terraform", "Ansible", "Puppet", "Chef", "CloudFormation", 
    
    # Monitoring and Logging
    "Prometheus", "Grafana", "Nagios", "Splunk", "ELK", "ELK Stack", 
    "Elastic Stack", "ElasticSearch", "Logstash", "Kibana",
    
    # Security and Secrets Management
    "Vault", "HashiCorp Vault", "Consul",
    
    # Other DevOps Tools
    "Git", "GitHub Actions", "GitHub", "Nomad", "Docker Swarm"
]

    
    # Normalize the text (convert to lowercase)
    text_lower = text.lower()
    
    # Extract DevOps tools mentioned in the text
    extracted_tools = [
        tool for tool in devops_tools 
        if tool.lower() in text_lower
    ]
    
    # Return unique DevOps tools or NaN if none are found
    return list(set(extracted_tools)) if extracted_tools else np.nan

def extract_databases(text):
    """
    Extract databases mentioned in the given text with improved matching.
    
    Args:
        text (str): The input text containing job descriptions.
        
    Returns:
        list or np.nan: A list of unique databases found in the text, or NaN if none are found.
    """
    # Liste des bases de données connues avec leurs variantes communes
    databases = {
        "mysql": ["mysql", "my sql", "mysql server"],
        "postgresql": ["postgresql", "postgres"],
        "sqlite": ["sqlite", "sql lite"],
        "mongodb": ["mongodb", "mongo db", "mongo", "mongoose"],
        "mariadb": ["mariadb", "maria db"],
        "oracle": ["oracle", "oracle db", "oracle database"],
        "mssql": ["mssql", "sql server", "microsoft sql server"],
        "cassandra": ["cassandra"],
        "redis": ["redis"],
        "couchdb": ["couchdb", "couch db"],
        "neo4j": ["neo4j"],
        "firebase": ["firebase"],
        "bigquery": ["bigquery", "google bigquery"],
        "dynamo db": ["dynamo db", "dynamodb"],
        "snowflake": ["snowflake"]
    }
    
    # Normalize the text (convert to lowercase and remove punctuation)
    text_lower = text.lower()
    
    found_databases = []
    
    # Check for each database and its variants
    for main_name, variants in databases.items():
        if any(variant in text_lower for variant in variants):
            found_databases.append(main_name)
    
    # Return unique databases or NaN if none are found
    return list(set(found_databases)) if found_databases else np.nan


def extract_cloud_providers(text):
    """
    Extract cloud providers mentioned in the given text.
    
    Args:
        text (str): The input text containing job descriptions.
        
    Returns:
        list or np.nan: A list of unique cloud providers found in the text, or NaN if none are found.
    """
    
    # Predefined list of cloud providers
    cloud_providers = [
    # AWS
    "AWS", "Amazon Web Services", "Amazon Cloud", "EC2", "S3", "AWS Lambda", "Amazon RDS",
    "Elastic Beanstalk", "Amazon EKS", "Amazon ECS", "Amazon DynamoDB", "Amazon Sagemaker",
    
    # Google Cloud
    "GCP", "Google Cloud Platform", "Google Cloud", "Google Compute Engine", "GKE", 
    "Google Kubernetes Engine", "BigQuery", "Google App Engine", "Google Cloud Storage",
    
    # Azure
    "Azure", "Microsoft Azure", "Azure Cloud", "Azure DevOps", "Azure Functions", 
    "Azure Kubernetes Service", "Azure Machine Learning", "Azure Blob Storage", 
    "Azure Virtual Machines", "Azure App Service",
    
    # Oracle Cloud
    "Oracle Cloud", "OCI", "Oracle Cloud Infrastructure", "Oracle Autonomous Database",
    "Oracle Compute", "Oracle Database Cloud", "Oracle Cloud Platform", "Oracle Analytics Cloud",
    
    # IBM Cloud
    "IBM Cloud", "IBM Bluemix", "IBM Watson", "IBM Cloud Functions", "IBM Cloud Kubernetes Service",
    
    # Other common cloud providers
    "Alibaba Cloud", "Aliyun", "Tencent Cloud", "Linode", "DigitalOcean", "Vultr",
    "Rackspace", "OVH Cloud", "Heroku", "SAP Cloud", "Salesforce Cloud", "Red Hat OpenShift",
    "Cloudflare", "Netlify", "Fastly", "Backblaze"
]

    
    # Normalize the text (convert to lowercase)
    text_lower = text.lower()
    
    # Extract cloud providers mentioned in the text
    extracted_tools = [
        tool for tool in cloud_providers 
        if tool.lower() in text_lower
    ]
    
    # Return unique cloud providers or NaN if none are found
    return list(set(extracted_tools)) if extracted_tools else np.nan


def extract_frameworks_libraries(text):
    """
    Extract frameworks and libraries mentioned in the given text with improved matching.
    
    Args:
        text (str): The input text containing job descriptions.
        
    Returns:
        list or np.nan: A list of unique frameworks/libraries found in the text, or NaN if none are found.
    """
    # Liste des frameworks et bibliothèques connues avec leurs variantes communes
    frameworks_libraries = {
        # Data Science / ML
        "numpy": ["numpy", "np"],
        "pandas": ["pandas", "pd"],
        "matplotlib": ["matplotlib", "plt"],
        "seaborn": ["seaborn", "sns"],
        "scipy": ["scipy"],
        "scikit-learn": ["scikit-learn", "sklearn", "sci-kit learn"],
        "keras": ["keras"],
        "pytorch": ["pytorch", "torch"],
        "tensorflow": ["tensorflow", "tf"],
        "xgboost": ["xgboost", "xgb"],
        "lightgbm": ["lightgbm", "lgb", "light gbm"],
        "nltk": ["nltk"],
        "spacy": ["spacy"],
        
        # Web/App Frameworks
        "react": ["react", "react.js", "reactjs"],
        "angular": ["angular", "angular.js", "angularjs"],
        "vue": ["vue", "vue.js", "vuejs"],
        "django": ["django"],
        "flask": ["flask"],
        "spring boot": ["spring boot", "springboot"],
        "node.js": ["node.js", "nodejs", "node"],
        "rails": ["rails", "ruby on rails"],
        "asp.net": ["asp.net", "asp .net", "asp net"],
        "flutter": ["flutter"],
        "xamarin": ["xamarin"]
    }
    
    # Normalize the text (convert to lowercase and remove punctuation)
    text_lower = text.lower()
    
    found_tools = []
    
    # Check for each framework/library and its variants
    for main_name, variants in frameworks_libraries.items():
        if any(variant in text_lower for variant in variants):
            found_tools.append(main_name)
    
    # Return unique frameworks/libraries or NaN if none are found
    return list(set(found_tools)) if found_tools else np.nan


def extract_bigdata(text):
    """
    Extract frameworks, libraries, and big data tools mentioned in the given text.
    
    Args:
        text (str): The input text containing job descriptions.
        
    Returns:
        list or np.nan: A list of unique tools found in the text, or NaN if none are found.
    """
    big_data = {
     
        # Big Data Tools
        "hadoop": ["hadoop", "apache hadoop", "hdfs"],
        "spark": ["spark", "apache spark", "pyspark"],
        "kafka": ["kafka", "apache kafka"],
        "airflow": ["airflow", "apache airflow"],
        "hive": ["hive", "apache hive"],
        "elasticsearch": ["elasticsearch", "elastic search", "elk"],
        "hbase": ["hbase", "apache hbase"],
        "pig": ["pig", "apache pig"],
        "storm": ["storm", "apache storm"],
        "flink": ["flink", "apache flink"],
        "nifi": ["nifi", "apache nifi"],
        "beam": ["beam", "apache beam"],
        "presto": ["presto"],
        "druid": ["druid", "apache druid"],
    }
    
    # Normalize the text (convert to lowercase and remove punctuation)
    text_lower = text.lower()
    
    found_tools = []
    
    # Check for each tool and its variants
    for main_name, variants in big_data.items():
        if any(variant in text_lower for variant in variants):
            found_tools.append(main_name)
    
    # Return unique tools or NaN if none are found
    return list(set(found_tools)) if found_tools else np.nan



def classify_job_level(job_description: str) -> str:
    """
    Determines if a job description is for a senior, junior, or internship position.
    
    Args:
        job_description (str): The job description text to analyze
        
    Returns:
        str: The job level classification ("SENIOR", "JUNIOR", or "INTERNSHIP")
    """
    # Convert to lowercase for case-insensitive matching
    text = job_description.lower()
    
    # Senior level indicators
    senior_patterns = {
        'experience': [
            r'\b[5-9]\+?\s*years?\s+of\s+experience',
            r'\b\d{2}\+?\s*years?\s+of\s+experience',
            r'senior\s+level\s+experience',
            r'extensive\s+experience'
        ],
        'leadership': [
            r'\blead\b|\bleading\b|\bleadership\b',
            r'\bmanage\b|\bmanager\b|\bmanagement\b',
            r'head\s+of',
            r'architect',
            r'principal'
        ],
        'strategic': [
            r'strategic',
            r'direction',
            r'vision',
            r'mentor\s+others',
            r'guide\s+team'
        ]
    }
    
    # Junior level indicators
    junior_patterns = {
        'experience': [
            r'\b[1-4]\+?\s*years?\s+of\s+experience',
            r'entry\s+level',
            r'junior',
            r'recent\s+graduate'
        ],
        'support': [
            r'assist\b',
            r'support\b',
            r'help\b',
            r'coordinate'
        ],
        'supervision': [
            r'under\s+supervision',
            r'under\s+guidance',
            r'report\s+to'
        ]
    }
    
    # Internship indicators
    internship_patterns = {
        'position': [
            r'\bintern\b',
            r'\binternship\b',
            r'\binterns\b',
            r'training\s+program',
            r'trainee'
        ],
        'education': [
            r'currently\s+(pursuing|enrolled|studying)',
            r'current\s+student',
            r'enrolled\s+in.*degree'
        ],
        'learning': [
            r'learning\s+opportunity',
            r'hands[-\s]on\s+experience',
            r'practical\s+experience',
            r'unpaid',
            r'academic\s+credit'
        ]
    }
    
    # Count matches for each level
    senior_count = 0
    junior_count = 0
    internship_count = 0
    
    # Check senior patterns
    for category, patterns in senior_patterns.items():
        for pattern in patterns:
            if re.search(pattern, text):
                senior_count += 1
    
    # Check junior patterns
    for category, patterns in junior_patterns.items():
        for pattern in patterns:
            if re.search(pattern, text):
                junior_count += 1
    
    # Check internship patterns
    for category, patterns in internship_patterns.items():
        for pattern in patterns:
            if re.search(pattern, text):
                internship_count += 1
    
    # Decision logic with weightings
    if internship_count >= 2:
        return "INTERNSHIP"
    elif senior_count >= 2:
        return "SENIOR"
    elif junior_count > senior_count or (junior_count >= 1 and senior_count < 2):
        return "JUNIOR"
    else:
        # Default to junior if unclear
        return "JUNIOR"

def get_moroccan_city(location: str) -> str:
    city_variants = {
        "rabat": "Rabat",
        "casablanca": "Casablanca",
        "fez": "Fez",
        "fès": "Fez",
        "marrakesh": "Marrakesh",
        "tangier": "Tangier",
        "tanger": "Tangier",
        "meknes": "Meknes",
        "agadir": "Agadir",
        "tetouan": "Tetouan",
        "tétouan": "Tetouan",
        "berkane": "Berkane",
        "kenitra": "Kenitra",
        "el borouj": "El Borouj"
    }
    location_lower = location.strip().lower()
    for variant, city in city_variants.items():
        if variant in location_lower:
            return city
    return ""

def categorize_job_title(job_title: str) -> str:
    categories = [
        ("Data Scientist", ["data scientist", "ml engineer", "ai & data science", "llm", 
                            "machine learning", "ai trainer", "quantitative data", 
                            "datascientist", "ai lead", "statistician"]),
        ("Data Analytics", ["data analytics", "data analyst", "bi", "data visualization", 
                            "data quality", "revenue management", "business research", 
                            "data insights", "data modeler", "biostatistician"]),
        ("Data Engineer", ["data engineer", "big data", "etl", "data modeling", 
                           "datawarehousing", "apache spark", "data pipeline", "data devops", 
                           "data lake", "data ops"]),
        ("DevOps", ["devops", "sre", "cloudops", "site reliability", "cicd", "kubernetes", 
                    "azure devops", "platform engineer", "cloud engineer"]),
        ("Cloud Engineer", ["cloud", "aws", "gcp", "azure", "google cloud", "cloud platform", 
                            "cloud security", "cloud architect", "cloud solution", "snowflake"]),
        ("Software Engineer", ["software engineer", "developer", "full stack", "backend", 
                               "frontend", "web developer", "mobile developer", "java", 
                               "python", "c#", "javascript", "node.js", "angular", "react", 
                               "symfony", "odoo", "salesforce", "php", "sw developer", 
                               "solidity", "rust", "flutter", "ios", "android", 
                               "embedded software", "qa engineer", "test automation", 
                               "coder", "technical lead", "api developer"]),
        ("Other", [])
    ]
    
    job_title_lower = job_title.strip().lower()
    for category, keywords in categories:
        for keyword in keywords:
            if keyword in job_title_lower:
                return category
    return "Other"


from azure.storage.blob import BlobServiceClient
from io import StringIO

def upload_dataframe_to_blob(new_data,connection_string, container_name, blob_name):
    """
    Appends new data to an existing CSV file in Azure Blob Storage.

    :param connection_string: str - Azure Blob Storage connection string.
    :param container_name: str - Name of the container in Blob Storage.
    :param blob_name: str - Name of the blob (CSV file).
    :param new_data: pd.DataFrame - New data to append.
    """
    try:
        # Initialize the BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)

        # Check if the blob exists
        blob_client = container_client.get_blob_client(blob_name)
        try:
            # Download existing data
            existing_blob = blob_client.download_blob().readall()
            existing_data = pd.read_csv(StringIO(existing_blob.decode('utf-8')))
        except Exception as e:
            print(f"Blob '{blob_name}' does not exist or is empty. Creating a new one.")
            existing_data = pd.DataFrame()  # Start with an empty DataFrame

        # Append new data to the existing DataFrame
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)

        # Save the updated DataFrame back to a CSV format
        updated_csv = StringIO()
        updated_data.to_csv(updated_csv, index=False)
        
        # Upload the updated CSV back to the blob
        blob_client.upload_blob(data=updated_csv.getvalue(), overwrite=True)

        print(f"Data appended successfully to blob '{blob_name}' in container '{container_name}'!")

    except Exception as e:
        print(f"An error occurred: {e}")

from azure.storage.blob import BlobServiceClient
from io import StringIO
import pandas as pd

def read_dataframe_from_blob(connection_string, container_name, blob_name):
    """
    Reads a CSV file from Azure Blob Storage and loads it into a Pandas DataFrame.
    
    :param connection_string: str - Azure Blob Storage connection string.
    :param container_name: str - The name of the container in Blob Storage.
    :param blob_name: str - The name of the blob (CSV file).
    :return: pd.DataFrame - The loaded DataFrame.
    """
    try:
        # Initialize BlobServiceClient
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        
        # Get the container client
        container_client = blob_service_client.get_container_client(container_name)
        
        # Download the blob content
        blob_client = container_client.get_blob_client(blob_name)
        blob_data = blob_client.download_blob().readall()
        
        # Convert the blob content to a DataFrame
        csv_data = StringIO(blob_data.decode('utf-8'))
        dataframe = pd.read_csv(csv_data)
        
        print(f"DataFrame loaded successfully from blob '{blob_name}' in container '{container_name}'!")
        return dataframe
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
