import openai
import os

# Load your OpenAI API key from an environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def process_document(document_text):
    """
    This function sends a document to the OpenAI API for processing.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=document_text,
            max_tokens=100
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"An error occurred while processing the document: {e}")
        return None

def fine_tune_model(training_data):
    """
    This function fine-tunes the GPT-4 model with the provided training data.
    """
    try:
        # Fine-tuning code goes here
        # Note: OpenAI currently does not support fine-tuning of the GPT-4 model via the API
        pass
    except Exception as e:
        print(f"An error occurred while fine-tuning the model: {e}")