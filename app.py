from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS  
from gtts import gTTS
from groq import Groq
import os

app = Flask(__name__)


CORS(app)

api_key = "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" 
client = Groq(api_key=api_key)

AUDIO_DIR = "static/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

def process_transcript_with_groq(transcript_text):
    try:
        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[
                {
                    "role": "user",
                    "content": (
                        "It's the content:\n" + transcript_text + "\nProvide me a good answer to this as if it's a conversation between two. You are a conversational assistant. Use short, conversational responses as if you're having a live conversation.\n Your response should be concise no more than 20 words."
                    ),
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        text_generated = completion.choices[0].message.content
        return text_generated
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def text_to_speech(text, filename="response.mp3"):
    tts = gTTS(text=text, lang='en', slow=False)
    filepath = os.path.join(AUDIO_DIR, filename)  
    tts.save(filepath)
    return filename


@app.route('/process_transcript', methods=['POST'])
def process_transcript():
    transcript = request.json.get('transcript')
    
    if not transcript:
        return jsonify({"error": "No transcript provided"}), 400
    
    generated_text = process_transcript_with_groq(transcript)
    
    if generated_text:
        
        audio_filepath = text_to_speech(generated_text)
        return jsonify({
            "generated_text": generated_text,
            "audio_file": audio_filepath
        })
    else:
        return jsonify({"error": "Failed to generate response"}), 500

@app.route('/audio/<filename>')
def serve_audio(filename):
    return send_from_directory(AUDIO_DIR, filename)

if __name__ == '__main__':
    app.run(debug=True)
