import tkinter as tk
from tkinter import *
import ttkbootstrap as tb # to install do: pip install ttkbootstrap
from ttkbootstrap.scrolled import ScrolledText

import time
import os
import sys

# Try other themes: superhero darky cyborg vapor lumen minty morph

root = tb.Window(themename="cyborg")
root.title("Simple Virtual Assistant")
root.geometry("690x635")


def loading(chat_window, delay=.25):
    text="..."
    for i in range(3):
        for item in range(len(text)):
            chat_window.insert(tk.END, text[item] + " ")
            chat_window.update()
            time.sleep(delay)
        chat_window.insert(tk.END, '\n')
        chat_window.delete("end-2l", "end-1c")
        chat_window.update()
        time.sleep(delay)
 
 
def smooth_transition_gui(chat_window, text, delay=0.046):
    for char in text:
        chat_window.insert(tk.END, char)
        chat_window.update()
        time.sleep(delay)   
    return " "

def send_message(event=None):
    msg = humaninput.get()
    if msg.strip() != "":
        chat_window.insert(tb.END, "\n")
        chat_window.insert(tb.END, "You: " + msg + "\n")
        loading(chat_window)
        humaninput.set("")
        chat_window.insert(tb.END, "\n")
        message = "Agent: I have a super good answer bro!"
        chat_window.insert(tb.END, smooth_transition_gui(chat_window, message), "\n")
        chat_window.insert(tb.END, "\n")
        
def bot_response(chat_window, response):
    chat_window.insert(tk.END, smooth_transition_gui(chat_window, response))
    chat_window.insert(tk.END, "\n")

chat_window = ScrolledText(root, width=60, height=30, wrap=WORD, autohide=True,
bootstyle="info", font=('Verdana', 15))
chat_window.grid(row=0, column=0, columnspan=2, padx=15, pady=15)
humaninput = tb.StringVar()
entry_field = tb.Entry(root, textvariable=humaninput, width= 48, bootstyle="info",
font=('Verdana', 15))
entry_field.grid(row=1, column=0)
entry_field.bind("<Return>", send_message)
send_button = tb.Button(root, text="Send", command=send_message, width=6,
bootstyle="outline")
send_button.grid(row=1, column=1)
topic = 'Juventus Futbol Club'
initial_response = "Agent: Hi, I am your virtual assistant, ask me anything about Juventus FC (2021 Roster)" 
root.after(500, bot_response(chat_window, initial_response))
root.mainloop()
