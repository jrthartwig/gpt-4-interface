import os
from azure.storage import AzureStorage
from azure.function import AzureFunction
from openai.gpt4 import GPT4
from openai.training import Training
from utils.data_cleaning import DataCleaning
from utils.data_formatting import DataFormatting

def main():
    # Initialize Azure Storage
    storage_account_name = os.getenv('STORAGE_ACCOUNT_NAME')
    storage_account_key = os.getenv('STORAGE_ACCOUNT_KEY')
    azure_storage = AzureStorage(storage_account_name, storage_account_key)

    # Initialize Azure Function
    function_name = os.getenv('FUNCTION_NAME')
    function_key = os.getenv('FUNCTION_KEY')
    azure_function = AzureFunction(function_name, function_key)

    # Initialize OpenAI GPT-4
    openai_api_key = os.getenv('OPENAI_API_KEY')
    gpt4 = GPT4(openai_api_key)

    # Initialize Training
    training = Training()

    # Initialize Data Cleaning and Formatting
    data_cleaning = DataCleaning()
    data_formatting = DataFormatting()

    # Main workflow
    while True:
        # Check for new documents in Azure Storage
        new_documents = azure_storage.check_new_documents()

        for document in new_documents:
            # Download the document
            raw_data = azure_storage.download_document(document)

            # Clean the data
            cleaned_data = data_cleaning.clean(raw_data)

            # Format the data
            formatted_data = data_formatting.format(cleaned_data)

            # Train the GPT-4 model
            model = training.train(formatted_data)

            # Generate response using GPT-4
            response = gpt4.generate_response(model)

            # Upload the response to Azure Storage
            azure_storage.upload_response(document, response)

        # Trigger Azure Function to process new documents
        azure_function.trigger()

if __name__ == "__main__":
    main()