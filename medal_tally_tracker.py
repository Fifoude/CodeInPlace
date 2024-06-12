
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
import pandas as pd
import tkinter as tk
from tkinter import messagebox

def read_medal_data(file):
    try:
        data = pd.read_csv(file)
        return data
    except Exception as e:
        print("Error reading CSV file: {e}")
        return None



# Read and print the medal dat
medal_data = read_medal_data('medal_data.csv')
print(medal_data)





# Initialize the main window
root = tk.Tk()
root.title("Medal Tally Tracker")
root.geometry("600x400")

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
    # Add validation and data processing here
    messagebox.showinfo("Info", f"Data submitted for {country}")

# Button to submit data
submit_button = tk.Button(root, text="Submit Data", command=submit_data)
submit_button.grid(row=4, column=0, columnspan=2, pady=20)

# Function to display data (to be implemented later)
def display_data():
    # Implement data display logic here
    pass

# Button to display data
display_button = tk.Button(root, text="Display Medal Tally", command=display_data)
display_button.grid(row=5, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
