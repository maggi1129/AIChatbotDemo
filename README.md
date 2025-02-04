# DSA Chatbot

A Python-based chatbot that helps users learn Data Structures and Algorithms (DSA) concepts through interactive conversations. The chatbot uses the OpenAI API through LangDB to provide detailed explanations and answers to DSA-related questions.

## Features

- Interactive command-line interface
- Specialized in DSA education
- Clear and simple explanations with analogies
- Basic conversation handling (greetings, farewells)
- Error handling for API calls
- Customizable response parameters

## Prerequisites

Before running the chatbot, make sure you have:

- Python 3.6 or higher installed
- pip (Python package installer)
- An active internet connection

## Installation

1. Clone this repository or download the source code:

```bash
git clone https://github.com/yourusername/dsa-chatbot.git
```

2. Navigate to the project directory:

```bash
cd dsa-chatbot
```

3. Install the required package:

```bash
pip install openai
```

## Usage

1. Run the chatbot:

```bash
python chatbot.py
```

2. Start interacting with the chatbot:
   - Type your DSA-related questions
   - Use 'hello' for greetings
   - Type 'bye' to exit the chat

Example questions you can ask:
- "Explain DP to a 5 year old"
- "What is a binary search tree?"
- "How does quicksort work?"
- "Explain time complexity"

## Configuration

The chatbot uses the following configuration:
- Model: gpt-4o-mini
- Temperature: 0.7 (controls response creativity)
- Max tokens: 300 (limits response length)
- Top p: 1.0 (uses nucleus sampling)

## Project Structure

```
dsa-chatbot/
│
├── chatbot.py          # Main chatbot implementation
├── README.md           # Project documentation
└── requirements.txt    # Project dependencies
```

## API Configuration

The chatbot uses LangDB API with the following configuration:
- API Base URL: https://api.us-east-1.langdb.ai
- Project ID: Configured in the code
- API Key: Configured in the code

## Customization

You can customize the chatbot by:
1. Modifying the `basic_responses` dictionary in the `DSAChatbot` class
2. Adjusting the system prompt in the `get_response` method
3. Changing the model parameters (temperature, max_tokens, etc.)
4. Adding new features or response types

## Error Handling

The chatbot includes basic error handling for API calls and will display any errors encountered during operation.

## Contributing

Feel free to fork this project and submit pull requests with improvements. Some areas for potential enhancement:
- Adding a graphical user interface
- Implementing conversation history
- Adding more specialized DSA topics
- Improving error handling
- Adding unit tests

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for the API
- LangDB for API access
- Contributors and maintainers

## Support

For support, please:
1. Check the existing documentation
2. Create an issue in the repository
3. Contact the maintainers

---

**Note**: Make sure to keep your API keys secure and never commit them directly to version control.

