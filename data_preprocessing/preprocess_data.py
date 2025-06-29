from google.cloud import bigquery

client = bigquery.Client()

query = """
INSERT INTO `elated-effect-464110-f2.breast_cancer_dataset.input_data`
SELECT `mean radius`, `mean area`, `mean concave points`, `mean fractal dimension`, 
`concavity error`, `concave points error`, `worst radius`, `worst area`, insert_timestamp
FROM `elated-effect-464110-f2.breast_cancer_dataset.raw_data`
WHERE DATE(insert_timestamp) >= (CURRENT_DATE - 1)
"""
df = client.query(query).to_dataframe()