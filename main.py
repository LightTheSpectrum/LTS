import os
from gtts import gTTS
import pygame

# Initialize pygame mixer
pygame.mixer.init()

def text_to_speech(text, lang='en'):
    # Convert text to speech
    tts = gTTS(text=text, lang=lang)
    tts.save("speech.mp3")

    # Play the speech
    pygame.mixer.music.load("speech.mp3")
    pygame.mixer.music.play()

    # Wait for the speech to finishff
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    print("AAC Device Simulation")
    print("Type 'exit' to quit")

    while True:
        text = input("Enter text: ")
        if text.lower() == 'exit':
            break
        text_to_speech(text)

    # Clean up
    if os.path.exists("speech.mp3"):
        os.remove("speech.mp3")

if __name__ == "__main__":
    main()