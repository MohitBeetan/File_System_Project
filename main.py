import tkinter as tk
from tkinter import messagebox
from file_system import FileSystem
from recovery import Recovery
from optimizer import Optimizer

fs = FileSystem()

# -------- FUNCTIONS -------- #

def update_disk_view():
    for widget in disk_frame.winfo_children():
        widget.destroy()

    for i, block in enumerate(fs.bitmap):
        color = "green" if block == 1 else "white"
        lbl = tk.Label(disk_frame, text=str(i), bg=color, width=4, height=2, relief="solid")
        lbl.grid(row=0, column=i, padx=2)

def update_file_list():
    file_list.delete(0, tk.END)
    for name, blocks in fs.get_files().items():
        file_list.insert(tk.END, f"{name} → {blocks}")

def create_file():
    name = entry_name.get()
    size = entry_size.get()

    if not name or not size:
        messagebox.showerror("Error", "Enter all fields")
        return

    try:
        size = int(size)
    except:
        messagebox.showerror("Error", "Size must be number")
        return

    result = fs.create_file(name, size)
    output.set(result)

    update_disk_view()
    update_file_list()

def delete_file():
    name = entry_name.get()

    if not name:
        messagebox.showerror("Error", "Enter file name")
        return

    result = fs.delete_file(name)
    output.set(result)

    update_disk_view()
    update_file_list()

def show_bitmap():
    output.set(f"Bitmap: {fs.show_bitmap()}")

def crash_system():
    result = fs.crash()
    output.set(result)
    update_file_list()

def recover_files():
    rec = Recovery(fs.bitmap)
    result = rec.recover_files()
    output.set(f"Recovered: {result}")

def defragment_disk():
    opt = Optimizer(fs.bitmap)
    fs.bitmap = opt.defragment()
    output.set("Disk Defragmented")

    update_disk_view()

# -------- GUI -------- #

root = tk.Tk()
root.title("File System Recovery Tool")
root.geometry("700x500")
root.configure(bg="#1e1e1e")

# Title
tk.Label(root, text="File System Simulator", font=("Arial", 18, "bold"),
         fg="white", bg="#1e1e1e").pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#1e1e1e")
input_frame.pack()

tk.Label(input_frame, text="File Name", fg="white", bg="#1e1e1e").grid(row=0, column=0)
entry_name = tk.Entry(input_frame)
entry_name.grid(row=0, column=1, padx=10)

tk.Label(input_frame, text="Size", fg="white", bg="#1e1e1e").grid(row=1, column=0)
entry_size = tk.Entry(input_frame)
entry_size.grid(row=1, column=1, padx=10)

# Buttons
btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Create", command=create_file, bg="#4CAF50", width=12).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_file, bg="#f44336", width=12).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Crash", command=crash_system, width=12).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Recover", command=recover_files, width=12).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Defragment", command=defragment_disk, width=12).grid(row=0, column=4, padx=5)

# Disk View
tk.Label(root, text="Disk Blocks", fg="white", bg="#1e1e1e").pack()
disk_frame = tk.Frame(root, bg="#1e1e1e")
disk_frame.pack(pady=10)

# File List
tk.Label(root, text="Files", fg="white", bg="#1e1e1e").pack()
file_list = tk.Listbox(root, width=50)
file_list.pack(pady=5)

# Output
output = tk.StringVar()
tk.Label(root, textvariable=output, fg="yellow", bg="#1e1e1e").pack(pady=10)

# Initialize
update_disk_view()
update_file_list()

root.mainloop()