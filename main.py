import tkinter as tk

# Function to update the expression in the entry field
def press(num):
    current = entry_field.get()
    entry_field.delete(0, tk.END)
    entry_field.insert(tk.END, current + str(num))

# Function to evaluate the final expression
def equal_press():
    try:
        total = str(eval(entry_field.get()))
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, total)
    except:
        entry_field.delete(0, tk.END)
        entry_field.insert(tk.END, "Error")

# Function to clear the entry field
def clear():
    entry_field.delete(0, tk.END)

# Set up the main application window
window = tk.Tk()
window.title("Simple Calculator")

# Create an entry field to display the expression/result
entry_field = tk.Entry(window, width=35, borderwidth=5, font=('Arial', 18))
entry_field.grid(row=0, column=0, columnspan=4)

# Define button values
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

# Function to create the buttons and place them in the grid
def create_buttons():
    row = 1
    col = 0
    for button in buttons:
        if button == "=":
            tk.Button(window, text=button, width=9, height=3, command=equal_press).grid(row=row, column=col, columnspan=2)
        elif button == "C":
            tk.Button(window, text=button, width=9, height=3, command=clear).grid(row=row, column=col)
        else:
            tk.Button(window, text=button, width=9, height=3, command=lambda button=button: press(button)).grid(row=row, column=col)
        
        col += 1
        if col > 3:
            col = 0
            row += 1

# Call the function to create the buttons
create_buttons()

# Start the Tkinter main loop
window.mainloop()
