import tkinter as tk
from tkinter import ttk

class GPA_Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("GPA Calculator")

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Header
        headers = ["Name", "Grade Obtained", "Credit Hour"]
        for col, header in enumerate(headers):
            lbl = tk.Label(self.master, text=header)
            lbl.grid(row=0, column=col, padx=5, pady=5)

        # Subject Entries
        self.subject_entries = []
        self.add_subject_entry()

        # Add Subject Button
        add_subject_btn = tk.Button(self.master, text="Add Subject", command=self.add_subject_entry)
        add_subject_btn.grid(column=5,row=(len(self.subject_entries) + 1), columnspan=3, pady=10)

        # Calculate Button
        calculate_btn = tk.Button(self.master, text="Calculate GPA", command=self.calculate_gpa)
        calculate_btn.grid(column=5, row=len(self.subject_entries) + 2, columnspan=3, pady=10)

    def add_subject_entry(self):
        row = len(self.subject_entries) + 1

        # Name Entry
        name_entry = tk.Entry(self.master)
        name_entry.grid(row=row, column=0, padx=5, pady=5)

        # Grade Dropdown
        grades = ["A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"]
        grade_var = tk.StringVar()
        grade_dropdown = ttk.Combobox(self.master, textvariable=grade_var, values=grades)
        grade_dropdown.grid(row=row, column=1, padx=5, pady=5)
        grade_dropdown.set(grades[0])  # Set default value

        # Credit Hour Dropdown
        credit_hours = [1, 2, 3]
        credit_hour_var = tk.StringVar()
        credit_hour_dropdown = ttk.Combobox(self.master, textvariable=credit_hour_var, values=credit_hours)
        credit_hour_dropdown.grid(row=row, column=2, padx=5, pady=5)
        credit_hour_dropdown.set(credit_hours[0])  # Set default value

        # Store the entry widgets
        self.subject_entries.append((name_entry, grade_var, credit_hour_var))

    def calculate_gpa(self):
        total_points = 0
        total_credit_hours = 0

        for name_entry, grade_var, credit_hour_var in self.subject_entries:
            grade = grade_var.get()
            credit_hour = int(credit_hour_var.get())

            # Calculate points based on the grade
            #grade_points = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}
            grade_points = {'A': 4.0, 'A-': 3.67, 'B+': 3.33, 'B': 3.0, 'B-': 2.67, 'C+': 2.33, 'C': 2.0, 'C-': 1.67, 'D+': 1.33, 'D': 1.0, 'F': 0.0}

            
            total_points += grade_points.get(grade, 0) * credit_hour
            total_credit_hours += credit_hour

        if total_credit_hours > 0:
            gpa = total_points / total_credit_hours
            result_str = f"Your GPA is: {gpa:.2f}"
        else:
            result_str = "Enter at least one subject to calculate GPA."

        result_label = tk.Label(self.master, text=result_str, font=("Helvetica", 12))
        result_label.grid(row=len(self.subject_entries) + 3, columnspan=3, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = GPA_Calculator(root)
    root.mainloop()
