import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Calculator")

        # Entry widget for input/output
        self.entry = tk.Entry(root, width=20, font=("Arial", 18), borderwidth=5, relief="ridge", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button layout
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        for (text, row, col) in buttons:
            self.add_button(text, row, col)

        # Clear button
        clear_btn = tk.Button(root, text="C", width=5, height=2, font=("Arial", 14), command=self.clear_entry)
        clear_btn.grid(row=5, column=0, columnspan=4, sticky="we")

    def add_button(self, text, row, col):
        btn = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 14),
                        command=lambda t=text: self.on_button_click(t))
        btn.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, char)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

# Run calculator
root = tk.Tk()
calc = Calculator(root)
root.mainloop()