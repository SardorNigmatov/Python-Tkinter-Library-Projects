import tkinter as tk

def on_click(button_value):
    current_text = entry_var.get()
    
    if button_value == '=':
        try:
            result = eval(current_text)
            entry_var.set(result)
        except Exception as e:
            entry_var.set("Error")
    elif button_value == 'C':
        entry_var.set("")
    else:
        entry_var.set(current_text + str(button_value))

root = tk.Tk()
root.title("Simple Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=('Arial', 14),borderwidth=5,border=4)
entry.grid(row=0, column=0, columnspan=10)

# Define buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Times New Roman', 12),
              command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Run the main loop
root.mainloop()

