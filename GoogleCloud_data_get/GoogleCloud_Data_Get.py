from google.cloud import bigquery
import pandas as pd


# Initialize BigQuery client
client = bigquery.Client()
print("BigQuery authentication successful!")

# Query entire dataset
query = "SELECT * FROM `bigquery-public-data.cms_medicare.inpatient_charges_2014`"

# Execute query and store as DataFrame
df = client.query(query).to_dataframe()

# Save as CSV
df.to_csv("medicare_data.csv", index=False)
print("Medicare dataset downloaded successfully!")