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
                print(f"Removed existing speech.mp3")
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
buttons_home_set_main = [
    [("All done", "alldone.png"), ("Yes", "yes.png"), ("Good", "good.png")],
    [("Help", "help.png"), ("Stop", "stop.png"), ("Go", "go.png"), ("Eat", "eat.png")]   
]

# Define phrases and associated image paths
buttons_home_set1 = [
    [("More", "more.png"), ("Not OK", "no.png"), ("Good", "good.png"),("More", "more.png")]
]

# Define phrases and associated image paths
buttons_emotion_set2 = [
    [("Happy", "happy.png"), ("Sad", "sad.png"),("Mad", "mad.png"),("Scared","scared.png")]
]

# Define phrases
phrases = [
    {"text": "up", "image": "alldone.png"},
    {"text": "good", "image": "good.png"},
    {"text": "yes", "image": "yes.png"},
]



class AACDevice:
    def __init__(self, root):
        self.root = root
        self.root.title("Tortoisum AAC Device")
        self.image_path = "icons\images"  # Base path for images
        self.root.geometry("600x300")
        self.menu_items = ["First Step", "Emotions", "About", "Exit"]
       
        
        # Create a PanedWindow
        self.paned_window = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)
        self.paned_window.grid(row=0, column=0, padx=5, pady=5) 
     
        
      
       
       
     
       

        # Create a frame for the textbox
        self.textbox_frame = tk.Frame(self.paned_window)
        self.paned_window.add(self.textbox_frame, width=300, height=100)
          # Create a textbox for constructing sentences
        self.textbox = tk.Text(self.textbox_frame, height=2, width=50)
        self.textbox.grid(row=0, column=100, columnspan=3, padx=5, pady=5)
      
        # Create a panels for the buttons
        self.panel_container = tk.Frame(self.paned_window)
        # Create the different panels (frames)
        self.buttons_frame = tk.Frame(self.paned_window)
        self.paned_window.add(self.buttons_frame, width=200, height=100)
        self.buttons_frame.grid(row=10, column=10, sticky="nsew")
        self.buttons_frame2 = tk.Frame(self.paned_window)
        self.paned_window.add(self.buttons_frame2, width=200, height=100)
        self.buttons_frame2.grid(row=10, column=10, sticky="nsew")
        self.buttons_frame3 = tk.Frame(self.paned_window)
        self.paned_window.add(self.buttons_frame3, width=200, height=100)
        self.buttons_frame3.grid(row=10, column=10, sticky="nsew")
        # Create a container frame for the panels
       
        self.paned_window.add(self.panel_container)
       
        
        self.create_buttons_main()
        self.create_buttons_set1()
        self.create_buttons_set2()
    
      
      
         # Create the buttons for each panel
        self.read_textbox_button()
        self.clear_textbox_button()
        
        
        # Create a frame for the menu buttons
        self.menu_frame = tk.Frame(self.paned_window)
        self.create_menu()  # Create the menu buttons
        self.paned_window.add(self.menu_frame, width=200)
        self.menu_frame.grid(row=0, column=0, sticky="nsew")

    def create_menu(self):
     
     for idx, item in enumerate(self.menu_items):
        btn = tk.Button(self.menu_frame, text=item, width=15, height=2, anchor="w",
                        command=lambda i=idx: self.show_panel(i))
        btn.grid(row=idx, column=0, sticky="w", padx=5, pady=2)
    
    def append_text(self, text):
         self.textbox.insert(tk.END, text + " ")
        

    def handle_read_button_click(self):
        # Read the text from the textbox
        text = self.textbox.get(1.0, tk.END).strip()
        if text:
            text_to_speech(text)
        else:
            print("Textbox is empty. Please enter some text.")
        
        # Optionally, you can play the audio file directly using an external player
        # Uncomment the line below if you want to use an external player like mpg321
     
       # os.system("mpg321 speech.mp3" if os.name != "nt" else "start speech.mp3")

    def handle_button_click(self, text):
        self.append_text(text)
        text_to_speech(text)
 

    def clear_textbox_button(self):
        # Create a button to clear the textbox
        clearbutton = tk.Button(self.panel_container, text="Clear", command=lambda: self.handle_clear_button_click(), height=2, width=10)
        clearbutton.grid(row=5, column=0, padx=5, pady=5)

    def handle_clear_button_click(self):
       #clear the textbox
        self.textbox.delete(1.0, tk.END)

    #create a button to read from the textbox
    def read_textbox_button(self):
        speaker_img_path = os.path.join(self.image_path, "speaker.png")
        try:
            img = Image.open(speaker_img_path).resize((75, 75), Image.LANCZOS)
            img = ImageTk.PhotoImage(img)
        except Exception as e:
            print(f"Error loading image {speaker_img_path}: {e}")
        read_button = tk.Button(self.panel_container, text="Read", command=lambda: self.handle_read_button_click(), height=2, width=10)
        read_button.grid(row=5, column=500, padx=5, pady=5)
    
  

   
    def create_buttons_main(self):
        for row_idx, row in enumerate(buttons_home_set_main):
            for col_idx, (phrase, image_file) in enumerate(row):
                img_path = os.path.join(self.image_path, image_file)
                try:
                    img = Image.open(img_path).resize((75, 75), Image.LANCZOS)
                    img = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f"Error loading image {img_path}: {e}") 
                    continue
                button = tk.Button(self.root, text=phrase, image=img, compound="top",
                                   command=lambda text=phrase: self.handle_button_click(text) , height=100, width=100)
                button.image = img  # Keep a reference to avoid garbage collection
                button.grid(row=row_idx, column=col_idx, padx=5, pady=5,in_=self.buttons_frame)
 

             

    
    def create_buttons_set1(self):
        for row_idx, row in enumerate(buttons_home_set1):
            for col_idx, (phrase, image_file) in enumerate(row):
                img_path = os.path.join(self.image_path, image_file)
                try:
                    img = Image.open(img_path).resize((75, 75), Image.LANCZOS)
                    img = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f"Error loading image {img_path}: {e}")
                    continue
                button1 = tk.Button(self.root, text=phrase, image=img, compound="top",
                                   command=lambda text=phrase: self.handle_button_click(text) , height=100, width=100)
                button1.image = img  # Keep a reference to avoid garbage collection
                button1.grid(row=row_idx, column=col_idx, padx=5, pady=5, in_=self.buttons_frame2)
        
    def create_buttons_set2(self):
        for row_idx, row in enumerate(buttons_emotion_set2):
            for col_idx, (phrase, image_file) in enumerate(row):
                img_path = os.path.join(self.image_path, image_file)
                try:
                    img = Image.open(img_path).resize((75, 75), Image.LANCZOS)
                    img = ImageTk.PhotoImage(img)
                except Exception as e:
                    print(f"Error loading image {img_path}: {e}")
                    continue
                button2 = tk.Button(self.root, text=phrase, image=img, compound="top",
                                   command=lambda text=phrase: self.handle_button_click(text) , height=100, width=100)
                button2.image = img  # Keep a reference to avoid garbage collection
                button2.grid(row=row_idx+1, column=col_idx+1, padx=5, pady=5, in_=self.buttons_frame3)
        
    def show_panel(self, idx):
        
        self.buttons_frame.grid_remove()
        self.buttons_frame2.grid_remove()
        self.buttons_frame3.grid_remove()

        if idx == 0:  # Home
            self.create_buttons_main()
            self.buttons_frame.grid(row=10, column=10, sticky="nsew")
            self.buttons_frame.tkraise()
            self.buttons_frame.update_idletasks()

            self.buttons_frame.tkraise()
            self.buttons_frame.update_idletasks()
            self.buttons_frame.grid(row=20, column=10, sticky="nsew")

          
            print(f"Home panel raised")
        elif idx == 1:  # Emotions
            self.buttons_frame3.tkraise()
            self.buttons_frame3.update_idletasks()
            self.buttons_frame3.grid(row=20, column=10, sticky="nsew")
        
        elif idx == 2:  # About
            self.buttons_frame3.tkraise()
            self.buttons_frame3.update_idletasks()
            self.buttons_frame3.grid(row=10, column=10, sticky="nsew")
        elif idx == 3:  # Exit
            self.root.quit()

if __name__ == "__main__":
     try:
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
            os.remove("speech.mp3")
            print("speech.mp3 deleted.")
     except Exception as e:
            print(f"Could not delete speech.mp3: {e}")
     while True:
            root = tk.Tk()
            app = AACDevice(root)
            root.mainloop()
            break