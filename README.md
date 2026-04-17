#  Hospital Management System

## 📌 Project Overview

The **Hospital Management System** is a desktop-based application designed to streamline hospital operations by managing patient records efficiently. This system is developed using **Python for the graphical user interface (GUI)** and **C++ for backend processing**, ensuring both usability and performance.

It enables healthcare staff to handle patient data, maintain records, and perform basic administrative operations in a structured and efficient manner.

---

## 🎯 Objectives

* To digitize hospital record management
* To reduce manual paperwork
* To improve data accuracy and accessibility
* To provide a simple and user-friendly interface

---

## ⚙️ Technologies Used

* **Python (Tkinter)** – GUI development
* **C++** – Core logic and backend processing
* **File Handling** – Data storage and retrieval

---

## 🚀 Key Features

* ➕ Add new patient records
* 📋 View all patient details
* 🔍 Search patient by ID or name
* ❌ Delete patient records
* 💾 Save and load patient data from files
* 🖥️ Simple and interactive GUI

---

## ▶️ How to Run the Project

### Step 1: Compile Backend (C++)

```bash
g++ backend.cpp -o backend.exe
```

### Step 2: Run Python GUI

```bash
python gui.py
```

---

## 📂 Project Structure

```
hospital_management_system/
│
├── src/
│   ├── gui.py          # Python GUI
│   └── backend.cpp     # C++ Backend
│
├── build/
│   └── backend.exe     # Compiled C++ file
│
├── data/
│   └── patients.txt    # Stored patient records
│
├── assets/
│   └── logo.png        # Project assets
│
├── README.md
└── requirements.txt
```

---

## 📊 System Workflow

1. User interacts with GUI
2. GUI sends request to backend
3. Backend processes data
4. Data stored/retrieved from file
5. Results displayed on GUI

---

## 🔮 Future Enhancements

* 🔐 User authentication system (Admin/Staff login)
* 🗄️ Integration with MySQL or MongoDB database
* ☁️ Cloud-based deployment
* 📊 Advanced analytics and reporting dashboard
* 🌐 Web-based version of the system

---

## 🧪 Testing & Results

The system has been tested for:

* Accurate data entry and retrieval
* Proper file handling operations
* Smooth GUI interaction

Results show that the system performs efficiently for small to medium-scale hospital management tasks.

---

## ✅ Conclusion

This project demonstrates how combining **Python GUI** with **C++ backend** can create a powerful hybrid system. It successfully reduces manual workload and improves operational efficiency in hospital environments.

---

## 👨‍💻 Author

**Keshav Mishra**

---

## 📌 Note

This is a mini project designed for academic purposes, but it has strong potential to be scaled into a real-world healthcare solution with further enhancements.
