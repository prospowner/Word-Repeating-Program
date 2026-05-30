import tkinter as tk
import random

WORD = "Afifa"
COLOR = "lime"

root = tk.Tk()
root.attributes("-fullscreen", True)
root.configure(bg="black")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg="black", highlightthickness=0)
canvas.pack()

def show_word():
    canvas.delete("all") 
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    size = random.randint(20, 100)
    canvas.create_text(x, y, text=WORD, fill=COLOR, font=("Arial", size, "bold"))
    root.after(100, show_word)  

def exit_fullscreen(event):
    root.destroy()

root.bind("<Escape>", exit_fullscreen)

show_word()
root.mainloop()
