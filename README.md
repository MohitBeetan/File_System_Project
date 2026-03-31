# File_System_Project
A File System Recovery and Optimization Tool that simulates disk management, recovers lost data, and improves file storage efficiency.
# 📂 File_System_Project

### File System Recovery and Optimization Tool

A Python-based File System Simulator that demonstrates core Operating System concepts such as file allocation, free space management, crash recovery, and disk optimization using a realistic and modular approach.

---

# 🧠 Project Overview

This project simulates how an operating system manages files on a disk using a **bitmap-based allocation technique**. It includes advanced features like **crash simulation, recovery mechanisms, and disk optimization (defragmentation)**.

The system is designed with a modular structure and persistent storage using JSON files, making it both educational and practical.

---

# 🎯 Objectives

* Simulate file storage using disk blocks
* Implement free space management using bitmap
* Demonstrate file creation and deletion
* Simulate system crash and recovery
* Implement disk optimization (defragmentation)
* Provide a user-friendly GUI interface

---

# 🛠️ Technologies Used

* Python 3
* Tkinter (GUI Library)
* JSON (Persistent Storage)

---

# ⚙️ Features

## ✅ File Management

* Create files with a given name and size
* Delete existing files
* Prevent duplicate file names

## 💿 Disk Simulation

* Disk represented using fixed-size blocks
* Each block can be:

  * 🟩 Occupied
  * ⬜ Free

## 📊 Bitmap Free Space Management

* Uses bitmap representation:

  * `1` = occupied
  * `0` = free

## 💥 Crash Simulation

* Simulates system crash by removing file metadata
* Disk data remains intact

## 🔄 Recovery System

* Recovers files using stored disk/block data
* Ensures data consistency after crash

## ⚡ Disk Optimization (Defragmentation)

* Rearranges scattered blocks
* Improves storage efficiency and access speed

## 🖥️ GUI Interface

* Built using Tkinter
* Interactive buttons and disk visualization
* Displays real-time system operations

## 💾 Persistent Storage

* `bitmap.json` → Tracks block usage
* `disk.txt` → Simulated disk storage
* `storage.json` → Stores file metadata (NEW)

---

# 📁 Project Structure

```
File_System_Project/
│
├── main.py              # GUI and main controller
├── file_system.py       # Core file system logic
├── recovery.py          # Crash recovery logic
├── optimizer.py         # Disk optimization logic
├── bitmap.json          # Block allocation map
├── disk.txt             # Simulated disk data
├── storage.json         # File metadata storage
└── README.md            # Project documentation
```

---

# ▶️ How to Run

1. Open project folder in VS Code
2. Open terminal
3. Run:

```
python main.py
```

---

# 🧪 How to Use

1. Enter file name and size
2. Click **Create** → store file
3. Click **Delete** → remove file
4. Click **Crash** → simulate system failure
5. Click **Recover** → restore files
6. Click **Defragment** → optimize disk

---

# 🧠 Key Concepts Covered

* File Allocation Techniques
* Bitmap Free Space Management
* Disk Fragmentation
* Defragmentation
* Crash Recovery Mechanism
* Persistent Storage Handling

---

# 📌 Example

```
file1 → [0,1,2]  
file2 → [3,4]
```

* file1 occupies blocks 0,1,2
* file2 occupies blocks 3,4

---

# 🚀 Future Enhancements

* Directory (folder) structure
* File read/write functionality
* Disk usage statistics
* Animated defragmentation
* Advanced UI/UX improvements

---

# 👨‍💻 Authors

* Mohit Beetan
* Prasanjit Majumder
* Soumya Prerit

---

# 📖 Conclusion

This project provides a practical understanding of how operating systems manage storage, recover from failures, and optimize disk usage. It effectively bridges theoretical OS concepts with real-world implementation using Python.

---
