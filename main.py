import os
from google.cloud import bigquery


def upload_data_to_gcs(data, context):
    client = bigquery.Client()
    dataset_id = os.environ["DATASET"]
    dataset_ref = client.dataset(dataset_id)
    job_config = bigquery.LoadJobConfig(autodetect=True)
    job_config.skip_leading_rows = 1
    job_config.source_format = bigquery.SourceFormat.CSV
    # get the URI for uploaded CSV in GCS from 'data'
    uri = "gs://" + os.environ["BUCKET"] + "/data_test.csv"
    # lets do this
    load_job = client.load_table_from_uri(
        uri, dataset_ref.table(os.environ["TABLE"]), job_config=job_config
    )
    print("Starting job {}".format(load_job.job_id))
    print("Function=csv_loader")
    print("File: data_test.csv")
    load_job.result()  # wait for table load to complete.
    print("Job finished.")
    destination_table = client.get_table(dataset_ref.table(os.environ["TABLE"]))
    print("Loaded {} rows.".format(destination_table.num_rows))
