# (your imports remain same)
import tkinter as tk
from tkinter import messagebox, ttk
from file_system import FileSystem
from recovery import Recovery
from optimizer import Optimizer
import time

# ---------------- SYSTEM INIT ----------------
fs = FileSystem()

fs.bitmap = [0] * 10
fs.files = {}

# ---------------- THEME ----------------
BG = "#0f172a"
CARD = "#1e293b"
TEXT = "#e2e8f0"
BLUE = "#3b82f6"
HOVER = "#2563eb"
GREY = "#334155"

# ---------------- NEW FEATURE VARIABLES ----------------
selected_file = None

# ---------------- PLACEHOLDER ENTRY ----------------
class PlaceholderEntry(tk.Entry):
    def __init__(self, master, placeholder, is_password=False):
        super().__init__(master, bg="white")

        self.placeholder = placeholder
        self.is_password = is_password

        self.insert(0, placeholder)
        self.config(fg="grey")

        self.bind("<FocusIn>", self.clear)
        self.bind("<FocusOut>", self.add)

    def clear(self, e):
        if self.get() == self.placeholder:
            self.delete(0, tk.END)
            self.config(fg="black")
            if self.is_password:
                self.config(show="*")

    def add(self, e):
        if not self.get():
            self.config(show="")
            self.insert(0, self.placeholder)
            self.config(fg="grey")

# ---------------- MODERN BUTTON ----------------
class ModernButton(tk.Canvas):
    def __init__(self, parent, text, command):
        super().__init__(parent, width=170, height=40,
                         bg=CARD, highlightthickness=0)

        self.command = command

        self.rect = self.create_rectangle(5, 5, 165, 35,
                                          fill=BLUE, outline=BLUE)
        self.text = self.create_text(85, 20, text=text,
                                    fill="white",
                                    font=("Segoe UI", 10, "bold"))

        self.bind("<Button-1>", lambda e: self.command())
        self.bind("<Enter>", lambda e: self.itemconfig(self.rect, fill=HOVER))
        self.bind("<Leave>", lambda e: self.itemconfig(self.rect, fill=BLUE))

# ---------------- DISK VIEW ----------------
def update_disk_view():
    for widget in disk_frame.winfo_children():
        widget.destroy()

    for i, block in enumerate(fs.bitmap):
        color = BLUE if block == 1 else GREY
        tk.Label(disk_frame, text=str(i),
                 bg=color, fg="white",
                 width=4, height=2).grid(row=0, column=i, padx=3)

    update_stats()

# ---------------- FILE LIST ----------------
def update_file_list():
    file_list.delete(0, tk.END)
    for name, blocks in fs.get_files().items():
        file_list.insert(tk.END, f"{name} → {blocks}")

# ---------------- SELECT FILE ----------------
def on_select(event):
    global selected_file
    try:
        index = file_list.curselection()[0]
        selected_file = list(fs.get_files().keys())[index]
        status.set(f"Selected: {selected_file}")
    except:
        pass

# ---------------- STATS ----------------
def update_stats():
    total = len(fs.bitmap)
    used = sum(fs.bitmap)
    percent = int((used / total) * 100)

    stats_label.config(text=f"Disk Usage: {percent}%")
    progress["value"] = percent

# ---------------- CREATE FILE ----------------
def create_file():
    name = entry_name.get()
    size = entry_size.get()

    if name == "Enter file name..." or size == "Enter file size...":
        messagebox.showerror("Error", "Enter valid input")
        return

    if sum(fs.bitmap) == len(fs.bitmap):
        messagebox.showerror("Error", "Disk is full")
        return

    try:
        size = int(size)
    except:
        messagebox.showerror("Error", "Size must be number")
        return

    result = fs.create_file(name, size)
    status.set(result)

    update_disk_view()
    update_file_list()

# ---------------- DELETE FILE ----------------
def delete_file():
    global selected_file

    name = selected_file if selected_file else entry_name.get()

    result = fs.delete_file(name)
    status.set(result)

    update_disk_view()
    update_file_list()

# ---------------- WRITE FILE ----------------
def write_file():
    if not selected_file:
        messagebox.showerror("Error", "Select file first")
        return

    content = content_entry.get()
    result = fs.write_file(selected_file, content)
    status.set(result)

