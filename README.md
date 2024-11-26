# Password Manager
## Description
A simple and secure Password Manager built with Python. This application helps you generate, store, and retrieve strong passwords for various websites. It features a user-friendly graphical interface powered by Tkinter, ensures ease of use, and supports JSON-based local storage for managing credentials.

---

## Features
* **Generate Strong Passwords**:
  * Automatically creates passwords with a mix of letters, numbers, and symbols.
  * Copies the generated password directly to your clipboard.

* **Save Credentials**:
  * Stores website credentials (website name, email/username, and password) in a local JSON file.
  * Allows updating credentials for existing websites.

* **Search for Saved Passwords**:
  * Quickly retrieve credentials by searching for a website name.
  * Displays the saved email/username and password in an easy-to-read format.

* User-Friendly Interface:
  * Built using Tkinter for a clean and interactive experience.

---

## Project Structure
```text
Password Manager
├── data.py                # Contains predefined lists of alphabets, numbers, and symbols.
├── password_generator.py  # Module for generating secure passwords.
├── password_manager.py    # Main script for managing the password manager's GUI and functionality.
├── logo.png               # Logo image displayed in the application (not included here).
└── passwords.json         # JSON file for storing credentials (auto-created).
```

---

## Setup Instructions
### Prerequisites
* Python 3.8 or higher installed on your system.
* Required Python libraries:
  * `pyperclip`
  * `tkinter` (comes pre-installed with Python on most systems)

### Installation
1. Clone this repository:
    ```commandline
    git https://github.com/shrabhay/Password-Manager.git
    cd password-manager
    ```

2. Install dependencies:
    ```commandline
    pip install pyperclip
    ```

3. Run the application:
    ```commandline
    python3 password_manager.py
    ```

---

## How to Use
### 1. Generate Passwords
* Enter the website name and your email/username in the respective fields.
* Click the "Generate Password" button to create a secure password.
* The password is automatically copied to your clipboard.

### 2. Save Passwords
* After generating a password, click the "Add" button.
* Confirm the details in the pop-up window to save your credentials.

### 3. Search for Passwords
* Enter the website name in the search field.
* Click the "Search" button to retrieve saved credentials for that website.
* If no credentials are found, you’ll be notified.

---

## File Details
### 1. `data.py`
Defines the character sets used for password generation:
* alphabets: Uppercase and lowercase letters.
* numbers: Numeric digits (0–9).
* symbols: Special characters like !, @, #, etc.

### 2. `password_generator.py`
Contains the `password_generator` function to:
* Randomly select letters, numbers, and symbols to create a secure password.
* Shuffle and return the password as a string.

### 3. `password_manager.py`
The main application file:
* Sets up the Tkinter-based GUI.
* Handles password generation, saving, and searching.
* Reads and writes data to the passwords.json file.

---

## Future Improvements
* Add encryption for `passwords.json` to enhance security.
* Implement multi-user support with authentication.
* Allow exporting credentials to a secure file format.
* Add an option to delete saved passwords.

---

## Screenshots
### Main Interface:
![img.png](img.png)

### Password Search:
# Password Manager
## Description
A simple and secure Password Manager built with Python. This application helps you generate, store, and retrieve strong passwords for various websites. It features a user-friendly graphical interface powered by Tkinter, ensures ease of use, and supports JSON-based local storage for managing credentials.

---

## Features
* **Generate Strong Passwords**:
  * Automatically creates passwords with a mix of letters, numbers, and symbols.
  * Copies the generated password directly to your clipboard.

* **Save Credentials**:
  * Stores website credentials (website name, email/username, and password) in a local JSON file.
  * Allows updating credentials for existing websites.

* **Search for Saved Passwords**:
  * Quickly retrieve credentials by searching for a website name.
  * Displays the saved email/username and password in an easy-to-read format.

* User-Friendly Interface:
  * Built using Tkinter for a clean and interactive experience.

---

## Project Structure
```text
Password Manager
├── data.py                # Contains predefined lists of alphabets, numbers, and symbols.
├── password_generator.py  # Module for generating secure passwords.
├── password_manager.py    # Main script for managing the password manager's GUI and functionality.
├── logo.png               # Logo image displayed in the application (not included here).
└── passwords.json         # JSON file for storing credentials (auto-created).
```

---

## Setup Instructions
### Prerequisites
* Python 3.8 or higher installed on your system.
* Required Python libraries:
  * `pyperclip`
  * `tkinter` (comes pre-installed with Python on most systems)

### Installation
1. Clone this repository:
    ```commandline
    git https://github.com/shrabhay/Password-Manager.git
    cd password-manager
    ```

2. Install dependencies:
    ```commandline
    pip install pyperclip
    ```

3. Run the application:
    ```commandline
    python3 password_manager.py
    ```

---

## How to Use
### 1. Generate Passwords
* Enter the website name and your email/username in the respective fields.
* Click the "Generate Password" button to create a secure password.
* The password is automatically copied to your clipboard.

### 2. Save Passwords
* After generating a password, click the "Add" button.
* Confirm the details in the pop-up window to save your credentials.

### 3. Search for Passwords
* Enter the website name in the search field.
* Click the "Search" button to retrieve saved credentials for that website.
* If no credentials are found, you’ll be notified.

---

## File Details
### 1. `data.py`
Defines the character sets used for password generation:
* alphabets: Uppercase and lowercase letters.
* numbers: Numeric digits (0–9).
* symbols: Special characters like !, @, #, etc.

### 2. `password_generator.py`
Contains the `password_generator` function to:
* Randomly select letters, numbers, and symbols to create a secure password.
* Shuffle and return the password as a string.

### 3. `password_manager.py`
The main application file:
* Sets up the Tkinter-based GUI.
* Handles password generation, saving, and searching.
* Reads and writes data to the passwords.json file.

---

## Future Improvements
* Add encryption for `passwords.json` to enhance security.
* Implement multi-user support with authentication.
* Allow exporting credentials to a secure file format.
* Add an option to delete saved passwords.

---

## Screenshots
### Main Interface:
![img.png](img.png)

### Password Search:
![img_1.png](img_1.png)

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing
Contributions are welcome! If you have ideas or improvements, feel free to open an issue or submit a pull request.



---

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing
Contributions are welcome! If you have ideas or improvements, feel free to open an issue or submit a pull request.

