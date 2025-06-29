from google.cloud import bigquery
import queries
import os
import numpy as np
import joblib


def load_model():
    model = joblib.load('model.pkl')
    return model

def read_data(client):
    input_data = client.query(queries.input_query).to_dataframe()
    return input_data


def predict_result(client):
    dataset = read_data(client)
    feature_array = np.array(list(dataset.values))
    model = load_model()
    dataset['predictions'] = model.predict(feature_array).tolist()
    return dataset

def insert_into_BQ_table(client):
    final_dataset = predict_result(client)
    final_dataset['predictions'] = final_dataset['predictions'].astype(bool)
    schema = []
    for col in final_dataset:
        if col == 'predictions':
            schema.append(bigquery.SchemaField(col, "BOOLEAN"))
            continue
        schema.append(bigquery.SchemaField(col, "FLOAT64"))
    job = client.insert_rows_from_dataframe('elated-effect-464110-f2.breast_cancer_dataset.final_table', 
                                 final_dataset,
                                 schema)
    return None

if __name__ == '__main__':
    client = bigquery.Client()
    try: 
        insert_into_BQ_table(client)
        print("Successfully done!")
    except Exception as e:
        print(e)

