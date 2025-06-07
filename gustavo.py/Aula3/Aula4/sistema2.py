import tkinter as tk
from tkinter import ttk, messagebox
import json
from pathlib import Path

# Design Constants
BG_COLOR = "#ffffff"
FG_COLOR = "#323130"             # Dark gray text color
SUBTEXT_COLOR = "#6b7280"        # Neutral gray
ACCENT_COLOR = "#2563eb"         # Modern blue accent
ACCENT_HOVER = "#1e40af"
ACCENT_ACTIVE = "#1e3a8a"
CARD_BG = "#f9fafb"
FONT_HEADER = ("Segoe UI Semibold", 48, "bold")
FONT_SUBHEADER = ("Segoe UI", 20)
FONT_LABEL = ("Segoe UI", 14)
FONT_ENTRY = ("Segoe UI", 14)
FONT_BUTTON = ("Segoe UI Semibold", 14)
DATA_FILE = "employees_dependents.json"
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 720
CARD_PADDING = 30


class EmployeeDependentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Profissional de Cadastro de Funcionários e Dependentes")
        self.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)

        # Load Data Store (list of employees)
        self.employees = []
        self.load_data()

        # Build UI
        self.build_navbar()
        self.container = tk.Frame(self, bg=BG_COLOR)
        self.container.pack(fill="both", expand=True, padx=40, pady=24)

        self.build_header()
        self.build_forms_area()
        self.build_list_area()

    def build_navbar(self):
        navbar = tk.Frame(self, bg=BG_COLOR, height=56)
        navbar.pack(side="top", fill="x", pady=(0, 4))
        navbar.pack_propagate(False)

        # Logo text
        logo = tk.Label(navbar, text="CompanyX", fg=ACCENT_COLOR, bg=BG_COLOR,
                        font=("Segoe UI Semibold", 24), cursor="hand2")
        logo.pack(side="left", padx=24)

        # Navigation items
        nav_frame = tk.Frame(navbar, bg=BG_COLOR)
        nav_frame.pack(side="right", padx=24)

        nav_items = ["Funcionários", "Dependentes", "Relatórios"]
        for item in nav_items:
            lbl = tk.Label(nav_frame, text=item, fg=SUBTEXT_COLOR, bg=BG_COLOR,
                           font=FONT_LABEL, cursor="hand2")
            lbl.pack(side="left", padx=18)
            lbl.bind("<Enter>", lambda e, w=lbl: w.config(fg=ACCENT_COLOR))
            lbl.bind("<Leave>", lambda e, w=lbl: w.config(fg=SUBTEXT_COLOR))

    def build_header(self):
        header = tk.Label(self.container,
                          text="Gerencie Funcionários e seus Dependentes",
                          font=FONT_HEADER, fg=FG_COLOR, bg=BG_COLOR,
                          anchor="w", justify="left")
        header.pack(fill="x", pady=(0, 12))

        subheader = tk.Label(self.container,
                             text="Um sistema profissional, com design moderno, para cadastro intuitivo e eficiente.",
                             font=FONT_SUBHEADER, fg=SUBTEXT_COLOR, bg=BG_COLOR,
                             anchor="w", justify="left")
        subheader.pack(fill="x", pady=(0, 40))

    def build_forms_area(self):
        forms_frame = tk.Frame(self.container, bg=BG_COLOR)
        forms_frame.pack(fill="x", pady=(0, 40))

        # Employee form card
        self.emp_card = self.create_card(forms_frame)
        self.emp_card.pack(side="left", fill="both", expand=True, padx=(0, 24))

        self.build_employee_form(self.emp_card)

        # Dependent form card
        self.dep_card = self.create_card(forms_frame)
        self.dep_card.pack(side="left", fill="both", expand=True, padx=(24, 0))

        self.build_dependent_form(self.dep_card)

    def create_card(self, parent):
        card = tk.Frame(parent, bg=CARD_BG, bd=0, highlightthickness=0)
        card.config(padx=CARD_PADDING, pady=CARD_PADDING)
        card.config(relief="groove", bd=1)
        return card

    def build_employee_form(self, parent):
        title = tk.Label(parent, text="Cadastrar Funcionário",
                         font=("Segoe UI Semibold", 20), fg=FG_COLOR, bg=CARD_BG)
        title.pack(anchor="w", pady=(0, 20))

        form = tk.Frame(parent, bg=CARD_BG)
        form.pack(fill="x")

        # ID
        tk.Label(form, text="ID do Funcionário:", font=FONT_LABEL, fg=FG_COLOR, bg=CARD_BG).grid(row=0, column=0, sticky="w", pady=16)
        self.emp_id_entry = ttk.Entry(form, font=FONT_ENTRY)
        self.emp_id_entry.grid(row=0, column=1, sticky="ew", pady=16, padx=(12, 0))

        # Name
        tk.Label(form, text="Nome Completo:", font=FONT_LABEL, fg=FG_COLOR, bg=CARD_BG).grid(row=1, column=0, sticky="w", pady=16)
        self.emp_name_entry = ttk.Entry(form, font=FONT_ENTRY)
        self.emp_name_entry.grid(row=1, column=1, sticky="ew", pady=16, padx=(12, 0))

        # Role/Position
        tk.Label(form, text="Cargo:", font=FONT_LABEL, fg=FG_COLOR, bg=CARD_BG).grid(row=2, column=0, sticky="w", pady=16)
        self.emp_role_entry = ttk.Entry(form, font=FONT_ENTRY)
        self.emp_role_entry.grid(row=2, column=1, sticky="ew", pady=16, padx=(12, 0))

        form.columnconfigure(1, weight=1)

        add_btn = tk.Button(parent, text="Adicionar Funcionário", font=FONT_BUTTON,
                            bg=ACCENT_COLOR, fg="#ffffff", bd=0, relief="flat",
                            activebackground=ACCENT_ACTIVE, activeforeground="#ffffff",
                            cursor="hand2", pady=12, command=self.add_employee)
        add_btn.pack(fill="x", pady=(24, 0))
        add_btn.bind("<Enter>", lambda e: add_btn.config(bg=ACCENT_HOVER))
        add_btn.bind("<Leave>", lambda e: add_btn.config(bg=ACCENT_COLOR))

    def build_dependent_form(self, parent):
        title = tk.Label(parent, text="Cadastrar Dependente",
                         font=("Segoe UI Semibold", 20), fg=FG_COLOR, bg=CARD_BG)
        title.pack(anchor="w", pady=(0, 20))

        form = tk.Frame(parent, bg=CARD_BG)
        form.pack(fill="x")

        # Select employee combobox
        tk.Label(form, text="Funcionário:", font=FONT_LABEL, fg=FG_COLOR, bg=CARD_BG).grid(row=0, column=0, sticky="w", pady=16)
        self.emp_select = ttk.Combobox(form, font=FONT_ENTRY, state="readonly")
        self.emp_select.grid(row=0, column=1, sticky="ew", pady=16, padx=(12, 0))

        # Dependent name
        tk.Label(form, text="Nome do Dependente:", font=FONT_LABEL, fg=FG_COLOR, bg=CARD_BG).grid(row=1, column=0, sticky="w", pady=16)
        self.dep_name_entry = ttk.Entry(form, font=FONT_ENTRY)
        self.dep_name_entry.grid(row=1, column=1, sticky="ew", pady=16, padx=(12, 0))

        # Dependent relationship
        tk.Label(form, text="Parentesco:", font=FONT_LABEL, fg=FG_COLOR, bg=CARD_BG).grid(row=2, column=0, sticky="w", pady=16)
        self.dep_rel_entry = ttk.Entry(form, font=FONT_ENTRY)
        self.dep_rel_entry.grid(row=2, column=1, sticky="ew", pady=16, padx=(12, 0))

        form.columnconfigure(1, weight=1)

        add_btn = tk.Button(parent, text="Adicionar Dependente", font=FONT_BUTTON,
                            bg=ACCENT_COLOR, fg="#ffffff", bd=0, relief="flat",
                            activebackground=ACCENT_ACTIVE, activeforeground="#ffffff",
                            cursor="hand2", pady=12, command=self.add_dependent)
        add_btn.pack(fill="x", pady=(24, 0))
        add_btn.bind("<Enter>", lambda e: add_btn.config(bg=ACCENT_HOVER))
        add_btn.bind("<Leave>", lambda e: add_btn.config(bg=ACCENT_COLOR))

        self.update_emp_select_options()

    def build_list_area(self):
        # List card
        list_card = self.create_card(self.container)
        list_card.pack(fill="both", expand=True)

        title = tk.Label(list_card, text="Funcionários Cadastrados", font=("Segoe UI Semibold", 22),
                         fg=FG_COLOR, bg=CARD_BG, anchor="w")
        title.pack(anchor="w", pady=(0, 20))

        columns = ("ID", "Nome", "Cargo", "Dependentes")
        self.tree = ttk.Treeview(list_card, columns=columns, show="headings", height=14)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="w")

        self.tree.pack(fill="both", expand=True)

        style = ttk.Style()
        style.configure("Treeview", font=FONT_LABEL, rowheight=32)
        style.configure("Treeview.Heading", font=("Segoe UI Semibold", 14))
        style.map("Treeview",
                  background=[('selected', ACCENT_COLOR)],
                  foreground=[('selected', '#ffffff')])

        self.refresh_list()

    def add_employee(self):
        emp_id = self.emp_id_entry.get().strip()
        name = self.emp_name_entry.get().strip()
        role = self.emp_role_entry.get().strip()

        if not emp_id or not name or not role:
            messagebox.showerror("Erro", "Preencha todos os campos do funcionário.")
            return

        if any(emp['id'] == emp_id for emp in self.employees):
            messagebox.showerror("Erro", f"ID '{emp_id}' já está cadastrado.")
            return

        self.employees.append({"id": emp_id, "name": name, "role": role, "dependents": []})
        self.save_data()
        self.clear_employee_form()
        self.update_emp_select_options()
        self.refresh_list()
        messagebox.showinfo("Sucesso", f"Funcionário '{name}' cadastrado.")

    def add_dependent(self):
        selected_idx = self.emp_select.current()
        dep_name = self.dep_name_entry.get().strip()
        dep_rel = self.dep_rel_entry.get().strip()

        if selected_idx == -1:
            messagebox.showerror("Erro", "Selecione um funcionário para associar o dependente.")
            return

        if not dep_name or not dep_rel:
            messagebox.showerror("Erro", "Preencha todos os campos do dependente.")
            return

        self.employees[selected_idx]["dependents"].append({"name": dep_name, "relation": dep_rel})
        self.save_data()
        self.clear_dependent_form()
        self.refresh_list()
        messagebox.showinfo("Sucesso", f"Dependente '{dep_name}' adicionado ao funcionário '{self.employees[selected_idx]['name']}'.")

    def clear_employee_form(self):
        self.emp_id_entry.delete(0, tk.END)
        self.emp_name_entry.delete(0, tk.END)
        self.emp_role_entry.delete(0, tk.END)

    def clear_dependent_form(self):
        self.dep_name_entry.delete(0, tk.END)
        self.dep_rel_entry.delete(0, tk.END)
        self.emp_select.set("")

    def update_emp_select_options(self):
        options = [f"{emp['name']} (ID: {emp['id']})" for emp in self.employees]
        self.emp_select['values'] = options
        self.emp_select.set("")

    def refresh_list(self):
        self.tree.delete(*self.tree.get_children())
        for emp in self.employees:
            deps = ", ".join(f"{d['name']} ({d['relation']})" for d in emp.get("dependents", [])) or "-"
            self.tree.insert("", "end", values=(emp["id"], emp["name"], emp["role"], deps))

    def load_data(self):
        path = Path(DATA_FILE)
        if path.exists():
            try:
                with open(path, "r", encoding="utf-8") as file:
                    self.employees = json.load(file)
            except Exception:
                self.employees = []
        else:
            self.employees = []

    def save_data(self):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as file:
                json.dump(self.employees, file, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar dados: {e}")


if __name__ == "__main__":
    app = EmployeeDependentApp()
    app.mainloop()
