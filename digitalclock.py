import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

root = tk.Tk()
root.title("Digital Clock")
root.configure(bg='gray20')  # Set window background

clock_label = tk.Label(
    root,
    font=('Arial', 48, 'bold'),
    bg='black',
    fg='cyan',
    bd=10,
    relief='ridge',
    padx=30,
    pady=30
)
clock_label.pack(padx=40, pady=40)

update_clock()
root.mainloop()