import json

def format_data_for_openai(input_data):
    """
    This function takes in raw data and formats it according to OpenAI's guidelines.
    The input data should be a list of dictionaries, where each dictionary represents a document.
    Each dictionary should have two keys: 'content' and 'summary'.
    'content' is the main text of the document, and 'summary' is a brief summary or abstract of the document.
    The function returns a string that is ready to be used for training a GPT-4 model.
    """
    formatted_data = ""
    for document in input_data:
        content = document['content']
        summary = document['summary']
        formatted_data += f"Document: {content}\nSummary: {summary}\n"
    return formatted_data

def save_formatted_data(formatted_data, output_file_path):
    """
    This function takes in formatted data and an output file path.
    It saves the formatted data to the output file in plain text format.
    """
    with open(output_file_path, 'w') as output_file:
        output_file.write(formatted_data)

def load_data(input_file_path):
    """
    This function takes in an input file path.
    It loads the data from the input file and returns it.
    The data in the input file should be in JSON format.
    """
    with open(input_file_path, 'r') as input_file:
        data = json.load(input_file)
    return data

def format_and_save_data(input_file_path, output_file_path):
    """
    This function takes in an input file path and an output file path.
    It loads the data from the input file, formats it, and saves it to the output file.
    """
    data = load_data(input_file_path)
    formatted_data = format_data_for_openai(data)
    save_formatted_data(formatted_data, output_file_path)