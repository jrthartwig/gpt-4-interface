from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def create_blob_service_client(storage_connection_string):
    """
    Create a BlobServiceClient using a connection string.
    """
    blob_service_client = BlobServiceClient.from_connection_string(storage_connection_string)
    return blob_service_client

def upload_document_to_blob(blob_service_client, container_name, blob_name, document):
    """
    Upload a document to a blob.
    """
    # Get a reference to the container
    container_client = blob_service_client.get_container_client(container_name)

    # Get a reference to the blob
    blob_client = container_client.get_blob_client(blob_name)

    # Upload the document
    with open(document, "rb") as data:
        blob_client.upload_blob(data)

def download_document_from_blob(blob_service_client, container_name, blob_name, download_path):
    """
    Download a document from a blob.
    """
    # Get a reference to the container
    container_client = blob_service_client.get_container_client(container_name)

    # Get a reference to the blob
    blob_client = container_client.get_blob_client(blob_name)

    # Download the document
    with open(download_path, "wb") as download_file:
        download_file.write(blob_client.download_blob().readall())