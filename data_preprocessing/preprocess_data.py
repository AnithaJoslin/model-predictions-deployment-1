from google.cloud import bigquery
from google.cloud import pubsub_v1
import queries

def publish_trigger(project_id, topic_id, publisher):
    topic_path = publisher.topic_path(project_id, topic_id)
    message = 'Trigger prediction job'
    future = publisher.publish(topic_path, message.encode("utf-8"))
    print(f"Published message ID: {future.result()}")
    
def preprocess_data(client):
    df = client.query(queries.input_query).to_dataframe()

if __name__ == '__main__':
    
    try: 
        client = bigquery.Client()
        preprocess_data(client)
        project_id = "elated-effect-464110-f2"
        topic_id = "data-ingestion"
        publisher = pubsub_v1.PublisherClient()
        publish_trigger(project_id, topic_id, publisher)
    except Exception as e:
        print(e)