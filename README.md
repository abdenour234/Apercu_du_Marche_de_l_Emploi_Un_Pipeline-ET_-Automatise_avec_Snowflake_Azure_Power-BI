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
- **Azure Blob Storage** :  Used for storing raw and cleaned datasets.
- **Snowflake Data Warehouse** : The central repository for gold data
- **Apache Airflow** : : Manages and automates the ETL pipeline.
- **Power BI** : : Creates interactive dashboards and reports.

## 📌 Project Steps

### 🛠 Step 1: Data Extraction

✅ The job market data is extracted from the API https://linkedin-data-scraper.p.rapidapi.com/search_jobs.

✅The API fetches job postings related to Data Science and Data Engineering roles in Morocco.

✅The extracted data is stored in Azure Blob Storage in the Bronze Layer. 

### 🔄 Step 2: Data Transformation


✅The extracted raw data is processed using Python and Pandas.

✅Key tasks include:

   - Removing duplicate job postings.

   - Normalizing text fields.

   - Handling missing values.

   - Standardizing date formats.

✅The cleaned data is saved in Azure Blob Storage (Silver Layer).

### 📥 Step 3: Data Loading into Snowflake
✅The transformed data is loaded into Snowflake using Python and SQL queries.

✅Snowflake acts as the central repository for the structured job postings.

✅Data is stored in the Gold Layer of the data pipeline.

### 📊 Step 4: Reporting with Power BI


## 🎨 Data Pipeline
andero schema dyl projet dylna 

## 🔍 Dashboard
ta nderoh 

## 🙏 Acknowledgment
les resources : documentation airflow , snowflkae, azure ..

