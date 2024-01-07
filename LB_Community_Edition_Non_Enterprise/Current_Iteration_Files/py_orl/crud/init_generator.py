import os
import re

# Define the path to the CRUD directory
crud_directory = 'C:\\Users\\Shawn\\Desktop\\Hepheastus_Project\\learning-blocks\\Learning-Blocks-No-Docker-Version\\py_orl\\crud'

# Regex pattern to identify CRUD class variable names in each file
crud_class_pattern = r'crud_\w+'

# A list to store the import statements
import_statements = []

# Iterate through all files in the CRUD directory
for filename in os.listdir(crud_directory):
    if filename.endswith('.py') and not filename.startswith('__'):
        with open(os.path.join(crud_directory, filename), 'r') as file:
            content = file.read()
            # Find all CRUD class variable names in the file
            crud_classes = re.findall(crud_class_pattern, content)
            for crud_class in crud_classes:
                # Generate import statement for each CRUD class
                import_statements.append(f'from crud.{filename[:-3]} import {crud_class}')

# Print the import statements
for statement in sorted(set(import_statements)):
    print(statement)

print("CRUD class imports generated.")
