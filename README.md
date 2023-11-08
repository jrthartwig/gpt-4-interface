# GPT-4 Interface for Business Development

This project provides a custom GPT-4 interface for business development where team members can drop documents into a folder for training. The system uses Azure Storage and Azure Functions for document handling, and the OpenAI API for AI model training and generation.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or higher
- An Azure account with an active subscription
- OpenAI API key

### Installation

1. Clone the repository to your local machine:

```
git clone https://github.com/yourusername/gpt-4-interface.git
```

2. Navigate to the project directory:

```
cd gpt-4-interface
```

3. Install the required Python libraries:

```
pip install -r requirements.txt
```

## Usage

1. Upload your documents to the specified Azure Blob Storage account.

2. Run the main script:

```
python src/main.py
```

The script will automatically detect new documents, send them for processing to the OpenAI API, and store the AI-generated responses.

## Testing

To run the unit tests, use the following command:

```
python -m unittest discover tests
```

## Documentation

For more detailed instructions on how to use the system and troubleshoot common issues, please refer to the `docs/usage_guide.md` and `docs/troubleshooting.md` files.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Acknowledgments

- OpenAI for providing the GPT-4 API
- Microsoft Azure for the cloud infrastructure

## Contact

If you have any questions, feel free to contact us.