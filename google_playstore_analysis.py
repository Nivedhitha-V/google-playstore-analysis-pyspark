# Importing PySpark libraries
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql.functions import *

# Start a Spark session (if not already running)
spark = SparkSession.builder.appName("GooglePlaystoreAnalysis").getOrCreate()

# Load the Google Playstore dataset from DBFS (uploaded manually in Databricks)
df = spark.read.load(
    'dbfs:/FileStore/tables/googleplaystore.csv',
    format='csv',
    sep=',',
    header=True,
    escape='"',
    inferSchema=True
)

# Count the total number of records
df.count()

# Preview the top 3 rows
df.show(3)

# Print schema to understand data types
df.printSchema()

# Drop unwanted columns that are not needed for analysis
df = df.drop("size", "Content Rating", "Last Updated", "Android Ver", "Current Ver")

# Check remaining columns
df.show(2)
df.printSchema()

# Clean and convert column data types for numerical analysis
df = df.withColumn("Reviews", col("Reviews").cast(IntegerType())) \
    .withColumn("Installs", regexp_replace(col("Installs"), "[^0-9]", "")) \
    .withColumn("Installs", col("Installs").cast(IntegerType())) \
    .withColumn("Price", regexp_replace(col("Price"), "[$]", "")) \
    .withColumn("Price", col("Price").cast(IntegerType()))

# Verify updated schema
df.printSchema()

# Show top 3 cleaned records
df.show(3)

# Create a temporary SQL view to run SQL queries in Databricks
df.createOrReplaceTempView("apps")

# ----------------------------
# Below are the SQL queries used in Databricks notebook (in %sql cells)
# ----------------------------

# Query 1: View all app data
%sql
SELECT * FROM apps

# Query 2: Top 10 apps with highest number of reviews
%sql
SELECT App, SUM(Reviews) AS total_reviews
FROM apps 
GROUP BY App 
ORDER BY total_reviews DESC 
LIMIT 10

# Query 3: Top 10 apps with highest installs (by app and type)
%sql
SELECT App, Type, SUM(Installs) AS Total_installs
FROM apps 
GROUP BY App, Type 
ORDER BY Total_installs DESC 
LIMIT 10

# Query 4: Total installs grouped by category
%sql
SELECT Category, SUM(Installs) AS Total_installs
FROM apps 
GROUP BY Category
ORDER BY Total_installs DESC

# Query 5: Paid apps with total price between 20 and 30 (wrong syntax noted — needs correction)
%sql
SELECT App, SUM(Price) AS price_total
FROM apps
WHERE Type = 'Paid'
GROUP BY App
HAVING price_total BETWEEN 20 AND 30
ORDER BY price_total DESC
