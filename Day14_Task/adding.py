#5. Adding and Updating Columns 
'''A DataFrame: 
df = pd.DataFrame({ 
"Price": [100, 200, 300] 
}) 
Scenario: 
● Add a column Discount = 10% of Price 
● Add another column Final Price = Price - Discount
'''
import pandas as pd

df = pd.DataFrame({ 
"price": [100, 200, 300] 
})

# Calculate Discount
df["Discount"] = df["price"] * 0.10

# Calculate final price
df["Final price"] = df["price"] - df["Discount"]

print(df)

