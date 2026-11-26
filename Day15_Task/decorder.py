#8. Decorator-based Access Control 
'''Scenario: 
Restrict access to certain functions. 
Task: 
● Create a decorator to check user role 
● Use condition inside decorator 
● Apply decorator to multiple functions 
● Store roles in a dictionary
'''
# Store user roles in dictionary
users = {
    "Ram": "admin",
    "Ravi": "user",
    "Sita": "manager"
}

# Current logged-in user
current_user = "Ram"

# Create decorator
def check_role(required_role):

    def decorator(func):

        def wrapper(*args, **kwargs):

            user_role = users.get(current_user)

            if user_role == required_role or user_role == "admin":
                print("Access Granted")
                return func(*args, **kwargs)

            else:
                print("Access Denied! Permission required.")

        return wrapper

    return decorator


# Apply decorator to functions
@check_role("admin")
def delete_employee():
    print("Employee deleted successfully")


@check_role("manager")
def view_employee():
    print("Employee details displayed")


@check_role("manager")
def update_salary():
    print("Salary updated successfully")


# Call functions
delete_employee()
view_employee()
update_salary()
