# Brute Force

This repository contains a brute force program designed to test combinations of phone numbers for DPU student accounts. The program targets the site:

https://apps.dpu.edu.krd/student_portal/

The program works as follows:

- It uses the last 5 digits of a student's phone number as a base.
- It brute-forces the remaining 3 digits, generating all possible combinations (000-999).
- For each combination, it sends a request to the correct API endpoint, resulting in 999 attempts per student.

## Files

- `attack1.py`, `attack2.py`, `attack3.py`, `attack4.py`, `attack4_multi.py`, `attack4_multi_lean.py`: Different brute force attack scripts.
- `generate_passwords.py`: Generates possible password combinations.
- `generated_passwords.txt`: Stores generated passwords.
- `post_request.py`: Handles sending requests to the API endpoint.
- `RESULTS_*.CSV`: Stores results of brute force attempts.
- `TARGET_NUMBERS.txt`, `target_numbersssss.txt`: Lists of target phone numbers.

## Attack Scripts Overview

### attack1.py

Single-threaded brute force for a single phone number. Reads passwords from `generated_passwords.txt` and tries each one sequentially. Use for simple, slow testing or debugging.

**How to use:**

1. Generate passwords using `generate_passwords.py` (edit the phone number in that script).
2. Run `attack1.py` (edit the phone number in the script).

### attack2.py

Multi-threaded brute force for a single phone number. Uses threads to speed up attempts. Reads passwords from `generated_passwords.txt`.

**How to use:**

1. Generate passwords using `generate_passwords.py`.
2. Run `attack2.py` (edit the phone number in the script).

### attack3.py

Multi-threaded brute force for a single phone number, with improved status output. Reads passwords from `generated_passwords.txt`.

**How to use:**

1. Generate passwords using `generate_passwords.py`.
2. Run `attack3.py` (edit the phone number in the script).

### attack4.py

Multi-threaded brute force for a single phone number. Generates passwords on the fly based on the last 5 digits of the phone number. Results are saved as HTML files for successful attempts.

**How to use:**

1. Edit `TARGET_PHONE_NUMBER` in `attack4.py`.
2. Run `attack4.py`.

### attack4_multi.py

Multi-threaded brute force for multiple phone numbers. Reads numbers from `TARGET_NUMBERS.txt` and generates passwords for each. Results are saved in a CSV file for each day.

**How to use:**

1. Add phone numbers (one per line) to `TARGET_NUMBERS.txt`.
2. Run `attack4_multi.py`.

### attack4_multi_lean.py

Optimized multi-threaded brute force for multiple phone numbers. Stops further attempts for a number once a working password is found. Reads numbers from `TARGET_NUMBERS.txt` and saves results in a CSV file.

**How to use:**

1. Add phone numbers (one per line) to `TARGET_NUMBERS.txt`.
2. Run `attack4_multi_lean.py`.

## Usage

1. Place the target phone numbers in `TARGET_NUMBERS.txt` (one per line).
2. Run the desired attack script as described above.
3. Results will be saved in the corresponding CSV or HTML files.

**Note:** This tool is for educational and authorized testing purposes only. Unauthorized use is strictly prohibited.
