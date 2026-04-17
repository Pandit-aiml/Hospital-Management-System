import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os

# Get project root path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct path to exe
EXE_PATH = os.path.join(BASE_DIR, "backend", "hospital.exe")

def add_patient():
    name = entry_name.get().replace(" ", "_")
    age = entry_age.get()
    problem = entry_problem.get().replace(" ", "_")
    weight = entry_weight.get()
    bg = combo_bg.get()
    payment = combo_payment.get()
    doctor = combo_doctor.get().replace(" ", "_")
    
    if not name or not age or not problem or not weight or not bg or not payment or not doctor:
        messagebox.showwarning("Input Error", "Please fill out all fields before adding a patient.")
        return

    subprocess.run([EXE_PATH, "add", name, age, problem, weight, bg, payment, doctor], cwd=BASE_DIR)
    messagebox.showinfo("Success", "Patient added successfully!")
    
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_problem.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    combo_bg.set('')
    combo_payment.set('')
    combo_doctor.set('')
    
    view_patients()

def view_patients():
    result = subprocess.run(
        [EXE_PATH, "view"],
        capture_output=True,
        text=True,
        cwd=BASE_DIR
    )

    # Clear existing data in treeview
    for row in tree.get_children():
        tree.delete(row)

    # Parse backend stdout and insert into Treeview
    lines = result.stdout.strip().split('\n')
    for line in lines:
        if not line:
            continue
        try:
            # Expected format: Name: John_Doe | Age: 30 | Problem: Fever | Weight: 70kg | Blood Group: O+ | Payment: Paid | Doctor: Dr._Smith_(Cardiology)
            parts = line.split(" | ")
            name = parts[0].split(": ")[1].replace("_", " ")
            age = parts[1].split(": ")[1]
            problem = parts[2].split(": ")[1].replace("_", " ")
            weight = parts[3].split(": ")[1].replace("kg", "")
            bg = parts[4].split(": ")[1]
            payment = parts[5].split(": ")[1]
            doctor = parts[6].split(": ")[1].replace("_", " ")
            
            tree.insert("", tk.END, values=(name, age, problem, weight + " kg", bg, payment, doctor))
        except Exception:
            pass # Skip malformed lines instead of crashing the GUI

def delete_patient():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Selection Error", "Please select a patient to delete.")
        return
        
    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this patient record?")
    if confirm:
        item_values = tree.item(selected[0], 'values')
        name = item_values[0].replace(" ", "_")
        
        subprocess.run([EXE_PATH, "delete", name], cwd=BASE_DIR)
        messagebox.showinfo("Success", "Patient record deleted.")
        view_patients()

app = tk.Tk()
app.title("Hospital Management System")
app.geometry("1100x650")
app.configure(bg="#f4f6f9") # Light background

# --- Styles ---
style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=('Arial', 11, 'bold'), background="#decaff", foreground="#2c3e50")
style.configure("Treeview", font=('Arial', 10), rowheight=25)

label_font = ("Arial", 11, "bold")
entry_font = ("Arial", 11)

# Header
header_frame = tk.Frame(app, bg="#2980b9", pady=15)
header_frame.pack(fill=tk.X)
tk.Label(header_frame, text="🏥 Hospital Management System Dashboard", font=("Arial", 20, "bold"), fg="white", bg="#2980b9").pack()

# Main Container
main_frame = tk.Frame(app, bg="#f4f6f9", padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# --- Left Panel: Form ---
left_frame = tk.LabelFrame(main_frame, text=" 📝 Add New Patient ", font=("Arial", 12, "bold"), bg="white", padx=15, pady=15)
left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 20))

def create_labeled_entry(parent, label_text):
    tk.Label(parent, text=label_text, font=label_font, bg="white").pack(anchor=tk.W, pady=(5, 2))
    entry = tk.Entry(parent, font=entry_font, width=32, relief=tk.SOLID)
    entry.pack(anchor=tk.W, pady=(0, 10))
    return entry

entry_name = create_labeled_entry(left_frame, "Patient Name:")
entry_age = create_labeled_entry(left_frame, "Age:")
entry_problem = create_labeled_entry(left_frame, "Medical Problem:")
entry_weight = create_labeled_entry(left_frame, "Weight (kg):")

tk.Label(left_frame, text="Blood Group:", font=label_font, bg="white").pack(anchor=tk.W, pady=(5, 2))
combo_bg = ttk.Combobox(left_frame, values=["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"], state="readonly", font=entry_font, width=30)
combo_bg.pack(anchor=tk.W, pady=(0, 10))

tk.Label(left_frame, text="Payment Status:", font=label_font, bg="white").pack(anchor=tk.W, pady=(5, 2))
combo_payment = ttk.Combobox(left_frame, values=["Paid", "Unpaid"], state="readonly", font=entry_font, width=30)
combo_payment.pack(anchor=tk.W, pady=(0, 10))

tk.Label(left_frame, text="Assign Doctor:", font=label_font, bg="white").pack(anchor=tk.W, pady=(5, 2))
combo_doctor = ttk.Combobox(left_frame, values=[
    "Dr. Smith (Cardiology)", 
    "Dr. House (Neurology)", 
    "Dr. Strange (Surgery)", 
    "Dr. Jones (Pediatrics)", 
    "Dr. Patel (General)"
], state="readonly", font=entry_font, width=30)
combo_doctor.pack(anchor=tk.W, pady=(0, 20))

tk.Button(left_frame, text="➕ Register Patient", font=("Arial", 12, "bold"), bg="#27ae60", fg="white", cursor="hand2", relief=tk.FLAT, command=add_patient).pack(fill=tk.X, pady=5)

# --- Right Panel: Data Table ---
right_frame = tk.LabelFrame(main_frame, text=" 📋 Patient Records ", font=("Arial", 12, "bold"), bg="white", padx=10, pady=10)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Setup Treeview (Data Table)
columns = ("Name", "Age", "Problem", "Weight", "Blood Group", "Payment", "Doctor")
tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=15)

# Define Headings and Column widths
tree.heading("Name", text="Name")
tree.column("Name", width=140, anchor=tk.W)

tree.heading("Age", text="Age")
tree.column("Age", width=50, anchor=tk.CENTER)

tree.heading("Problem", text="Problem")
tree.column("Problem", width=120, anchor=tk.W)

tree.heading("Weight", text="Weight")
tree.column("Weight", width=70, anchor=tk.CENTER)

tree.heading("Blood Group", text="Blood P.")
tree.column("Blood Group", width=80, anchor=tk.CENTER)

tree.heading("Payment", text="Payment")
tree.column("Payment", width=80, anchor=tk.CENTER)

tree.heading("Doctor", text="Doctor")
tree.column("Doctor", width=160, anchor=tk.W)

# Add Scrollbar
scrollbar = ttk.Scrollbar(right_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack(fill=tk.BOTH, expand=True)

# Add Delete Button Frame
bottom_right_frame = tk.Frame(right_frame, bg="white")
bottom_right_frame.pack(fill=tk.X, pady=(10, 0))

tk.Button(bottom_right_frame, text="🗑️ Delete Selected Patient", font=("Arial", 11, "bold"), bg="#e74c3c", fg="white", cursor="hand2", relief=tk.FLAT, command=delete_patient).pack(side=tk.RIGHT, padx=5)

# Initial Load
view_patients()

app.mainloop()