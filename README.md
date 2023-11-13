# AirBnB_clone
This is a documentation for a project that runs on Ubuntu 14.04 LTS using python3.

Installation
To install this project, follow these steps:
- Clone this repository from GitHub: git clone "git@github.com:Alphonse16/AirBnB_clone.git"
- Change to the AirBnb directory: cd AirBnB_clone
- Run the console in interactive mode: ./console and enter command
- Run the console in non-interactive mode: echo "<command>" | ./console.py

File Descriptions
console.py - This file contains the command interpreter for the project. It supports the following commands:

EOF - exits the console
quit - exits the console
<emptyline> - does nothing
create - Creates a new instance of BaseModel, saves it to the JSON file and prints the id
destroy - Deletes an instance based on the class name and id (save the change to the JSON file).
show - Prints the string representation of an instance based on the class name and id.
all - Prints all string representations of all instances based or not on the class name.
update - Updates an instance based on the class name and id by adding or updating attribute (save the change to the JSON file).
models/ directory contains the classes for the project:
base_model.py - This file defines the BaseModel class, which is the base class for all other classes.

def __init__(self, *args, **kwargs) - Initializes a new instance of BaseModel
def __str__(self) - Returns a string representation of the BaseModel instance
def save(self) - Updates the updated_at attribute with the current datetime
def to_dict(self) - Returns a dictionary containing all keys/values of the instance
