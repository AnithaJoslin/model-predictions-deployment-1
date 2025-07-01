input_query = """
INSERT INTO `elated-effect-464110-f2.breast_cancer_dataset.input_data`
SELECT `mean radius`, `mean area`, `mean concave points`, `mean fractal dimension`, 
`concavity error`, `concave points error`, `worst radius`, `worst area`, insert_date
FROM `elated-effect-464110-f2.breast_cancer_dataset.raw_data`
WHERE DATE(insert_date) >= (CURRENT_DATE - 1)
"""