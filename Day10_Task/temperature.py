#2. Temperature Monitoring System 
'''A weather station records temperatures for two days. 
Scenario: 
Day 1: [30, 32, 31] 
Day 2: [29, 33, 34] 
Task: 
● Create a 2D NumPy array to store this data. 
● Print the array. 
● Find the total temperature recorded.
'''
import numpy as np

#temparature data
day1 = [20, 30, 25]
day2 = [32, 35, 30]

#Create 2D numpy array
temp = np.array([day1, day2])

#print array
print("Temperature Array:")
print(temp)

# Find total temperature
total = np.sum(temp)

print("Total Temperature:",total)
