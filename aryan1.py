import tkinter as tk

# Create window
root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("320x420")
root.configure(bg="#2c3e50")

# Entry (display)
entry = tk.Entry(
    root,
    width=18,
    font=("Arial", 20),
    borderwidth=5,
    relief="ridge",
    justify="right",
    bg="white",
    fg="black"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# Functions
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Button style
btn_font = ("Arial", 14)
num_color = "#ecf0f1"
op_color = "#f39c12"

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 1
col = 0

for b in buttons:
    if b == '=':
        tk.Button(
            root, text=b, width=5, height=2,
            font=btn_font, bg="#27ae60", fg="white",
            command=calculate
        ).grid(row=row, column=col, padx=5, pady=5)

    elif b in ['+','-','*','/']:
        tk.Button(
            root, text=b, width=5, height=2,
            font=btn_font, bg=op_color, fg="black",
            command=lambda x=b: click(x)
        ).grid(row=row, column=col, padx=5, pady=5)

    else:   # <-- THIS FIXES YOUR BUG (numbers & dot button)
        tk.Button(
            root, text=b, width=5, height=2,
            font=btn_font, bg=num_color, fg="black",
            command=lambda x=b: click(x)
        ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(
    root, text="CLEAR", width=22, height=2,
    font=btn_font, bg="#e74c3c", fg="white",
    command=clear
).grid(row=row, column=0, columnspan=4, padx=5, pady=10)

# Run app
root.mainloop()
