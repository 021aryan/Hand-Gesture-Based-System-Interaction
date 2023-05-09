import tkinter as tk
from tkinter import *
from PIL import ImageTk
import threading

imagebox = None  # define imagebox globally

def show_image(imagefile):
    global imagebox  # use the global imagebox
    image = ImageTk.PhotoImage(file=imagefile)
    imagebox.config(image=image)
    imagebox.image = image  # save a reference of the image to avoid garbage collection

def run_gui():
    global imagebox  # use the global imagebox
    
    root = tk.Tk()

    frame = tk.Frame(root)
    frame.pack()

    info = tk.Button(frame, text="Switch Tabs", command=lambda: show_image("C:\Akash\switch.jpg"))
    info.pack(side=TOP)

    other = tk.Button(frame, text="Lock screen", command=lambda: show_image("C:\Akash\WinL.png"))
    other.pack(side=TOP)

    other1= tk.Button(frame, text="  Mouse Navigation  ", command=lambda: show_image("C:\Akash\Mcon.png"))
    other1.pack(side=TOP)

    other2= tk.Button(frame, text="Right Click", command=lambda: show_image("C:\Akash\Rcli.png"))
    other2.pack(side=TOP)

    other3= tk.Button(frame, text="Left Click", command=lambda: show_image("C:\Akash\Lcli.png"))
    other3.pack(side=TOP)

    imagebox = tk.Label(root)
    imagebox.pack()
    root.mainloop()

def run_gui_thread():
    gui_thread = threading.Thread(target=run_gui)
    gui_thread.start()
    
