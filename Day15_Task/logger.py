#7. Generator-based Log Reader 
'''Scenario: 
A large log file needs to be processed. 
Task: 
● Create a generator to read file line by line 
● Use loop to process logs 
● Use condition to filter errors 
● Count occurrences using a dictionary
'''
# Create sample log file
with open("log.txt", "w") as file:
    file.write("INFO: Application started\n")
    file.write("ERROR: File not found\n")
    file.write("INFO: User logged in\n")
    file.write("ERROR: Database connection failed\n")
    file.write("WARNING: Low memory\n")
    file.write("ERROR: File not found\n")

# Generator function
def read_logs(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()

# Dictionary to count errors
error_count = {}

print("Error Logs:")

# Process logs using loop
for log in read_logs("log.txt"):

    if "ERROR" in log:
        print(log)

        error_type = log.split(":")[1].strip()

        if error_type in error_count:
            error_count[error_type] += 1
        else:
            error_count[error_type] = 1

# Display error count
print("\nError Count:")

for error, count in error_count.items():
    print(error, ":", count)
