import tkinter as tk
from gtts import gTTS
import os
from PIL import Image, ImageTk
import pygame


# Initialize pygame mixer
pygame.mixer.init()

def text_to_speech(text, lang='en'):

     # Clean up
    try:
            if os.path.exists("speech.mp3"):
                pygame.mixer.music.unload()  # Ensure the file is not in use
                os.remove("speech.mp3")
    except PermissionError as e:
            print(f"Error: {e}")


    # Convert text to speech
    tts = gTTS(text=text, lang=lang)
    tts.save("speech.mp3")

    # Play the speech
    pygame.mixer.music.load("speech.mp3")
    pygame.mixer.music.play()


    # Wait for the speech to finishff
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
             # Clean up
   

# Define phrases and associated image paths
buttons_data = [
    [("Up", "up.png"), ("Yes", "yes.png"), ("Good", "good.png")]
]

# Define phrases
phrases = [
    {"text": "up", "image": "up.png"},
    {"text": "good", "image": "good.png"},
    {"text": "yes", "image": "yes.png"},
]



class AACDevice:
    def __init__(self, root):
        self.root = root
        self.root.title("AAC Device")
        self.image_path = "icons\images"  # Base path for images
        self.create_buttons()
        
          # Create a PanedWindow
        self.paned_window = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.paned_window.grid(row=2, column=2, padx=5, pady=5) 

        # Create a frame for the textbox
        self.textbox_frame = tk.Frame(self.paned_window)
        self.paned_window.add(self.textbox_frame, width=300, height=100)

        # Create a frame for the buttons
        self.buttons_frame = tk.Frame(self.paned_window)
        self.paned_window.add(self.buttons_frame)


        # Create a textbox for constructing sentences
        self.textbox = tk.Text(self.root, height=2, width=50)
        self.textbox.grid(row=2, column=2, columnspan=3, padx=5, pady=5)
     
    
    def append_text(self, text):
         self.textbox.insert(tk.END, text + " ")
        

   
     
       # os.system("mpg321 speech.mp3" if os.name != "nt" else "start speech.mp3")

    def handle_button_click(self, text):
        self.append_text(text)
        text_to_speech(text)
 
    def create_buttons(self):
        for row_idx, row in enumerate(buttons_data):
            for col_idx, (phrase, image_file) in enumerate(row):
                img_path = os.path.join(self.image_path, image_file)
                try:
                    img = Image.open(img_path).resize((50, 50), Image.LANCZOS)
                    img = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f"Error loading image {img_path}: {e}")
                    continue
                button = tk.Button(self.root, text=phrase, image=img, compound="top",
                                   command=lambda text=phrase: self.handle_button_click(text) , height=100, width=100)
                button.image = img  # Keep a reference to avoid garbage collection
                button.grid(row=row_idx, column=col_idx, padx=5, pady=5)
    


if __name__ == "__main__":
    root = tk.Tk()
    app = AACDevice(root)
    root.mainloop()