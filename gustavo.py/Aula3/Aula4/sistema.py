import tkinter as tk
from tkinter import ttk, messagebox
import json
from pathlib import Path

# Constants for style and layout
BG_COLOR = "#ffffff"
FG_COLOR = "#374151"
ACCENT_COLOR = "#2563eb"
FONT_HEADER = ("Segoe UI", 24, "bold")
FONT_LABEL = ("Segoe UI", 12)
FONT_ENTRY = ("Segoe UI", 12)
FONT_BUTTON = ("Segoe UI", 12, "bold")
CARD_BG = "#f9fafb"
CARD_ROUNDED_RADIUS = 12
CARD_PADDING = 15
DATA_FILE = "data.json"


class EmployeeDependentManager(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Cadastro de Funcionários e Dependentes")
        self.geometry("900x700")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)

        # Data storage
        self.employees = []  # List of dicts: {id, name, position, dependents:[]}
        self.load_data()

        # Main container frame centered with max width
        self.container = tk.Frame(self, bg=BG_COLOR)
        self.container.pack(expand=True, fill="both", padx=30, pady=30)

        # Header
        self.header = tk.Label(
            self.container,
            text="Sistema de Cadastro de Funcionários e Dependentes",
            font=FONT_HEADER,
            fg=FG_COLOR,
            bg=BG_COLOR,
            pady=10,
        )
        self.header.pack(anchor="center", pady=(0, 20))

        # Frames for forms and list display
        self.forms_frame = tk.Frame(self.container, bg=BG_COLOR)
        self.forms_frame.pack(fill="x", pady=(0, 30))

        self.list_frame = tk.Frame(self.container, bg=BG_COLOR)
        self.list_frame.pack(fill="both", expand=True)

        # Build forms and list
        self.build_employee_form()
        self.build_dependent_form()
        self.build_list_view()

    def build_employee_form(self):
        # Employee Form Card
        frame = tk.Frame(self.forms_frame, bg=CARD_BG, bd=0, highlightthickness=0)
        frame.pack(side="left", fill="y", expand=True, padx=(0, 20), pady=10)

        # Title
        title = tk.Label(frame, text="Cadastrar Funcionário", font=("Segoe UI", 18, "bold"), fg=FG_COLOR, bg=CARD_BG)
        title.pack(anchor="w", padx=CARD_PADDING, pady=(CARD_PADDING, 10))

        # Form fields
        form_frame = tk.Frame(frame, bg=CARD_BG)
        form_frame.pack(fill="x", padx=CARD_PADDING)

        # Employee ID
        tk.Label(form_frame, text="ID do Funcionário:", font=FONT_LABEL, fg=FG_COLOR, bg=CARD_BG).grid(row=0, column=0, sticky="w", pady=6)
        self.emp_id_entry = ttk.Entry(form_frame, font=FONT_ENTRY)
        self.emp_id_entry.grid(row=0, column=1, sticky="ew", pady=6, padx=(10,0))

        # Employee Name
        tk.Label(form_frame, text="Nome Completo:", font=FONT_LABEL, fg=FG_COLOR, bg=CARD_BG).grid(row=1, column=0, sticky="w", pady=6)
        self.emp_name_entry = ttk.Entry(form_frame, font=FONT_ENTRY)
        self.emp_name_entry.grid(row=1, column=1, sticky="ew", pady=6, padx=(10,0))

        # Position
        tk.Label(form_frame, text="Cargo:", font=FONT_LABEL, fg=FG_COLOR, bg=CARD_BG).grid(row=2, column=0, sticky="w", pady=6)
        self.emp_position_entry = ttk.Entry(form_frame, font=FONT_ENTRY)
        self.emp_position_entry.grid(row=2, column=1, sticky="ew", pady=6, padx=(10,0))

        form_frame.columnconfigure(1, weight=1)

        # Add Employee Button
        add_btn = tk.Button(
            frame,
            text="Adicionar Funcionário",
            font=FONT_BUTTON,
            bg=ACCENT_COLOR,
            fg="#fff",
            activebackground="#1E40AF",
            activeforeground="#fff",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=self.add_employee,
            pady=8,
        )
        add_btn.pack(fill="x", padx=CARD_PADDING, pady=(20, CARD_PADDING))

    def build_dependent_form(self):
        # Dependent Form Card
        frame = tk.Frame(self.forms_frame, bg=CARD_BG, bd=0, highlightthickness=0)
        frame.pack(side="left", fill="y", expand=True, padx=(20, 0), pady=10)

        # Title
        title = tk.Label(frame, text="Cadastrar Dependente", font=("Segoe UI", 18, "bold"), fg=FG_COLOR, bg=CARD_BG)
        title.pack(anchor="w", padx=CARD_PADDING, pady=(CARD_PADDING, 10))

        # Form fields
        form_frame = tk.Frame(frame, bg=CARD_BG)
        form_frame.pack(fill="x", padx=CARD_PADDING)

        # Employee selector combobox
        tk.Label(form_frame, text="Funcionário:", font=FONT_LABEL, fg=FG_COLOR, bg=CARD_BG).grid(row=0, column=0, sticky="w", pady=6)
        self.emp_select = ttk.Combobox(form_frame, font=FONT_ENTRY, state="readonly")
        self.emp_select.grid(row=0, column=1, sticky="ew", pady=6, padx=(10, 0))

        # Dependent Name
        tk.Label(form_frame, text="Nome do Dependente:", font=FONT_LABEL, fg=FG_COLOR, bg=CARD_BG).grid(row=1, column=0, sticky="w", pady=6)
        self.dep_name_entry = ttk.Entry(form_frame, font=FONT_ENTRY)
        self.dep_name_entry.grid(row=1, column=1, sticky="ew", pady=6, padx=(10, 0))

        # Dependent Relationship
        tk.Label(form_frame, text="Parentesco:", font=FONT_LABEL, fg=FG_COLOR, bg=CARD_BG).grid(row=2, column=0, sticky="w", pady=6)
        self.dep_relation_entry = ttk.Entry(form_frame, font=FONT_ENTRY)
        self.dep_relation_entry.grid(row=2, column=1, sticky="ew", pady=6, padx=(10, 0))

        form_frame.columnconfigure(1, weight=1)

        # Add Dependent Button
        add_btn = tk.Button(
            frame,
            text="Adicionar Dependente",
            font=FONT_BUTTON,
            bg=ACCENT_COLOR,
            fg="#fff",
            activebackground="#1E40AF",
            activeforeground="#fff",
            bd=0,
            relief="flat",
            cursor="hand2",
            command=self.add_dependent,
            pady=8,
        )
        add_btn.pack(fill="x", padx=CARD_PADDING, pady=(20, CARD_PADDING))

        self.update_employee_options()

    def build_list_view(self):
        # List card with white background and subtle rounding and shadow effect (simulated)
        frame = tk.Frame(self.list_frame, bg=CARD_BG)
        frame.pack(fill="both", expand=True)

        # Title
        title = tk.Label(frame, text="Funcionários Cadastrados", font=("Segoe UI", 18, "bold"), fg=FG_COLOR, bg=CARD_BG)
        title.pack(anchor="w", padx=CARD_PADDING, pady=(CARD_PADDING, 10))

        # Treeview for display employees and dependents
        columns = ("ID", "Nome", "Cargo", "Dependentes")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=13)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="w", stretch=True)
        self.tree.pack(fill="both", expand=True, padx=CARD_PADDING, pady=(0, CARD_PADDING))

        self.refresh_treeview()

    def add_employee(self):
        emp_id = self.emp_id_entry.get().strip()
        name = self.emp_name_entry.get().strip()
        position = self.emp_position_entry.get().strip()

        if not emp_id or not name or not position:
            messagebox.showerror("Erro", "Todos os campos do funcionário são obrigatórios.")
            return

        if any(emp['id'] == emp_id for emp in self.employees):
            messagebox.showerror("Erro", f"ID '{emp_id}' já está cadastrado.")
            return

        new_emp = {"id": emp_id, "name": name, "position": position, "dependents": []}
        self.employees.append(new_emp)
        self.save_data()
        self.clear_employee_form()
        self.update_employee_options()
        self.refresh_treeview()
        messagebox.showinfo("Sucesso", f"Funcionário '{name}' adicionado com sucesso.")

    def add_dependent(self):
        selected_emp_index = self.emp_select.current()
        dep_name = self.dep_name_entry.get().strip()
        dep_relation = self.dep_relation_entry.get().strip()

        if selected_emp_index == -1:
            messagebox.showerror("Erro", "Selecione um funcionário para associar o dependente.")
            return

        if not dep_name or not dep_relation:
            messagebox.showerror("Erro", "Todos os campos do dependente são obrigatórios.")
            return

        emp = self.employees[selected_emp_index]
        emp['dependents'].append({"name": dep_name, "relation": dep_relation})
        self.save_data()
        self.clear_dependent_form()
        self.refresh_treeview()
        messagebox.showinfo("Sucesso", f"Dependente '{dep_name}' adicionado ao funcionário '{emp['name']}'.")

    def clear_employee_form(self):
        self.emp_id_entry.delete(0, tk.END)
        self.emp_name_entry.delete(0, tk.END)
        self.emp_position_entry.delete(0, tk.END)

    def clear_dependent_form(self):
        self.dep_name_entry.delete(0, tk.END)
        self.dep_relation_entry.delete(0, tk.END)
        self.emp_select.set("")

    def update_employee_options(self):
        emp_names = [f"{emp['name']} (ID: {emp['id']})" for emp in self.employees]
        self.emp_select['values'] = emp_names
        self.emp_select.set("")

    def refresh_treeview(self):
        self.tree.delete(*self.tree.get_children())
        for emp in self.employees:
            deps_str = ", ".join([f"{d['name']} ({d['relation']})" for d in emp.get('dependents', [])]) if emp.get('dependents') else "-"
            self.tree.insert("", "end", values=(emp['id'], emp['name'], emp['position'], deps_str))

    def load_data(self):
        if Path(DATA_FILE).exists():
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    self.employees = json.load(f)
            except Exception:
                self.employees = []
        else:
            self.employees = []

    def save_data(self):
        try:
            with open(DATA_FILE, "w", encoding="utf-8") as f:
                json.dump(self.employees, f, ensure_ascii=False, indent=4)
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar dados: {e}")


if __name__ == "__main__":
    app = EmployeeDependentManager()
    app.mainloop()

