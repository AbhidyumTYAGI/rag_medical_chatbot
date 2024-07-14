# Nurse Joy: Your Personal Nurse

Welcome to **Nurse Joy**, the intelligent medical chatbot system designed to provide reliable answers to all your medical questions. Trained on comprehensive medical books, Nurse Joy offers precise and insightful responses to enhance your understanding of medical topics.

## Introduction

Nurse Joy is an advanced question-answering RAG system tailored for the medical community. Whether you are a healthcare professional or simply seeking medical attention, Nurse Joy helps you find answers to your medical queries quickly and efficiently.

## Screenshot

Here’s a preview of Nurse Joy:

![medical_Ch](https://github.com/Abhidyum/medical_ai_RAG/assets/94860032/781a16cd-b4bb-4706-bb7a-2ce46cc6f856)

## Features

- **Comprehensive Knowledge**: Uses a large number of authentic medical books to retrieve information.
- **Vector Database**: Utilizes Chroma vector database for efficient information retrieval based on semantic similarity.
- **Accurate Responses**: Provides precise answers to your medical questions.
- **User-Friendly Interface**: Easy to interact with and get the information you need.

## How RAG System Works

The Retrieval-Augmented Generation (RAG) system enhances the capabilities of a standard language model by integrating information retrieval directly into the generation process. Here's a simplified explanation of how it works:

1. **Query Understanding**: When you ask a question, the system first processes and understands your query using a pre-trained language model.

2. **Information Retrieval**: The system then retrieves relevant documents or passages from a large corpus of medical texts. This is done using a vector database, like Chroma, which retrieves information based on semantic similarity.

3. **Answer Generation**: The retrieved documents provide context for the language model to generate a precise and contextually relevant answer. The model combines the information from these documents with its pre-existing knowledge to produce a detailed response.

4. **Response Delivery**: Finally, the system delivers the generated response back to the user through the user-friendly interface.



## Tech Stack

- **Python**: Core programming language used for development.
- **Flask**: Web framework used to build the web application.
- **LangChain**: Library used to build the question-answering system.
- **Chroma**: Vector database used for efficient information retrieval.
- **Bootstrap**: Front-end framework for responsive web design.
- **jQuery**: JavaScript library used for DOM manipulation and AJAX requests.
- **Llama 2**: Pre-trained language model used for generating responses.
- **HTML/CSS**: Markup and styling for the web interface.


## Installation

To set up Nurse Joy on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Abhidyum/medical_ai_RAG.git
    cd medical_ai_RAG
    ```

2. **Download the quantized Llama 2 model**:
    Download `llama-2-7b-chat.ggmlv3.q4_0.bin` from the following link: [Llama 2 Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)
    
    Place the downloaded model file in the `model` directory of your project.

3. **Install the necessary dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application**:
    ```bash
    python app.py
    ```

## Usage

Once the application is running, you can start asking your medical questions directly through the interface. Here’s a simple example:

1. **Start the application**:
    ```bash
    python app.py
    ```

2. **Ask a question**:
    Enter your medical question in the input field and press enter or press the send button.
    
    Example:
    ```
    What are the symptoms of diabetes?
    ```

3. **Receive an answer**:
    Nurse Joy will process your question and provide a detailed answer.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to reach out to us:

- **Email**: tyagiabhidyum@gmail.com
- **GitHub**: [Abhidyum](https://github.com/Abhidyum)
