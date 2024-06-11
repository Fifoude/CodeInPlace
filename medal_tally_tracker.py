
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
