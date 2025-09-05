
import tkinter as tk
from tkinter import ttk

# Define logic for each option
def enable_logging():
    print("Logging enabled")

def use_gpu():
    print("GPU mode activated")

def verbose_output():
    print("Verbose output on")

def dry_run():
    print("Dry run initiated")

def send_email():
    print("Email notification will be sent")

def backup_data():
    print("Data backup started")

# Map checkbox labels to their logic functions
checkbox_actions = {
    "Enable Logging": enable_logging,
    "Use GPU": use_gpu,
    "Verbose Output": verbose_output,
    "Dry Run": dry_run,
    "Send Email Notification": send_email,
    "Backup Data": backup_data
}

# GUI setup
root = tk.Tk()
root.title("Program Options")

checkbox_vars = []

# Create checkboxes
for label in checkbox_actions.keys():
    var = tk.BooleanVar()
    checkbox = ttk.Checkbutton(root, text=label, variable=var)
    checkbox.pack(anchor='w', padx=10, pady=2)
    checkbox_vars.append(var)

# Run logic based on selected checkboxes
def run_program():
    print("\nRunning program with selected options:")
    for var, label in zip(checkbox_vars, checkbox_actions.keys()):
        if var.get():
            checkbox_actions[label]()  # Execute the associated function

# Run button
run_button = ttk.Button(root, text="Run Program", command=run_program)
run_button.pack(pady=10)

root.mainloop()
