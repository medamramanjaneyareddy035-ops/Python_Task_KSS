#3. Expense Distribution Pie Chart 
'''Scenario: 
Monthly expenses: 
expenses = np.array([500, 300, 200]) 
labels = ["Food", "Rent", "Travel"] 
Task: 
● Create a pie chart 
● Show percentage distribution
'''
import numpy as np
import matplotlib.pyplot as plt

# Monthly expenses
expenses = np.array([500, 300, 200])

# Expense labels
labels = ["Food", "Rent", "Travel"]

# Calculate total expenses
total = np.sum(expenses)

print("Total Monthly Expenses:", total)

# Create pie chart
plt.pie(
    expenses,
    labels=labels,
    autopct="%1.1f%%",
    startangle=90
)

# Add title
plt.title("Monthly Expense Distribution")

# Display chart
plt.show()
