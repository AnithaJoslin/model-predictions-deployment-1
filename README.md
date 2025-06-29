# model-predictions-deployment-1
The repository uses a trained model to predict the data and load predictionsto bigquery table.<br>
**Proposed architecture for the repository is:**<br>
Data Preprocessor -> Model predictions -> Output to BigQuery table
The repo has the following folders:<br>
**model-training** - This folder contains the model_training.ipynb file that has trained the model<br>
**model-containerize** - This folder contains <br>
- predict.py - Reads in the processed data from the table for the entire day, predicts the results and appends the final_table with the features and results
- queries.py - Contains the query to read in the input data for the whole day
- model.pkl - The trained model
- Dockerfile, requirements.txt - To containerise the model
**data_preprocessing** - This folder is used for preprocessing <br>
- create_BQ_table.ipynb - The notebook used to create all the BQ tables used in this project
- preprocess_data.py - Currently a simple file that just inserts the required columns into input_table. This will further be modified for more complex preprocessing