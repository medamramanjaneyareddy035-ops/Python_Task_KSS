#4. Basic File Logger 
'''Scenario: 
A system logs user actions. 
Task: 
● Take user input 
● Store logs in a file 
● Use loop to allow multiple entries 
● Handle file errors using exception handling
'''
# Basic File Logger

try:
    with open("user_logs.txt", "a") as file:

        while True:
            log = input("Enter user activity (type exit to stop): ")

            if log.lower() == "exit":
                break

            file.write(log + "\n")

    print("Logs saved successfully!")

except OSError as e:
    print("File Error:", e)

except Exception as e:
    print("Error:", e)
