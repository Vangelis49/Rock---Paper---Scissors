#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:43:24 2023

@author: evangelos
"""

import tkinter as tk
import random

# possible choices
choices = ['Rock', 'Paper', 'Scissors']

def random_choice():
    choice = random.choice(choices)
    choice_label.config(text=f'{choice}')

root = tk.Tk()
root.title("Random Rock Paper Scissors")

button = tk.Button(root, 
                   text="Generate",
                   command=random_choice)
button.pack()

choice_label = tk.Label(root, text="")
choice_label.pack()

root.mainloop()
