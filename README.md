# AirBnB Clone - Command Interpreter

## Project Description

The AirBnB Clone project is an ambitious endeavor to create a web application that emulates the functionality of the popular platform Airbnb. The project aims to develop a full-fledged AirBnB clone with features like property listings, user accounts, booking management, and more. The Command Interpreter is a fundamental part of this project, providing a command-line interface for managing AirBnB objects, such as users, states, cities, places, and more.

## Command Interpreter

The Command Interpreter is designed to facilitate the management of AirBnB objects within the project. It provides the following functionalities:

- **Create**: Allows you to create new objects of different types, such as User, State, City, Place, and more.

- **Retrieve**: Enables you to retrieve objects from a file or database. You can retrieve all objects of a specific type or a single object by its ID.

- **Update**: Allows you to update attributes of existing objects. You can modify attributes like name, description, or any other relevant information.

- **Delete**: Provides the capability to delete objects by specifying their type and ID.

### How to Start It

To start the AirBnB Clone Command Interpreter, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Andenga/AirBnB-Clone.git
   ```

2. Navigate to the project directory:

   ```bash
   cd AirBnB-Clone
   ```

3. Start the command interpreter:

   ```bash
   ./console.py
   ```

### How to Use It

The Command Interpreter operates in both interactive and non-interactive modes.

- **Interactive Mode**: In this mode, you will be presented with a prompt, `(hbnb)`, where you can enter commands and receive immediate responses.

- **Non-Interactive Mode**: You can also use the command interpreter to execute commands from a file or script. For example, you can run a list of commands from a text file.

### Examples

#### Interactive Mode

Here are some examples of commands you can use in the interactive mode:

- Create a new user:

  ```bash
  (hbnb) create User
  ```

- Retrieve all objects of a specific type (e.g., User):

  ```bash
  (hbnb) all User
  ```

- Update an attribute of an object:

  ```bash
  (hbnb) update User 12345 first_name "John"
  ```

- Delete an object:

  ```bash
  (hbnb) destroy User 12345
  ```

#### Non-Interactive Mode

You can also use the Command Interpreter in non-interactive mode by providing commands in a file. For example, you can run a list of commands stored in a text file:

```bash
echo "create User" | ./console.py
```

## Authors

This project is a made by me Lydia Andenga