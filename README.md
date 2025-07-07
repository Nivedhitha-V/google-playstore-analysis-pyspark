
#  Google Playstore Data Analysis using PySpark (Databricks)

This project is a hands-on exploration of the Google Playstore dataset using **PySpark on Databricks**.  
It focuses on data cleaning, transformation, and analysis using both **PySpark APIs** and **Spark SQL** — perfect for beginners getting into **Data Engineering** tools and workflows.

---

##  Objective

To explore and analyze the Google Playstore dataset using PySpark and Spark SQL on Databricks, gaining familiarity with:

- Databricks platform & DBFS
- PySpark for data wrangling
- Running SQL queries over Spark DataFrames
- Cleaning real-world messy data
- Performing aggregations and transformations

---

##  Project files 

| File | Discription |
|------|-------------|
| `googleplaystore.csv` | Raw input sales data |
| `google_playstore_analysis.py` | Project code |

---

##  Tech Stack

-  **PySpark** (DataFrame API & SQL)
-  **Databricks Community Edition**
-  **Google Playstore Dataset** (from Kaggle, manually uploaded to DBFS)
-  **Python**

---

##  Project Workflow

1. **Data Loading**
   - Uploaded CSV to DBFS (`/FileStore/tables/`)
   - Loaded using `spark.read.load()` with schema inference

2. **Data Cleaning**
   - Dropped irrelevant columns
   - Removed symbols from `Installs` and `Price`
   - Casted `Reviews`, `Installs`, `Price` to IntegerType

3. **Temporary View**
   - Created a Spark SQL view using `createOrReplaceTempView("apps")`

4. **SQL Queries Run in Databricks**
   - Top apps by reviews
   - Top apps by installs (grouped by type)
   - Installs per category
   - Paid apps with price total between 20 and 30

---

## Connect

This project demonstrates foundational Data Engineering skills, from raw file ingestion to clean, analysed output.

Feel free to **star** the repo or **fork** for practice or extension!

Made with 💙 by Nivedhitha V 
[Github](https://github.com/Nivedhitha-V)
[Email](nivedhithav0407@gmail.com)
[LinkedIn](https://www.linkedin.com/in/nivedhitha-v/)
