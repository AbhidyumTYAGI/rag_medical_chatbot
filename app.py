from flask import Flask, render_template, request, jsonify
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import CTransformers
from utils import load_pdf, text_split, setup_vector_store, load_vector_store, vector_store_exists


app = Flask(__name__)


# Set up the vector store and retriever
data_directory = 'data'  # Directory where your PDFs are stored
persist_directory = 'dbase'  # Directory for vector database storage

if vector_store_exists(persist_directory):
    vectordb = load_vector_store(persist_directory)
else:
    extracted_data = load_pdf(data_directory)
    text_chunks = text_split(extracted_data)
    vectordb = setup_vector_store(text_chunks, persist_directory)

retriever = vectordb.as_retriever(search_kwargs={'k': 1})

prompt_template = """
You are nurse Joy a medical chatbot.
Use the following pieces of information to answer the user's question.
If you want more details, just ask from the user.
Do not try to make answer, If you dont know, just say I don't know.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain_type_kwargs = {"prompt": PROMPT}

llm = CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin", model_type="llama", config={'max_new_tokens': 512, 'temperature': 0.8})
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True, chain_type_kwargs=chain_type_kwargs)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get', methods=['POST'])
def get_bot_response():
    user_message = request.form['msg']
    context = request.form['context']

    # Process user input and generate bot response
    result = qa({"query": user_message, "context": context})
    answer = result.get('result', 'No answer found.')

    # Update context with the current interaction
    context += f"\nYou: {user_message}\nNurse Joy: {answer}\n"

    return jsonify(answer)

if __name__ == '__main__':
    app.run(debug=True)
