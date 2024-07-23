from flask import Flask, request, jsonify
from langchain_community.llms import Ollama

app = Flask(__name__)

# Set up the connection to the local model server
ollama = Ollama(base_url='http://localhost:11434', model="llama3")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    input_text = data.get("text", "")
    response = ollama(input_text)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
