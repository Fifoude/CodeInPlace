
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
import pandas as pd             # pandas 2.2.2 to work with datas https://pandas.pydata.org/pandas-docs/stable/getting_started/index.html
import tkinter as tk
from tkinter import messagebox, ttk  # https://docs.python.org/3/library/tkinter.messagebox.html

def read_medal_data(csv_file):      # read CSV file and manage errors
    try:
        data = pd.read_csv(csv_file)
        return data
    except Exception as e:
        print("Error reading CSV file: {e}")
        return None

'''
# Read and print the medal dat
medal_data = read_medal_data('medal_data.csv')
print(medal_data)
'''

# Function to display data in a treeview
def display_data():
    # Clear existing data in treeview
    for i in treeview.get_children():
        treeview.delete(i)

    # Read data from CSV
    medal_data = read_medal_data('medal_data.csv')
    
    # Insert data into treeview
    for index, row in medal_data.iterrows():
        treeview.insert("", "end", values=(row['Country'], row['Gold'], row['Silver'], row['Bronze']))




# Initialize the main window
root = tk.Tk()
root.title("Medal Tally Tracker")
root.geometry("600x400")

# Create treeview for displaying data
columns = ("Country", "Gold", "Silver", "Bronze")
treeview = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    treeview.heading(col, text=col)
    treeview.grid(row=6, column=0, columnspan=2)


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

    # Validate inputs
    if not country or not gold or not silver or not bronze:
        messagebox.showerror("Error", "All fields are required")
        return
    if not gold.isdigit() or not silver.isdigit() or not bronze.isdigit():
        messagebox.showerror("Error", "Medal counts must be non-negative integers")
        return
    # Append data to CSV
    with open('medal_data.csv', 'a') as f:
        f.write(f"\n{country},{gold},{silver},{bronze}")
    messagebox.showinfo("Info", f"Data submitted for {country}")
    display_data()


# Button to submit data
submit_button = tk.Button(root, text="Submit Data", command=submit_data)
submit_button.grid(row=4, column=0, columnspan=2, pady=20)

'''
# Function to display data (to be implemented later)
def display_data():
    # Implement data display logic here
    pass
'''

# Button to display data
display_button = tk.Button(root, text="Display Medal Tally", command=display_data)
display_button.grid(row=5, column=0, columnspan=2, pady=10)

# Initial call to display data
display_data()

# Run the Tkinter event loop
root.mainloop()
