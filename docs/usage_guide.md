# Usage Guide

This document provides a step-by-step guide on how to use the GPT-4 Interface for Business Development. 

## Prerequisites

Before you start, ensure you have the following:

- Python 3.7 or later installed on your machine.
- An Azure account with the necessary permissions to create and manage resources.
- An OpenAI account with an API key.

## Setup

1. Clone the repository to your local machine.

2. Navigate to the project directory:

    ```
    cd gpt-4-interface
    ```

3. Install the required Python libraries:

    ```
    pip install -r requirements.txt
    ```

4. Set up your Azure and OpenAI credentials as environment variables. Replace `your_azure_storage_connection_string`, `your_azure_function_name`, and `your_openai_api_key` with your actual credentials.

    ```
    export AZURE_STORAGE_CONNECTION_STRING=your_azure_storage_connection_string
    export AZURE_FUNCTION_NAME=your_azure_function_name
    export OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

1. To start the application, run the following command:

    ```
    python src/main.py
    ```

2. Upload your documents to the Azure Blob Storage account. The application will automatically detect new documents and send them for processing.

3. The AI-generated responses will be stored in the same Azure Blob Storage account. You can download and review them at your convenience.

## Feedback

If you have any feedback on the AI-generated responses, please provide it through the feedback system implemented in the application. Your feedback is crucial for the continuous improvement of the AI model.

## Troubleshooting

If you encounter any issues while using the application, please refer to the `troubleshooting.md` document in the `docs` directory. If the issue persists, please contact the support team.

Remember to always keep your Azure and OpenAI credentials confidential to prevent unauthorized access to your resources.