# File_System_Project
A File System Recovery and Optimization Tool that simulates disk management, recovers lost data, and improves file storage efficiency.
# 📂 File System Recovery and Optimization Tool

## 🧠 Project Overview

This project is a **File System Simulator** developed using Python. It demonstrates core Operating System concepts such as file allocation, free space management, crash recovery, and disk optimization.

The system simulates how an actual operating system manages files on a disk using a **bitmap-based allocation method** and provides a graphical interface for interaction.

---

## 🎯 Objectives

* To simulate file storage using disk blocks
* To implement **free space management using bitmap**
* To demonstrate **file creation and deletion**
* To simulate **system crash and recovery**
* To implement **disk optimization (defragmentation)**
* To provide a **user-friendly GUI interface**

---

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter (GUI Library)**
* JSON (for persistent storage)

---

## ⚙️ Features

### ✅ File Management

* Create files with a given name and size
* Delete existing files
* Prevent duplicate file names

### 💿 Disk Simulation

* Disk is represented using blocks
* Each block can be either:

  * 🟩 Occupied
  * ⬜ Free

### 📊 Bitmap Free Space Management

* Uses a bitmap where:

  * `1` = occupied block
  * `0` = free block

### 💥 Crash Simulation

* Simulates system crash by deleting file metadata
* Disk data remains intact

### 🔄 Recovery System

* Recovers files based on occupied blocks after crash

### ⚡ Disk Optimization

* Defragmentation combines scattered blocks
* Improves file access efficiency

### 🖥️ GUI Interface

* Built using Tkinter
* Easy-to-use buttons and visual disk blocks
* Displays file allocation and system output

---

## 📁 Project Structure

```
file_system_project/
│
├── main.py              # GUI and main program
├── file_system.py       # File system logic
├── recovery.py          # Recovery mechanism
├── optimizer.py         # Defragmentation logic
├── bitmap.json          # Stores block usage
└── disk.txt             # Simulated disk
```

---

## ▶️ How to Run

1. Open project folder in VS Code
2. Open terminal
3. Run the command:

```
python main.py
```

---

## 🧪 How to Use

1. Enter file name and size
2. Click **Create** to store file
3. Click **Delete** to remove file
4. Click **Crash** to simulate system failure
5. Click **Recover** to restore lost files
6. Click **Defragment** to optimize disk

---

## 🧠 Key Concepts Covered

* File Allocation Methods
* Bitmap Free Space Management
* Disk Fragmentation
* Defragmentation
* Crash Recovery Mechanism

---

## 📌 Example

```
file1 → [0,1,2]
file2 → [3,4]
```

This means:

* file1 occupies blocks 0,1,2
* file2 occupies blocks 3,4

---

## 🚀 Future Enhancements

* Directory (folder) structure
* File read/write functionality
* Disk usage statistics
* Animation for defragmentation
* Advanced UI design

---

## 👨‍💻 Authors

Mohit Beetan, Prasanjit Majumder, Soumya Prerit

---

## 📖 Conclusion

This project provides a simplified but effective understanding of how operating systems manage files, recover from crashes, and optimize storage. It bridges theoretical OS concepts with practical implementation.

---
