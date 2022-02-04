import tkinter as tk
import pyttsx3

engine = pyttsx3.init()

def speak():
    engine.say(text_variable.get())
    engine.runAndWait()
    engine.stop()

window = tk.Tk()

text_variable = tk.StringVar()

label1 = tk.Label(window, text="Text to Speech", font=20)
label1.pack(pady=20, padx=10, ipady=10)

label2 = tk.Label(window, text="Text", font=30)
label2.pack(side=tk.LEFT, ipadx=20, ipady=20)

entry = tk.Entry(window, textvariable=text_variable, font=30, width=25, bd=5)
entry.pack(side=tk.LEFT, padx=10)

button = tk.Button(window, text="Speak", font=20, bg="black", fg="white", command=speak)
button.pack(side=tk.LEFT, padx=10)

window.title("Text to Speech")
window.geometry("500x200")
window.resizable(False, False)
window.mainloop()
