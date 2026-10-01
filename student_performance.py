import tkinter as tk
from tkinter import ttk, messagebox


class StudentResult:
    def __init__(self, name, subject, assignment, test, exam):
        self.name = name
        self.subject = subject
        self.assignment = assignment
        self.test = test
        self.exam = exam

    def calculate_score(self):
        return self.assignment * 0.30 + self.test * 0.30 + self.exam * 0.40

    def get_grade(self):
        score = self.calculate_score()

        if score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        else:
            return "F"

    def get_status(self):
        return "PASS" if self.calculate_score() >= 50 else "FAIL"

    def __str__(self):
        return f"{self.name} | {self.subject} | {self.calculate_score():.2f}% | Grade {self.get_grade()}"


def calculate_result():
    try:
        name = name_entry.get().strip()
        subject = subject_box.get()

        if name == "":
            raise ValueError("Please enter student name.")

        if subject == "":
            raise ValueError("Please select a subject.")

        assignment = float(assignment_entry.get())
        test = float(test_entry.get())
        exam = float(exam_entry.get())

        for mark in [assignment, test, exam]:
            if mark < 0 or mark > 100:
                raise ValueError("Marks must be between 0 and 100.")

        student = StudentResult(name, subject, assignment, test, exam)

        score_label.config(text=f"{student.calculate_score():.2f}%")
        grade_label.config(text=student.get_grade())
        status_label.config(text=student.get_status())
        summary_label.config(text=str(student))

    except ValueError as error:
        messagebox.showerror("Invalid Input", str(error))


def clear_fields():
    for entry in [name_entry, assignment_entry, test_entry, exam_entry]:
        entry.delete(0, tk.END)

    subject_box.set("")
    score_label.config(text="-")
    grade_label.config(text="-")
    status_label.config(text="-")
    summary_label.config(text="No result calculated yet.")
    name_entry.focus()


def exit_program():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        root.destroy()


root = tk.Tk()
root.title("Student Performance Analyzer")
root.geometry("620x580")
root.resizable(False, False)

style = ttk.Style()
style.configure("Title.TLabel", font=("Arial", 20, "bold"))
style.configure("Heading.TLabel", font=("Arial", 11, "bold"))
style.configure("Result.TLabel", font=("Arial", 14, "bold"))

main = ttk.Frame(root, padding=25)
main.pack(fill="both", expand=True)

ttk.Label(
    main,
    text="Student Performance Analyzer",
    style="Title.TLabel"
).pack()

ttk.Label(
    main,
    text="Academic Result Calculator"
).pack(pady=(0, 15))

input_frame = ttk.LabelFrame(
    main,
    text="Student Information",
    padding=15
)
input_frame.pack(fill="x", pady=10)

labels = [
    "Student Name",
    "Assignment Mark",
    "Test Mark",
    "Final Exam Mark"
]

for i, text in enumerate(labels):
    ttk.Label(
        input_frame,
        text=text + ":"
    ).grid(row=i, column=0, sticky="w", pady=6)

name_entry = ttk.Entry(input_frame, width=30)
assignment_entry = ttk.Entry(input_frame, width=30)
test_entry = ttk.Entry(input_frame, width=30)
exam_entry = ttk.Entry(input_frame, width=30)

entries = [
    name_entry,
    assignment_entry,
    test_entry,
    exam_entry
]

for i, entry in enumerate(entries):
    entry.grid(row=i, column=1, padx=10, pady=6)

ttk.Label(
    input_frame,
    text="Subject:"
).grid(row=4, column=0, sticky="w", pady=6)

subject_box = ttk.Combobox(
    input_frame,
    width=27,
    state="readonly",
    values=[
        "Python Programming",
        "Database",
        "Networking",
        "Web Development"
    ]
)
subject_box.grid(row=4, column=1, padx=10, pady=6)

button_frame = ttk.Frame(main)
button_frame.pack(pady=15)

ttk.Button(
    button_frame,
    text="Calculate Result",
    command=calculate_result
).grid(row=0, column=0, padx=5)

ttk.Button(
    button_frame,
    text="Clear",
    command=clear_fields
).grid(row=0, column=1, padx=5)

ttk.Button(
    button_frame,
    text="Exit",
    command=exit_program
).grid(row=0, column=2, padx=5)

result_frame = ttk.LabelFrame(
    main,
    text="Performance Result",
    padding=15
)
result_frame.pack(fill="x", pady=10)

ttk.Label(result_frame, text="Final Score:").grid(row=0, column=0, sticky="w", pady=5)
ttk.Label(result_frame, text="Grade:").grid(row=1, column=0, sticky="w", pady=5)
ttk.Label(result_frame, text="Status:").grid(row=2, column=0, sticky="w", pady=5)

score_label = ttk.Label(result_frame, text="-", style="Result.TLabel")
grade_label = ttk.Label(result_frame, text="-", style="Result.TLabel")
status_label = ttk.Label(result_frame, text="-", style="Result.TLabel")

score_label.grid(row=0, column=1, padx=25)
grade_label.grid(row=1, column=1, padx=25)
status_label.grid(row=2, column=1, padx=25)

summary_label = ttk.Label(
    main,
    text="No result calculated yet."
)
summary_label.pack(pady=15)

name_entry.focus()
root.mainloop()