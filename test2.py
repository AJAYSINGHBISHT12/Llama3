from flask import Flask, request, send_file
from langchain_community.llms import Ollama
from gtts import gTTS
import io

app = Flask(__name__)

# Set up the connection to the local model server
ollama = Ollama(base_url='http://localhost:11434', model="llama3")

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    input_text = data.get("text", "")
    response_text = ollama(input_text)
    
    # Convert text response to audio
    tts = gTTS(text=response_text, lang='en')
    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)
    
    # Send audio file
    return send_file(audio_file, mimetype='audio/mpeg', as_attachment=True, download_name='response.mp3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
