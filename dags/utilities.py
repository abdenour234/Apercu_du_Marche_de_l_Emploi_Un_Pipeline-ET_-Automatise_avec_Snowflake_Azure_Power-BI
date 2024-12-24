import numpy as np 
import pandas as pd 
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