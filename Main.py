from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import os

# Initialize the Flask application
app = Flask(__name__, static_folder='static')

# Define the Text-to-Speech endpoint
@app.route('/tts', methods=['POST'])
def text_to_speech():
    # Parse the JSON data from the request
    data = request.get_json()
    text = data.get('text')  # Get the text from the JSON payload
    language = data.get('language', 'en-in')  # Get the language, default to 'en-in'
    
    # Check if text is provided
    if not text:
        return jsonify({'error': 'No text provided'}), 400  # Return error if text is missing
    
    # Convert the text to speech using gTTS
    tts = gTTS(text)
    tts.save('output.mp3')  # Save the output as an MP3 file
    
    # Send the MP3 file as a downloadable response
    return send_file('output.mp3', as_attachment=True)

# Define the route for the frontend
@app.route('/')
def index():
    # Serve the static HTML file (index.html) from the static folder
    return app.send_static_file('index.html')

# Entry point of the application
if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True)
