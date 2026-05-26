import csv
import os
import datetime
import sys
import customtkinter as ctk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


FILE_NAME = "finance.csv"
HEADERS = ["date", "description", "amount", "type", "Total_balance", "Net_balance"]
file_name = "Summary.csv"
HEADERS2 = ["description", "amount"]
# current total balance (set at program start)
Total_balance = 0.0

# Global variables for UI components
app = None
total_balance_entry = None
desc_option = None
amount_entry = None
output_box = None
limits_vars = {}

categories = [
    "Housing & Rent",
    "Food & Groceries",
    "Transportation",
    "Bills & Services",
    "Shopping & Needs",
    "Health & Care",
    "Entertainment",
    "Education",
    "Salary",
    "Others",
]


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()


#  Adds the user's data inside the CSV File
def add_transactions(transaction_data):
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS)
        writer.writerow(transaction_data)


# Puts the user's data in a List of Dictionaries
def get_transactions():
    transactions = []
    try:
        with open(FILE_NAME) as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        # If file doesn't exist yet, just return an empty list
        return []
    return transactions


def initialize_file2():
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=HEADERS2)
            writer.writeheader()


def summarize_data(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10):
    summary_dict = {
        "Housing & Rent": 0,
        "Food & Groceries": 0,
        "Transportation": 0,
        "Bills & Services": 0,
        "Shopping & Needs": 0,
        "Health & Care": 0,
        "Entertainment": 0,
        "Education": 0,
        "Salary": 0,
        "Others": 0,
    }
    data = get_transactions()
    result = []
    for items in data:
        if items["description"] in summary_dict:
            summary_dict[items["description"]] += float(items["amount"])

    for key, value in summary_dict.items():
        if value == 0:
            continue
        else:
            result.append({"description": key, "amount": value})

    summary_limits = {
        "Housing & Rent": v1,
        "Food & Groceries": v2,
        "Transportation": v3,
        "Bills & Services": v4,
        "Shopping & Needs": v5,
        "Health & Care": v6,
        "Entertainment": v7,
        "Education": v8,
        "Salary": v9,
        "Others": v10,
    }

    for key, value in summary_dict.items():
        if float(summary_limits[key])==0:
            pass
        elif float(value) > float(summary_limits[key]):
            print(
                "Warning! You have exceeded the limit by",
                (float(value) - float(summary_limits[key])),
            )
            
    return result


def add_summarized_transation(data):
    with open(file_name, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=HEADERS2)
        writer.writerows(data)


# PART 2: GUI Implementation (Functional)

def gui_add_transaction():
    try:
        global Total_balance
        Total_balance = float(total_balance_entry.get())
        description = desc_option.get()
        amount_val = amount_entry.get()

        if not amount_val:
            messagebox.showwarning("Input Error", "Please enter an amount.")
            return

        amount = float(amount_val)
        trans_type = "Income" if description == "Salary" else "Expense"
        date = datetime.datetime.today().replace(microsecond=0)

        data = {
            "date": date,
            "description": description,
            "amount": amount,
            "type": trans_type,
            "Total_balance": Total_balance,
        }

        add_transactions(data)
        messagebox.showinfo("Success", "Transaction saved successfully!")
        amount_entry.delete(0, "end")
        gui_view_data()
    except ValueError:
        messagebox.showerror("Error", "Enter a valid number (e.g., 10.50)")


def gui_view_data():
    output_box.delete("1.0", "end")
    data = get_transactions()
    if not data:
        output_box.insert("end", "No transactions found yet.")
        return

    expense, income = 0.0, 0.0
    header = f"{'Date':<20} {'Description':<20} {'Amount':<10} {'Type':<10} {'Net Balance'}\n"
    separator = "-" * 85 + "\n"
    output_box.insert("end", header + separator)

    for row in data:
        amt = float(row["amount"])
        if row["type"] == "Expense":
            expense += amt
        else:
            income += amt

        net = (float(row["Total_balance"]) + income) - expense
        line = f"{str(row['date']):<20} {row['description']:<20} ${amt:<10.2f} {row['type']:<10} ${net:.2f}\n"
        output_box.insert("end", line)


def gui_show_summary():
    initialize_file2()
    limits = {cat: v.get() for cat, v in limits_vars.items()}
    # Pass arguments in correct order
    summarization = summarize_data(*[limits[cat] for cat in categories])

    result = summarization

    output_box.delete("1.0", "end")
    output_box.insert("end", "=== DETAILED SUMMARY (Spent vs Limit) ===\n\n")
    output_box.insert(
        "end", f"{'Category':<25} | {'Spent':<12} | {'Limit':<12} | {'Status'}\n"
    )
    output_box.insert("end", "-" * 75 + "\n")

    for item in result:
        cat = item["description"]
        spent = float(item["amount"])
        limit = float(limits.get(cat, 0))
        status = "OK"
        if limit > 0 and spent > limit:
            status = "⚠️ EXCEEDED"

        line = f"{cat:<25} | ${spent:<11.2f} | ${limit:<11.2f} | {status}\n"
        output_box.insert("end", line)


