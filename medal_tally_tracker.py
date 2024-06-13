
#           Project title : Olympics Medal Tally Tracker

# Plan Milestones:
'''
M1: Understand the Project Requirements and Plan
================================================

Main Features:
    - Medal Table : Display the count of gold, silver, and bronze medals for each country.
    - Country Ranking : Rank countries based on the total number of medals.
    - Data Visualization : Create bar charts and pie charts to visualize medal distribution
    - Error Handling : Ensure robust input validation and display appropriate error messages.

Main Components:
    - Medal Table: Use Tkinter to create a table layout.
    - Country Ranking: Implement sorting logic for ranking countries.
    - Data Visualization: Use matplotlib for creating visualizations.
    - Error Handling: Implement input validation and error messages using Tkinter's messagebox.
'''
'''
M2: Set Up Your Project and Read CSV Data
=========================================
'''
# importing the necessary libraries for this project:
# import pandas as pd             # pandas 2.2.2 to work with datas https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html
import tkinter as tk
from tkinter import messagebox, ttk  # https://docs.python.org/3/library/tkinter.messagebox.html
import matplotlib.pyplot as plt
import csv


# Initialize the main window
root = tk.Tk()
root.title("Olympics Medal Tally Tracker")
root.geometry("800x600")

# Function to display the data
def display_data():
    for item in treeview.get_children():
        treeview.delete(item)
    with open('medal_data.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        data = [row for row in reader]
    
    # Sort the data based on the total medals, then gold, silver, and bronze
    data.sort(key=lambda x: (int(x[1]) + int(x[2]) + int(x[3]), int(x[1]), int(x[2]), int(x[3])), reverse=True)
    
    for row in data:
        treeview.insert("", "end", values=row)

# Function to create a medal chart
def create_medal_chart():
    countries = []
    gold_medals = []
    silver_medals = []
    bronze_medals = []
    with open('medal_data.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        for row in reader:
            countries.append(row[0])
            gold_medals.append(int(row[1]))
            silver_medals.append(int(row[2]))
            bronze_medals.append(int(row[3]))
    
    fig, ax = plt.subplots()
    bar_width = 0.25
    index = range(len(countries))
    
    ax.bar(index, gold_medals, bar_width, label='Gold')
    ax.bar([i + bar_width for i in index], silver_medals, bar_width, label='Silver')
    ax.bar([i + 2 * bar_width for i in index], bronze_medals, bar_width, label='Bronze')
    
    ax.set_xlabel('Countries')
    ax.set_ylabel('Medals Count')
    ax.set_title('Medal Distribution by Country')
    ax.set_xticks([i + bar_width for i in index])
    ax.set_xticklabels(countries, rotation=45, ha="right")
    ax.legend()
    
    plt.tight_layout()
    plt.show()

# Treeview for displaying the medal tally
columns = ("country", "gold", "silver", "bronze")
treeview = ttk.Treeview(root, columns=columns, show="headings")
treeview.heading("country", text="Country")
treeview.heading("gold", text="Gold")
treeview.heading("silver", text="Silver")
treeview.heading("bronze", text="Bronze")
treeview.grid(row=6, column=0, columnspan=2, sticky='nsew')

# Scrollbars for the treeview
treeview_scroll_y = ttk.Scrollbar(root, orient="vertical", command=treeview.yview)
treeview_scroll_y.grid(row=6, column=2, sticky='ns')
treeview.configure(yscrollcommand=treeview_scroll_y.set)

treeview_scroll_x = ttk.Scrollbar(root, orient="horizontal", command=treeview.xview)
treeview_scroll_x.grid(row=7, column=0, columnspan=2, sticky='ew')
treeview.configure(xscrollcommand=treeview_scroll_x.set)

# Entry and label for country name
country_label = tk.Label(root, text="Country:")
country_label.grid(row=0, column=0, padx=10, pady=10)
country_entry = tk.Entry(root)
country_entry.grid(row=0, column=1, padx=10, pady=10)

# Entry and label for gold medals
gold_label = tk.Label(root, text="Gold Medals:")
gold_label.grid(row=1, column=0, padx=10, pady=10)
gold_entry = tk.Entry(root)
gold_entry.grid(row=1, column=1, padx=10, pady=10)

# Entry and label for silver medals
silver_label = tk.Label(root, text="Silver Medals:")
silver_label.grid(row=2, column=0, padx=10, pady=10)
silver_entry = tk.Entry(root)
silver_entry.grid(row=2, column=1, padx=10, pady=10)

# Entry and label for bronze medals
bronze_label = tk.Label(root, text="Bronze Medals:")
bronze_label.grid(row=3, column=0, padx=10, pady=10)
bronze_entry = tk.Entry(root)
bronze_entry.grid(row=3, column=1, padx=10, pady=10)

# Function to submit data
def submit_data():
    country = country_entry.get()
    gold = gold_entry.get()
    silver = silver_entry.get()
    bronze = bronze_entry.get()
    if not country or not gold or not silver or not bronze:
        messagebox.showerror("Error", "All fields are required")
        return
    if not gold.isdigit() or not silver.isdigit() or not bronze.isdigit():
        messagebox.showerror("Error", "Medal counts must be non-negative integers")
        return

    with open('medal_data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([country, gold, silver, bronze])
    
    messagebox.showinfo("Info", f"Data submitted for {country}")
    country_entry.delete(0, tk.END)
    gold_entry.delete(0, tk.END)
    silver_entry.delete(0, tk.END)
    bronze_entry.delete(0, tk.END)
    update_country_menu()
    display_data()

# Create a dropdown menu for country selection
selected_country = tk.StringVar()
country_menu = ttk.Combobox(root, textvariable=selected_country)
country_menu.grid(row=6, column=0, columnspan=2, pady=10)

def update_country_menu():
    with open('medal_data.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        countries = [row[0] for row in reader]
    country_menu['values'] = countries

update_country_menu()

def load_entry_data():
    selected = selected_country.get()
    with open('medal_data.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header
        for row in reader:
            if row[0] == selected:
                country_entry.delete(0, tk.END)
                country_entry.insert(0, row[0])
                gold_entry.delete(0, tk.END)
                gold_entry.insert(0, row[1])
                silver_entry.delete(0, tk.END)
                silver_entry.insert(0, row[2])
                bronze_entry.delete(0, tk.END)
                bronze_entry.insert(0, row[3])
                break

load_button = tk.Button(root, text="Load Entry Data", command=load_entry_data)
load_button.grid(row=7, column=0, columnspan=2, pady=10)

def modify_entry():
    country = country_entry.get()
    gold = gold_entry.get()
    silver = silver_entry.get()
    bronze = bronze_entry.get()
    if not country or not gold or not silver or not bronze:
        messagebox.showerror("Error", "All fields are required")
        return
    if not gold.isdigit() or not silver.isdigit() or not bronze.isdigit():
        messagebox.showerror("Error", "Medal counts must be non-negative integers")
        return
    
    # Read the current data
    rows = []
    with open('medal_data.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    # Update the relevant row
    for i in range(1, len(rows)):  # Skip the header
        if rows[i][0] == country:
            rows[i] = [country, gold, silver, bronze]
            break
    
    # Write the updated data
    with open('medal_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    
    messagebox.showinfo("Info", f"Data modified for {country}")
    update_country_menu()
    display_data()

modify_button = tk.Button(root, text="Modify Entry", command=modify_entry)
modify_button.grid(row=8, column=0, columnspan=2, pady=10)

# Button to add data
submit_button = tk.Button(root, text="Submit Data", command=submit_data)
submit_button.grid(row=4, column=0, columnspan=2, pady=10)

# Button to display the medal tally
display_button = tk.Button(root, text="Display Medal Tally", command=display_data)
display_button.grid(row=5, column=0, columnspan=2, pady=10)

# Button to show medal chart
chart_button = tk.Button(root, text="Show Medal Chart", command=create_medal_chart)
chart_button.grid(row=6, column=1, columnspan=2, pady=10)

# Initial display of data
display_data()

# Run the main loop
root.mainloop()
