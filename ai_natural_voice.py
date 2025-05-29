import tkinter as tk
from gtts import gTTS
import os
import tempfile
import threading
import platform
import subprocess

# Globals
current_process = None

# Function to play the MP3 file
def play_audio(file_path):
    global current_process
    if platform.system() == "Windows":
        current_process = subprocess.Popen(["start", file_path], shell=True)
    elif platform.system() == "Darwin":  # macOS
        current_process = subprocess.Popen(["afplay", file_path])
    else:  # Linux
        current_process = subprocess.Popen(["xdg-open", file_path])

# Function to speak the text using gTTS
def speak_text():
    text = text_input.get("1.0", tk.END).strip()
    if text:
        try:
            tts = gTTS(text=text, lang='en', slow=speed_var.get() == "Slow")
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
            tts.save(temp_file.name)
            play_audio(temp_file.name)
        except Exception as e:
            print("Error:", e)

# Thread wrapper
def start_speaking():
    threading.Thread(target=speak_text, daemon=True).start()

# Stop playback
def stop_speaking():
    global current_process
    if current_process:
        current_process.terminate()
        current_process = None

# Function to clear the text input
def clear_text():
    text_input.delete("1.0", tk.END)

# Paste clipboard text into the input box
def paste_text():
    try:
        clipboard_content = root.clipboard_get()
        text_input.insert(tk.END, clipboard_content)
    except tk.TclError:
        print("Nothing in clipboard.")
# GUI setup
root = tk.Tk()
root.title("LBYP Text-to-Speech")
root.geometry("420x450")  # Increased height for new button
root.configure(bg="#f0f0f0")

# Input label
tk.Label(root, text="Enter text below:", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

# Text box
text_input = tk.Text(root, height=10, width=45, font=("Arial", 11))
text_input.pack(pady=5)

# Speed selection
speed_var = tk.StringVar(value="Normal")
tk.Label(root, text="Speed:", font=("Arial", 11), bg="#f0f0f0").pack()
speed_frame = tk.Frame(root, bg="#f0f0f0")
tk.Radiobutton(speed_frame, text="Normal", variable=speed_var, value="Normal", bg="#f0f0f0").pack(side=tk.LEFT)
tk.Radiobutton(speed_frame, text="Slow", variable=speed_var, value="Slow", bg="#f0f0f0").pack(side=tk.LEFT)
speed_frame.pack(pady=5)

# Button frame
buttons_frame = tk.Frame(root, bg="#f0f0f0")
buttons_frame.pack(pady=10)

tk.Button(buttons_frame, text="Speak", command=start_speaking, font=("Arial", 12), bg="#4caf50", fg="white", width=10).pack(side=tk.LEFT, padx=5)
tk.Button(buttons_frame, text="Stop", command=stop_speaking, font=("Arial", 12), bg="#f44336", fg="white", width=10).pack(side=tk.LEFT, padx=5)

# Clear Button (Newly Added)
tk.Button(root, text="Clear", command=clear_text, font=("Arial", 12), bg="#2196F3", fg="white", width=10).pack(pady=10)

# Paste Button
tk.Button(buttons_frame, text="Paste", command=paste_text, font=("Arial", 12), bg="#9c27b0", fg="white", width=10).pack(side=tk.LEFT, padx=5)
root.mainloop()
