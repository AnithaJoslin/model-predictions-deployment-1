# model-predictions-deployment-1
The repository uses a trained model to predict the data and load predictionsto bigquery table.<br>
**Proposed architecture for the repository is:**<br>
Data Generator → Pub/Sub → Cloud Function → Vertex AI Endpoint → BigQuery
The repo has the following folders:<br>
**model-training** - This folder contains the model_training.ipynb file that has trained the model<br>
**model-containerize** - This folder contains <br>
- serve.py - uses a flask app to deploy the result based on inputs given
- test_model.ipynb - to test out the model
- example_cmds.md - This contains the example commands to give while the serve.py is running. The output is then obtained.