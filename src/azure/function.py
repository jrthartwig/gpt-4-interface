import os
import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient
from ..openai.gpt4 import process_document

def main(myblob: func.InputStream):
    try:
        # Get connection string from app settings
        connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')

        # Create the BlobServiceClient object
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)

        # Get the blob client for the input blob
        blob_client = blob_service_client.get_blob_client(os.getenv('AZURE_STORAGE_CONTAINER_NAME'), myblob.name)

        # Download the blob content
        logging.info(f"Processing file: {myblob.name}")
        blob_content = blob_client.download_blob().readall()

        # Send the document content to OpenAI API for processing
        response = process_document(blob_content)

        # Log the response from OpenAI API
        logging.info(f"Response from OpenAI API: {response}")

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")