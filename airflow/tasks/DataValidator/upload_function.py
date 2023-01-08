from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import pandas as pd

def upload_to_storage(clean_data: dict, storage_url:str, container_name:str, data_level: str, gender: str):

    df = pd.DataFrame(clean_data)

    azure_credentials = DefaultAzureCredential()
    upload_file_path = rf"{data_level}\product-{gender}-{data_level}.csv"
    blob_service_client = BlobServiceClient(f"{storage_url}",credential=azure_credentials)
    blob_client = blob_service_client.get_blob_client(
        container=container_name, blob=upload_file_path
    )

    try:
        output = df.to_csv(index=False, sep=";", encoding="utf-8")
    except Exception as e:
        print(e)

    try:
        blob_client.upload_blob(output, blob_type="BlockBlob",overwrite=True)
    except Exception as e:
        print(e)
