# Chat with a Website from URL - LangChain Chatbot with Streamlit GUI

Welcome to the GitHub repository for the LangChain Chatbot with Streamlit GUI! This project serves as a comprehensive guide to building a chatbot capable of interacting with websites, extracting information, and delivering a seamless conversational experience. By integrating LangChain with a Streamlit-powered user interface, the project ensures both functionality and accessibility for a wide range of users.

## Features

- **Website Interaction**: Harnesses the power of LangChain to interact with websites and extract relevant information.
- **Large Language Model Integration**: Fully compatible with state-of-the-art models such as GPT-4, Mistral, Llama2, and Ollama. This implementation uses GPT-4 by default, but you can easily swap it for another model.
- **Streamlit GUI**: Offers an intuitive and user-friendly graphical interface built with Streamlit.
- **Python-Based**: The entire project is written in Python for ease of understanding and customization.

## How RAG (Retrieval-Augmented Generation) Works

Retrieval-Augmented Generation (RAG) enhances the chatbot’s capabilities by "augmenting" its knowledge with external information. Here’s how it works:

1. **Text Vectorization**: All the text to be used as "augmented knowledge" is vectorized.
2. **Similarity Search**: The most relevant vectorized text is retrieved based on the user’s input.
3. **Prompt Augmentation**: This retrieved text is added to the chatbot’s prompt, providing the LLM with additional context.


## Installation

Ensure that Python is installed on your system. Then, follow these steps to set up the project:

1. Clone this repository:

```bash
git clone https://github.com/Shiv2116/RAG_Website_Chatbot
cd RAG_Website_Chatbot
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and include your API key:

```env
OPENAI_API_KEY=[your-openai-api-key]
```

## Running the Application

To launch the Streamlit app, run the following command in your terminal:

```bash
streamlit run app.py
```

This will start the application and open it in your default web browser.

## Contributing

Contributions are limited to bug fixes and typo corrections.

If you encounter any issues or have suggestions, feel free to open an issue in this repository.

## License

This project is licensed under the MIT License. For more details, refer to the LICENSE file included in the repository.

## Disclaimer

This project is designed for educational and research purposes only. Ensure you comply with the terms of use and guidelines of the APIs and services utilized in this project.


