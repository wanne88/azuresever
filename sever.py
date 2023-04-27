from flask_cors import CORS
from flask import Flask, request, jsonify
from pyChatGPT import ChatGPT
import openai
app = Flask(__name__)
CORS(app)
@app.route('/')
def home():
    return 'Hello World!'

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    text = ChatGPT(data['prompt'], data['length'])
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run()
