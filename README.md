# Speech-to-Chat Assistant

This project is a Speech-to-Chat Assistant that converts user speech to text, processes it using the Groq API, generates a conversational response, and provides an audio output using Text-to-Speech (TTS).

## Features
- Real-time speech-to-text transcription.
- Processed responses via the Groq conversational AI API.
- Text-to-Speech output of responses using gTTS.
- Web-based user interface for interaction.

## Project Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Install Dependencies
Run the following command to install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 3. Setup Groq API Key
Replace the `api_key` variable in the Flask backend (`app.py`) with your Groq API key:
 In this case my API key is available so no need to change.
```python
api_key = "your_groq_api_key"
```

### 4. Run the Flask Backend
Start the Flask server:
```bash
python app.py
```
By default, the Flask server will run on `http://localhost:5000`.

### 5. Open the Web Interface
Open the `voice_bot.html` file in your browser by double click, or host it using a simple HTTP server for better performance:
```bash
python -m http.server 8000
```
Then navigate to `http://localhost:8000` in your browser.

## Usage
1. Allow microphone access when prompted.
2. Speak into the microphone.
3. Wait for the transcription to appear in the chat interface.
4. The assistant will respond with a text reply and play the corresponding audio response.

## Dependencies
- Flask
- Flask-Cors
- gTTS
- groq


