import tkinter as tk #1
from tkinter import messagebox
import time
import random

def fake_crash():
    root = tk.Tk()
    root.title("Microsoft Visual Studio")
    root.geometry("600x300")
    root.configure(bg="white")

    label1 = tk.Label(root, text="Microsoft Visual Studio dejó de funcionar",
                      font=("Segoe UI", 14), bg="white")
    label1.pack(pady=20)

    error_code = f"Error Code: 0x{random.randint(100000,999999):X}"

    label2 = tk.Label(root,
                      text=f"Se produjo un error inesperado.\n{error_code}\n\nRecopilando información...",
                      font=("Segoe UI", 11),
                      bg="white")
    label2.pack(pady=10)

    progress = tk.Label(root, text="0%", font=("Segoe UI", 10), bg="white")
    progress.pack()

    root.update()

    # Simulación de progreso
    for i in range(101):
        progress.config(text=f"{i}%")
        root.update()
        time.sleep(0.03)

    time.sleep(1)

    messagebox.showinfo("Visual Studio", "El programa se cerrará ahora.")
    root.destroy()

fake_crash()
