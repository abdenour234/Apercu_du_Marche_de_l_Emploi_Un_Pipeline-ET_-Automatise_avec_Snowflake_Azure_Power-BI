
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


