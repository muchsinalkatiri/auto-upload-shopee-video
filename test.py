variable_name = input("Enter the variable name: ")
variable_value = input("Enter the variable value: ")

# Create a variable with the provided name and value
globals()[variable_name] = variable_value

print(f"Created variable '{variable_name}' with value '{variable_value}'")