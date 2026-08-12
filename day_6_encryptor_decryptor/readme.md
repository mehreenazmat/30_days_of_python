# Day 6 – Encryption and Decryption of Messages

**30 Days of Python Challenge**

## Project Description

This project is a **console-based Secure Message Locker** developed as part of my **30 Days of Python Challenge**.

The program allows users to encrypt messages using the **Caesar Cipher algorithm**, decrypt the most recently encrypted message, save encrypted messages, delete saved messages, and recover deleted messages through a backup system.

## Features

* Encrypt messages using the Caesar Cipher
* Decrypt the most recently encrypted message
* Choose a custom shift value
* Generate a random shift automatically
* Save encrypted messages
* View all saved messages
* Delete saved messages
* Recover deleted messages from backup
* Display system information and help
* Validate shift values between 1 and 25
* Keep spaces, numbers, and symbols unchanged

## Concepts Used

* Python Functions
* Lists
* `for` Loops
* `while` Loops
* `if-elif-else` Conditions
* Global Variables
* String Manipulation
* ASCII / Unicode values using `ord()` and `chr()`
* `random` Module
* Exception Handling
* `try-except`
* `ValueError`
* Caesar Cipher Algorithm

## How Encryption Works

The program uses the **Caesar Cipher** technique.

Each alphabetic character is shifted by a selected number of positions in the alphabet.

For example, with a shift of `3`:

```text
HELLO → KHOOR
```

The same shift can then be used to decrypt the encrypted message.

Numbers, spaces, and special characters remain unchanged.

## How to Run

Make sure Python 3.x is installed on your system.

Run the program using:

```bash
python encryption_decryption.py
```

## Learning Outcome

Through this project, I practiced implementing an encryption algorithm using Python and learned how to work with character encoding, string manipulation, lists, functions, random values, and exception handling.

This project also helped me understand how different Python concepts can be combined to create a more feature-rich console application.

## Author

**Mehreen**

**Day 6 of 30 Days of Python Challenge**