def gui_show_chart():
    data = get_transactions()
    if not data:
        messagebox.showinfo("Info", "No data to display chart.")
        return

    expenses = {}
    for row in data:
        if row["type"] == "Expense":
            cat = row["description"]
            expenses[cat] = expenses.get(cat, 0) + float(row["amount"])

    if not expenses:
        messagebox.showinfo("Info", "No expenses found for chart.")
        return

    chart_win = ctk.CTkToplevel(app)
    chart_win.title("Expense Distribution")
    chart_win.geometry("500x500")
    chart_win.attributes("-topmost", True)

    fig, ax = plt.subplots(figsize=(5, 5), dpi=100)
    ax.pie(
        expenses.values(), labels=expenses.keys(), autopct="%1.1f%%", startangle=140
    )
    ax.set_title("Expenses by Category")

    canvas = FigureCanvasTkAgg(fig, master=chart_win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)


def gui_reset_data():
    if messagebox.askyesno(
        "Reset Confirmation",
        "Are you sure you want to DELETE ALL transactions? This cannot be undone.",
    ):

        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=HEADERS)
            writer.writeheader()
        if os.path.exists(file_name):
            with open(file_name, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=HEADERS2)
                writer.writeheader()

        output_box.delete("1.0", "end")
        output_box.insert("end", "All data has been reset.")
        messagebox.showinfo("Reset", "Data cleared successfully.")


def open_limits_window():
    limit_win = ctk.CTkToplevel(app)
    limit_win.title("Set Category Spending Limits")
    limit_win.geometry("400x550")
    limit_win.attributes("-topmost", True)

    ctk.CTkLabel(
        limit_win, text="Monthly Spending Limits", font=("Arial", 16, "bold")
    ).pack(pady=10)

    scroll_frame = ctk.CTkScrollableFrame(limit_win, width=350, height=400)
    scroll_frame.pack(pady=10, padx=10)

    for cat in categories:
        row = ctk.CTkFrame(scroll_frame, fg_color="transparent")
        row.pack(fill="x", pady=5)
        ctk.CTkLabel(row, text=cat, width=180, anchor="w").pack(side="left")
        ctk.CTkEntry(row, textvariable=limits_vars[cat], width=100).pack(
            side="right"
        )

    ctk.CTkButton(limit_win, text="Done", command=limit_win.destroy).pack(pady=10)


def main():
    global app, total_balance_entry, desc_option, amount_entry, output_box, limits_vars

    app = ctk.CTk()
    
    initialize_file()
    app.title("Personal Finance Tracker")
    app.geometry("850x850")
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("green")

    # Variables
    limits_vars = {cat: ctk.StringVar(value="0") for cat in categories}

    # Setup UI
    
    # Title
    label = ctk.CTkLabel(
        app, text="Personal Finance Tracker", font=("Arial", 28, "bold")
    )
    label.pack(pady=20)

    # Total Balance Input
    balance_frame = ctk.CTkFrame(app)
    balance_frame.pack(pady=10, padx=20, fill="x")

    ctk.CTkLabel(
        balance_frame, text="Starting Total Balance: $", font=("Arial", 14)
    ).pack(side="left", padx=10, pady=10)
    total_balance_entry = ctk.CTkEntry(balance_frame, width=150)
    total_balance_entry.insert(0, "0.0")
    total_balance_entry.pack(side="left", padx=10)

    # Add Transaction Section
    add_frame = ctk.CTkFrame(app)
    add_frame.pack(pady=10, padx=20, fill="x")

    ctk.CTkLabel(add_frame, text="Category:").grid(
        row=0, column=0, padx=10, pady=5, sticky="w"
    )
    desc_option = ctk.CTkOptionMenu(
        add_frame, values=categories, width=200
    )
    desc_option.grid(row=1, column=0, padx=10, pady=10)

    ctk.CTkLabel(add_frame, text="Amount ($):").grid(
        row=0, column=1, padx=10, pady=5, sticky="w"
    )
    amount_entry = ctk.CTkEntry(
        add_frame, placeholder_text="e.g. 50.0", width=150
    )
    amount_entry.grid(row=1, column=1, padx=10, pady=10)

    add_btn = ctk.CTkButton(
        add_frame,
        text="Add Transaction",
        command=gui_add_transaction,
        fg_color="#27ae60",
        hover_color="#219150",
    )
    add_btn.grid(row=1, column=2, padx=20, pady=10)

    # Control Buttons
    btn_frame = ctk.CTkFrame(app, fg_color="transparent")
    btn_frame.pack(pady=10, padx=20, fill="x")

    # Row 1 of buttons
    ctk.CTkButton(
        btn_frame, text="View History", command=gui_view_data
    ).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    ctk.CTkButton(
        btn_frame, text="Detailed Summary", command=gui_show_summary
    ).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
    ctk.CTkButton(
        btn_frame,
        text="Set Limits",
        command=open_limits_window,
        fg_color="#d35400",
    ).grid(row=0, column=2, padx=5, pady=5, sticky="ew")

    # Row 2 of buttons
    ctk.CTkButton(
        btn_frame,
        text="View Pie Chart ",
        command=gui_show_chart,
        fg_color="#3498db",
    ).grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    ctk.CTkButton(
        btn_frame,
        text="Reset All Data ",
        command=gui_reset_data,
        fg_color="#c0392b",
    ).grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

    btn_frame.grid_columnconfigure((0, 1, 2), weight=1)

    # Output Display
    output_box = ctk.CTkTextbox(
        app, width=750, height=300, font=("Courier New", 12)
    )
    output_box.pack(pady=20, padx=20, fill="both", expand=True)

    app.mainloop()


if __name__ == "__main__":
    main()