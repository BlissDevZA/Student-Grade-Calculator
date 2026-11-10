import tkinter as tk
from tkinter import messagebox


class StudentGradeApp:
    """A GUI application for calculating a student's grade."""

    def __init__(self, root):
        """Initialise the application and create the GUI."""

        self.root = root
        self.root.title("Student Grade Calculator")
        self.root.geometry("400x300")

        # Student name label and entry
        self.name_label = tk.Label(root, text="Student Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.name_entry = tk.Entry(root, width=25)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Student mark label and entry
        self.mark_label = tk.Label(root, text="Mark:")
        self.mark_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.mark_entry = tk.Entry(root, width=25)
        self.mark_entry.grid(row=1, column=1, padx=10, pady=10)

        # Calculate Grade button
        self.calculate_button = tk.Button(
            root,
            text="Calculate Grade",
            command=self.calculate_grade
        )
        self.calculate_button.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=15
        )

        # Result label
        self.result_label = tk.Label(
            root,
            text="",
            wraplength=350
        )
        self.result_label.grid(
            row=3,
            column=0,
            columnspan=2,
            padx=10,
            pady=10
        )

        # Additional method: clear form
        self.clear_button = tk.Button(
            root,
            text="Clear",
            command=self.clear_form
        )
        self.clear_button.grid(
            row=4,
            column=0,
            columnspan=2,
            pady=10
        )

    def calculate_grade(self):
        """Calculate and display the student's grade."""

        name = self.name_entry.get().strip()

        try:
            mark = float(self.mark_entry.get())

            # Validate that the mark is between 0 and 100.
            if mark < 0 or mark > 100:
                raise ValueError

            # Determine the grade.
            if mark >= 75:
                grade = "Distinction (D)"
            elif mark >= 60:
                grade = "Merit (M)"
            elif mark >= 50:
                grade = "Pass (P)"
            else:
                grade = "Fail (F)"

            # Display the result in the required format.
            self.result_label.config(
                text=f"Student: {name} | Mark: {mark:g} | Grade: {grade}"
            )

        except ValueError:
            messagebox.showerror(
                "Invalid Mark",
                "Please enter a valid number between 0 and 100."
            )

    def clear_form(self):
        """Clear the input fields and result."""

        self.name_entry.delete(0, tk.END)
        self.mark_entry.delete(0, tk.END)
        self.result_label.config(text="")


# Create the main application window.
root = tk.Tk()

# Create an instance of the application class.
app = StudentGradeApp(root)

# Start the Tkinter event loop.
root.mainloop()
