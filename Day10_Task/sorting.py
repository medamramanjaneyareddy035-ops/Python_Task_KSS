#3. Sorting Product Prices 
'''An e-commerce company stores product prices in a NumPy array. 
Scenario: 
Prices = [499, 299, 799, 199, 599] 
Task: 
● Convert it into a NumPy array. 
● Sort the prices in ascending order.
'''
import numpy as np

# original prices
prices = [499, 299, 799, 199, 599]

#convert list into Numpy array
arr = np.array(prices)

#sort pricesin ascending order
sorted_prices = np.sort(arr)

#print output

print("Original marks:", arr)
print("sorted prices:", sorted_prices)