# ---------------- READ FILE ----------------
def read_file():
    if not selected_file:
        messagebox.showerror("Error", "Select file first")
        return

    data = fs.read_file(selected_file)
    status.set(f"Content: {data}")

# ---------------- ACCESS TIME ----------------
def show_access_time():
    opt = Optimizer(fs.bitmap)
    time_val = opt.access_time()
    status.set(f"Access Time: {time_val} ms")

# ---------------- CRASH ----------------
def crash_system():
    status.set(fs.crash())
    update_file_list()

# ---------------- RECOVERY ----------------
def recover_files():
    rec = Recovery(fs.bitmap)
    recovered = rec.recover_files()

    fs.files = {}
    for i, blocks in enumerate(recovered):
        fs.files[f"recovered_{i}"] = blocks

    status.set(f"Recovered {len(recovered)} files")
    update_file_list()

# ---------------- DEFRAGMENT ----------------
def defragment_disk():
    opt = Optimizer(fs.bitmap)
    new_bitmap = opt.defragment()

    for i in range(len(new_bitmap)):
        fs.bitmap[i] = new_bitmap[i]
        update_disk_view()
        root.update()
        time.sleep(0.1)

    status.set("Disk optimized")

# ---------------- LOGIN ----------------
def login():
    if user.get() == "admin" and pwd.get() == "1234":
        login_frame.destroy()
        build_ui()
    else:
        messagebox.showerror("Error", "Invalid credentials")

# ---------------- MAIN UI ----------------
def build_ui():
    global entry_name, entry_size, content_entry, file_list, disk_frame, stats_label, status, progress

    root.configure(bg=BG)

    tk.Label(root, text="💾 File System Dashboard",
             bg=BG, fg=TEXT,
             font=("Segoe UI", 18, "bold")).pack(pady=10)

    main = tk.Frame(root, bg=BG)
    main.pack(fill="both", expand=True)

    # LEFT PANEL
    left = tk.Frame(main, bg=CARD, padx=10, pady=10)
    left.pack(side="left", fill="y", padx=10)

    entry_name = PlaceholderEntry(left, "Enter file name...")
    entry_name.pack(pady=8)

    entry_size = PlaceholderEntry(left, "Enter file size...")
    entry_size.pack(pady=8)

    content_entry = PlaceholderEntry(left, "Enter file content...")
    content_entry.pack(pady=8)

    ModernButton(left, "Create File", create_file).pack(pady=5)
    ModernButton(left, "Delete File", delete_file).pack(pady=5)
    ModernButton(left, "Write File", write_file).pack(pady=5)
    ModernButton(left, "Read File", read_file).pack(pady=5)
    ModernButton(left, "Access Time", show_access_time).pack(pady=5)
    ModernButton(left, "Crash System", crash_system).pack(pady=5)
    ModernButton(left, "Recover Files", recover_files).pack(pady=5)
    ModernButton(left, "Defragment", defragment_disk).pack(pady=5)

    # CENTER PANEL
    center = tk.Frame(main, bg=CARD)
    center.pack(side="left", expand=True, fill="both")

    disk_frame = tk.Frame(center, bg=CARD)
    disk_frame.pack(pady=20)

    progress = ttk.Progressbar(center, length=300)
    progress.pack()

    stats_label = tk.Label(center, bg=CARD, fg="white")
    stats_label.pack()

    # RIGHT PANEL
    right = tk.Frame(main, bg=CARD)
    right.pack(side="right", fill="y", padx=10)

    file_list = tk.Listbox(right, width=30)
    file_list.pack()

    file_list.bind("<<ListboxSelect>>", on_select)

    # STATUS BAR
    status = tk.StringVar()
    tk.Label(root, textvariable=status,
             bg="#020617", fg="white").pack(fill="x")

    update_disk_view()
    update_file_list()

# ---------------- LOGIN UI ----------------
root = tk.Tk()
root.geometry("900x600")
root.configure(bg=BG)

login_frame = tk.Frame(root, bg=BG)
login_frame.pack(expand=True)

user = PlaceholderEntry(login_frame, "Username")
user.pack(pady=5)

pwd = PlaceholderEntry(login_frame, "Password", is_password=True)
pwd.pack(pady=5)

tk.Button(login_frame, text="Login",
          bg=BLUE, fg="white",
          command=login).pack(pady=10)

# -------- ADD THIS --------
def on_close():
    fs.reset_bitmap()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()