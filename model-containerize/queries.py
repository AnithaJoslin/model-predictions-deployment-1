input_query = """
    SELECT `mean radius`, `mean area`, `mean concave points`, 
    `mean fractal dimension`, `concavity error`, `concave points error`, 
    `worst radius`, `worst area`
    FROM elated-effect-464110-f2.breast_cancer_dataset.raw_data
    WHERE DATE(insert_date) >= (CURRENT_DATE - 1)
    """