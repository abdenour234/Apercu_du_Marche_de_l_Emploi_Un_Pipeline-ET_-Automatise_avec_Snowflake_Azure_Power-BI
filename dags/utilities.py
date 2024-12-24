import pandas as pd
import numpy as np
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