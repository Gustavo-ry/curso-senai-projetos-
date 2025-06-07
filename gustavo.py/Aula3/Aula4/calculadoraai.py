import tkinter as tk
from tkinter import font

class ProfessionalCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculadora Profissional")
        self.geometry("380x520")
        self.configure(bg="#ffffff")
        self.resizable(False, False)

        # Fonts
        self.display_font = font.Font(family="Segoe UI", size=32, weight="bold")
        self.button_font = font.Font(family="Segoe UI", size=18, weight="bold")

        # Display Entry
        self.display_var = tk.StringVar()
        self.display = tk.Entry(
            self,
            textvariable=self.display_var,
            font=self.display_font,
            bg="#f9fafb",
            fg="#111827",
            bd=0,
            justify="right",
            relief="flat",
            highlightthickness=2,
            highlightbackground="#e5e7eb",
            highlightcolor="#2563eb",
            insertbackground="#2563eb"
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=24, pady=(24, 40), ipady=20)

        # Button styling parameters
        self.btn_bg_default = "#f3f4f6"
        self.btn_fg_default = "#111827"
        self.btn_bg_operator = "#dbeafe"
        self.btn_fg_operator = "#2563eb"
        self.btn_bg_clear = "#fee2e2"
        self.btn_fg_clear = "#b91c1c"
        self.btn_bg_equal = "#2563eb"
        self.btn_fg_equal = "#ffffff"

        # Buttons layout: (text, row, column, colspan, bg, fg, command)
        buttons = [
            ("C", 1, 0, 1, self.btn_bg_clear, self.btn_fg_clear, self.clear),
            ("%", 1, 1, 1, self.btn_bg_operator, self.btn_fg_operator, self.percent),
            ("÷", 1, 2, 1, self.btn_bg_operator, self.btn_fg_operator, lambda: self.add_to_expression("/")),
            ("×", 1, 3, 1, self.btn_bg_operator, self.btn_fg_operator, lambda: self.add_to_expression("*")),

            ("7", 2, 0, 1, self.btn_bg_default, self.btn_fg_default, lambda: self.add_to_expression("7")),
            ("8", 2, 1, 1, self.btn_bg_default, self.btn_fg_default, lambda: self.add_to_expression("8")),
            ("9", 2, 2, 1, self.btn_bg_default, self.btn_fg_default, lambda: self.add_to_expression("9")),
            ("−", 2, 3, 1, self.btn_bg_operator, self.btn_fg_operator, lambda: self.add_to_expression("-")),

            ("4", 3, 0, 1, self.btn_bg_default, self.btn_fg_default, lambda: self.add_to_expression("4")),
            ("5", 3, 1, 1, self.btn_bg_default, self.btn_fg_default, lambda: self.add_to_expression("5")),
            ("6", 3, 2, 1, self.btn_bg_default, self.btn_fg_default, lambda: self.add_to_expression("6")),
            ("+", 3, 3, 2, self.btn_bg_operator, self.btn_fg_operator, lambda: self.add_to_expression("+")),

            ("1", 4, 0, 1, self.btn_bg_default, self.btn_fg_default, lambda: self.add_to_expression("1")),
            ("2", 4, 1, 1, self.btn_bg_default, self.btn_fg_default, lambda: self.add_to_expression("2")),
            ("3", 4, 2, 1, self.btn_bg_default, self.btn_fg_default, lambda: self.add_to_expression("3")),

            ("0", 5, 0, 2, self.btn_bg_default, self.btn_fg_default, lambda: self.add_to_expression("0")),
            (".", 5, 2, 1, self.btn_bg_default, self.btn_fg_default, lambda: self.add_to_expression(".")),
            ("=", 5, 3, 1, self.btn_bg_equal, self.btn_fg_equal, self.calculate),
        ]

        # Create buttons
        for (text, row, col, colspan, bg, fg, cmd) in buttons:
            self.create_button(text, row, col, colspan, bg, fg, cmd)

        # Configure grid weights for a balanced layout
        for r in range(6):
            self.grid_rowconfigure(r, weight=1)
        for c in range(4):
            self.grid_columnconfigure(c, weight=1)

    def create_button(self, text, row, column, colspan, bg, fg, command):
        btn = tk.Button(
            self,
            text=text,
            font=self.button_font,
            bg=bg,
            fg=fg,
            activebackground="#93c5fd",
            activeforeground="#1e3a8a",
            bd=0,
            relief="flat",
            command=command,
            cursor="hand2",
            highlightthickness=0,
            padx=10,
            pady=10,
        )
        btn.grid(row=row, column=column, columnspan=colspan, sticky="nsew", padx=18, pady=12)

        # Implement hover effect: brighten background
        def on_enter(e):
            btn['bg'] = "#bfdbfe"
        def on_leave(e):
            btn['bg'] = bg

        # Only add hover effect to non-equal buttons for better UX
        if text != "=":
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)

    def add_to_expression(self, char):
        current = self.display_var.get()
        if current == "Erro":
            self.display_var.set(char)
        else:
            self.display_var.set(current + char)

    def clear(self):
        self.display_var.set("")

    def percent(self):
        expression = self.display_var.get()
        try:
            # Evaluate current expression then divide by 100
            value = float(eval(expression))
            percent_value = value / 100
            self.display_var.set(str(percent_value))
        except Exception:
            self.display_var.set("Erro")

    def calculate(self):
        expression = self.display_var.get()
        try:
            result = str(eval(expression))
            self.display_var.set(result)
        except Exception:
            self.display_var.set("Erro")

if __name__ == "__main__":
    app = ProfessionalCalculator()
    app.mainloop()
