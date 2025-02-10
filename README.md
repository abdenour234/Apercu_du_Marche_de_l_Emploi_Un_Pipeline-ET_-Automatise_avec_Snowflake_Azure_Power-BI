# ETL Project : Job Data Pipeline

## 📌 Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Tools Used](#tools-used)
- [Project Steps](#project-steps)
  - [Step 1: Data Extraction](#step-1-extraction-des-données)
  - [Step 2: Data Transformation](#step-2-transformation-des-données)
  - [Step 3: Data Loading into Snowflake](#step-3-chargement-des-données)
  - [Step 4: Reporting with Power BI](#step-4-visualisation-des-données)
- [Acknowledgment](#acknowledgment)


## 🎯 Introduction
This README document provides an overview of an ETL (Extract, Transform, Load) project developed to extract job market data from an API, transform it using Python and Pandas, load the cleaned data into Snowflake, and create a reporting dashboard using Power BI.

## 🏗️ Project Overview
The goal of this project is to automate the collection and processing of job postings related to Data Science and Data Engineering roles in Morocco. The  data is stored in Snowflake and visualized in Power BI, enabling insights into job market trends.

## 🛠️ Tools Used
- **Python** : Used for scripting and data manipulation.
- **Pandas** : Employed for data transformation and cleaning.
- **Scipy/Regular Expression** : Used for extracting relevent informations from Job's Description.
- **Azure Blob Storage** :  Used for storing raw and cleaned datasets.
- **Docker** : Used for Creating Isolated Environment For our Project .
- **Azure Vm** : Used for hosting and runing our containers.
- **Snowflake Data Warehouse** : The central repository for gold data.
- **Snowpipe** : Used for Automating Data Ingestion into Snowflake. 
- **Apache Airflow** : : Manages and automates the ETL pipeline.
- **Power BI** : : Creates interactive dashboards and reports.

## 📌 Project Steps

### 🛠 Step 1: Data Extraction

✅ The job market data is extracted from the API https://linkedin-data-scraper.p.rapidapi.com/search_jobs.

✅The API fetches job postings related to Data Science and Data Engineering roles in Morocco.

✅The extracted data is stored in **Azure Blob Storage in the Bronze Layer**. 

### 🔄 Step 2: Data Transformation  

✅ The extracted raw data is processed using Python and Pandas.  

✅ Key tasks include:  

   - Handling missing values and removing duplicate job postings.  
   - Normalizing text fields and standardizing date formats.  
   - Applying NLP techniques to extract relevant information from job descriptions, such as required **skills** (Cloud technologies, programming languages, frameworks).  

✅ The transformed data is saved in **Azure Blob Storage (Silver Layer).**

### 📥 Step 3: Data Loading into Snowflake  

✅ **Configuring Snowflake & Snowpipe:**  
   - **Snowflake** and **Snowpipe** were configured for automated data ingestion.  
   - **Event-driven ingestion:** Snowpipe listens for events in **Azure Blob Storage (Gold Layer)** and automatically ingests new data into **Snowflake** upon updates.  

✅ **Data Loading:**  
   - Additional cleaning is performed before loading the data into **Snowflake**.  
   - The cleaned data is stored in the **Gold Layer** of the data pipeline.  

✅ **Snowflake Ingestion & Transformation:**  
   - **Flattening nested data:** Some fields contained lists, which were flattened in **Snowflake** to ensure a structured format.  
   - **Creating standardized views:** A new view was created in Snowflake to provide a **clean, structured, and standardized** version of the job postings for analytics and reporting.

### 📊 Step 4: Reporting with Power BI  

✅ **Report Creation:**  
   - Designed **interactive dashboards** to visualize key job market insights.  
   - Tracked **KPIs** such as demand for specific skills, job trends, and company hiring patterns.  

✅ **Data Integration:**  
   - Connected **Power BI** to **Snowflake** for real-time reporting.  
   - Utilized **optimized queries and data models** to enhance performance.  

✅ **Business Insights:**  
   - Provided **actionable insights** for recruiters and job seekers.  
   - Enabled dynamic filtering and drill-down capabilities for deeper analysis.


## 🎨 Data Pipeline
andero schema dyl projet dylna 

## 🔍 Dashboard
ta nderoh 

## 🙏 Acknowledgment  

We would like to acknowledge the following resources that contributed to the success of this project:  

- **Official Documentation:**  
  - Apache Airflow  
  - Snowflake  
  - Microsoft Azure  

- **Community Forums & Blogs:**  
  - Stack Overflow  
  - Medium articles  
  - Snowflake and Azure community discussions
 
- **ChatGpt/DeepSeek/ClaudAi**
   - They were our project Encadrants

These resources provided valuable guidance and best practices throughout the development process.

