#14. Splitting Student Scores Across Servers 
'''A dataset: 
[50, 60, 70, 80, 90, 100, 110, 120] 
Scenario: 
A distributed system needs to divide this data among 4 servers. 
Task: 
● Convert to NumPy array. 
● Split the array into 4 equal parts using array_split().
'''
import numpy as np

# Student scores
scores = np.array([50, 60, 70, 80, 90, 100, 110, 120])

# Split the array into 4 equal parts
server_data = np.array_split(scores, 4)

# Display the data assigned to each server
for i, data in enumerate(server_data):
    print(f"Server {i+1}:", data)
