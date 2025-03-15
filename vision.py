import tkinter as tk
from gtts import gTTS
import os
from PIL import Image, ImageTk

# Define phrases and associated image paths
buttons_data = [
    [("Finished", "finish.png"), ("Up", "up.png"), ("Yes", "yes.png"), ("Good", "good.png")]
]


# Define phrases
phrases = [
            {"text": "up", "image": "up.png"},
            {"text": "good", "image": "good.png"},
            {"text": "finish", "image": "finish.png"},
        ]



class AACDevice:
    def __init__(self, root):
        self.root = root
        self.root.title("AAC Device")
        self.image_path = "/icons/images"
        
         # Maximize the window
        self.root.state('zoomed')

        # Create a textbox for constructing sentences
        self.textbox = tk.Text(self.root, height=2, width=50)
        self.textbox.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        self.create_buttons()
     
    
     # Function to speak text
    def speak(self, text):
        tts = gTTS(text=text, lang='en')
        tts.save("speech.mp3")
        os.system("mpg321 speech.mp3" if os.name != "nt" else "start speech.mp3")

    def create_buttons(self):

        for row_idx, row in enumerate(buttons_data):
            for col_idx, (phrase, image_path) in enumerate(row):
                img = Image.open(image_path).resize((50, 50))
                img = img.resize((50, 50), Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)

                button = tk.Button(self.root,text=phrase["text"], image=img, compound="top",
                                   command=lambda p=phrase: self.speak(p["text"]), height=100, width=100)
                button.image = img  # Keep a reference to avoid garbage collection
                button.grid(row=row_idx, column=col_idx, padx=5, pady=5)
                button.pack(pady=50)




if __name__ == "__main__":
    root = tk.Tk()
    app = AACDevice(root)
    root.mainloop()
