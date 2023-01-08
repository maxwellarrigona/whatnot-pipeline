from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

def files_list(storage_url:str, container_name:str, data_level:str):

    default_credential = DefaultAzureCredential()
    blob_service_client = BlobServiceClient(f"{storage_url}",credential=default_credential)

    blob_container_client = blob_service_client.get_container_client(f"{container_name}")
    blob_list = blob_container_client.list_blobs(name_starts_with=f"{data_level}")
    files = []
    for blob in blob_list:
        if "/" in blob.name:
            start_position = blob.name.find("/") + 1
            name = blob.name[start_position::]
            files.append(name)
        else:
            pass

    return files
