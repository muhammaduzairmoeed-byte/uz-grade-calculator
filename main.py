# yourname=input("Enter your name: ")
# number=int(input("Enter marks: "))
# totalnumber=int(input("Enter total numbers: "))
# percentage=(float(number/totalnumber*100))
# print("Your name is:", yourname,"\nyour marks are:", number,"\nTotal marks are:", totalnumber,"\nYour percentage is:", percentage)
# if percentage >=90:
#     print("Status: Pass")
#     print("Grade:  A+")
# elif percentage >=80:
#     print("Status: Pass")
#     print("Grade: A")
# elif percentage >=70:
# #     print("Status: Pass")
# #     print("Grade: B")
# # elif percentage >=60:
# #     print("Status: Pass")
# #     print("Grade: C")
# # elif percentage >=50:
# #     print("Status: Pass")
# #     print("Grade: D")
# # else:
# #     print("Status: Fail")
# #     print("Grade: F")

import tkinter as tk
from tkinter import messagebox

# Function to calculate percentage and grade
def calculate_grade():
    try:
        # Get data from entry fields
        name = name_entry.get()
        marks = float(marks_entry.get())
        total = float(total_entry.get())
        
        # Validation to prevent division by zero
        if total <= 0:
            messagebox.showerror("Error", "Total marks must be greater than 0.")
            return
            
        # Calculation
        percentage = (marks / total) * 100
        
        # Determine Grade and Status
        if percentage >= 90:
            status, grade = "Pass", "A+"
        elif percentage >= 80:
            status, grade = "Pass", "A"
        elif percentage >= 70:
            status, grade = "Pass", "B"
        elif percentage >= 60:
            status, grade = "Pass", "C"
        elif percentage >= 50:
            status, grade = "Pass", "D"
        else:
            status, grade = "Fail", "F"
            
        # Update the result labels
        result_name.config(text=f"Name: {name}")
        result_percentage.config(text=f"Percentage: {percentage:.2f}%")
        result_status.config(text=f"Status: {status}")
        result_grade.config(text=f"Grade: {grade}")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values for marks.")

# --- UI Setup ---
root = tk.Tk()
root.title("Student Grade Calculator")
root.geometry("400x450")
root.config(bg="#f0f4f8")

# Title Banner
title_label = tk.Label(root, text="UZ Grade Calculator", font=("Arial", 18, "bold"), bg="#102a43", fg="white", pady=10)
title_label.pack(fill="x",  pady=(0, 20))

# Form Frame
form_frame = tk.Frame(root, bg="#f0f4f8")
form_frame.pack()

# Inputs
tk.Label(form_frame, text="Enter Name:", font=("Arial", 11), bg="#f0f4f8").grid(row=0, column=0, sticky="w", pady=5)
name_entry = tk.Entry(form_frame, font=("Arial", 11), width=20)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Obtained Marks:", font=("Arial", 11), bg="#f0f4f8").grid(row=1, column=0, sticky="w", pady=5)
marks_entry = tk.Entry(form_frame, font=("Arial", 11), width=20)
marks_entry.grid(row=1, column=1, pady=5)

tk.Label(form_frame, text="Total Marks:", font=("Arial", 11), bg="#f0f4f8").grid(row=2, column=0, sticky="w", pady=5)
total_entry = tk.Entry(form_frame, font=("Arial", 11), width=20)
total_entry.grid(row=2, column=1, pady=5)

# Calculate Button
calc_btn = tk.Button(root, text="Calculate Grade", font=("Arial", 12, "bold"), bg="#243b53", fg="white", padx=10, pady=5, command=calculate_grade)
calc_btn.pack(pady=20)

# --- Results Section ---
result_frame = tk.LabelFrame(root, text=" Results ", font=("Arial", 11, "bold"), bg="#ffffff", padx=15, pady=15, width=300, height=150)
result_frame.pack_propagate(False) # Prevents the frame from shrinking
result_frame.pack()

result_name = tk.Label(result_frame, text="Name: ", font=("Arial", 11), bg="#ffffff")
result_name.pack(anchor="w", pady=2)

result_percentage = tk.Label(result_frame, text="Percentage: ", font=("Arial", 11), bg="#ffffff")
result_percentage.pack(anchor="w", pady=2)

result_status = tk.Label(result_frame, text="Status: ", font=("Arial", 11), bg="#ffffff")
result_status.pack(anchor="w", pady=2)

result_grade = tk.Label(result_frame, text="Grade: ", font=("Arial", 11, "bold"), bg="#ffffff")
result_grade.pack(anchor="w", pady=2)

root.mainloop()
