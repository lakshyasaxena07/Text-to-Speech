from gtts import gTTS
import os

# Function to convert text to speech
def text_to_speech(text, language='en'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Save the audio file
    tts.save("output.mp3")
    
    # Optionally, play the audio file (works on Windows)
    os.system("start output.mp3")  


if __name__ == "__main__":
    # Take input from the user
    text = input("Please enter the text you want to convert to speech: ")
    text_to_speech(text)
