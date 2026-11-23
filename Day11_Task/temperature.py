#11. Filter High Temperature Values 
'''A weather station records temperatures: 
[28, 31, 35, 27, 40, 22] 
Scenario: 
The system needs temperatures above 30°C. 
Task: 
● Filter the values greater than 30 using NumPy boolean filtering.
'''
import numpy as np

# Temperature values
temperatures = np.array([28, 31, 35, 27, 40, 22])

# Filter temperatures greater than 30°C
high_temperatures = temperatures[temperatures > 30]

# Display the result
print("Temperatures above 30°C:", high_temperatures)
