import tkinter as tk
import pyttsx3
import threading

# Initialize TTS engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

# Flag to keep track of speech thread
speaking_thread = None

# Function to speak the input text
def speak_text():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        # Set voice
        selected_voice = voice_var.get()
        if selected_voice == "Male":
            engine.setProperty('voice', voices[0].id)
        else:
            engine.setProperty('voice', voices[1].id)
        
        # Set speed
        engine.setProperty('rate', speed_scale.get())

        engine.say(text)
        engine.runAndWait()

# Threaded wrapper for speaking to avoid freezing the GUI
def start_speaking():
    global speaking_thread
    speaking_thread = threading.Thread(target=speak_text)
    speaking_thread.start()

# Function to stop speaking
def stop_speaking():
    engine.stop()

# # Set up the GUI window
# root = tk.Tk()
# root.title("Text-to-Speech Reader")
# root.geometry("420x420")
# root.configure(bg="#f0f0f0")

# # Label
# label = tk.Label(root, text="Enter text below:", font=("Arial", 12), bg="#f0f0f0")
# label.pack(pady=10)

# # Text input box
# text_input = tk.Text(root, height=10, width=45, font=("Arial", 11))
# text_input.pack(pady=5)

# # Voice selection
# voice_var = tk.StringVar(value="Male")
# voice_frame = tk.Frame(root, bg="#f0f0f0")
# tk.Label(voice_frame, text="Voice:", font=("Arial", 11), bg="#f0f0f0").pack(side=tk.LEFT)
# tk.Radiobutton(voice_frame, text="Male", variable=voice_var, value="Male", bg="#f0f0f0").pack(side=tk.LEFT)
# tk.Radiobutton(voice_frame, text="Female", variable=voice_var, value="Female", bg="#f0f0f0").pack(side=tk.LEFT)
# voice_frame.pack(pady=5)

# # Speed control
# tk.Label(root, text="Speed (Words per Minute):", font=("Arial", 11), bg="#f0f0f0").pack()
# speed_scale = tk.Scale(root, from_=100, to=300, orient=tk.HORIZONTAL, length=200)
# speed_scale.set(200)
# speed_scale.pack(pady=5)

# # Buttons Frame
# buttons_frame = tk.Frame(root, bg="#f0f0f0")
# buttons_frame.pack(pady=10)

# # Speak button
# speak_button = tk.Button(buttons_frame, text="Speak", command=start_speaking, font=("Arial", 12), bg="#4caf50", fg="white", width=10)
# speak_button.pack(side=tk.LEFT, padx=10)

# # Stop button
# stop_button = tk.Button(buttons_frame, text="Stop", command=stop_speaking, font=("Arial", 12), bg="#f44336", fg="white", width=10)
# stop_button.pack(side=tk.LEFT, padx=10)

# # Run GUI
# root.mainloop()

