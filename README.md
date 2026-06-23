# Password Generator & Strength Checker

A simple Python project that can generate random passwords and check their strength based on different security criteria.

## Features

### Password Generator
- Generate random passwords of any length
- Includes:
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Numbers (0-9)
  - Special symbols (!, @, #, etc.)
- Input validation for password length

### Password Strength Checker
Checks whether a password contains:
- Uppercase letters
- Lowercase letters
- Numbers
- Special symbols
- Minimum length requirement (8+ characters)

Based on these factors, the password is classified as:
- Weak
- Medium
- Strong

## Technologies Used

- Python
- Random Module
- String Module

## How to Run

```bash
python password_generator.py
```

## Menu

```text
Welcome to Password Generator

Generate Password    - Click 1
Strength Checker     - Click 2
Exit                 - Click 3
```

## Example

### Generate Password

```text
Enter Length:- 12

Generated Password:
A@7xK#2pQ!9m
```

### Check Password Strength

```text
Enter your password:- Hello@123

Uppercase yes
Lowercase yes
Numbers yes
Special symbol yes
Length is perfect

Strong
```

## Concepts Practiced

- Functions
- Loops
- Conditional Statements
- String Handling
- Exception Handling
- Random Number Generation
- Input Validation
- Password Strength Analysis

## Future Improvements

- Copy password to clipboard
- Save generated passwords
- Multiple strength levels
- Custom password rules
- GUI version using Tkinter

## Author

Daksh kaushik
B.Tech CSE (AI/ML)
First year
