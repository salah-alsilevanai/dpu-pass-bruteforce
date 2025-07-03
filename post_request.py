import requests
import json
from datetime import datetime

def get_payload():
    # Payload data directly in the code
    return {
        'phone_no': '07501234567',
        'password': '34567009',
        'g-recaptcha-response': '',
        'submit': '',
        'token': ''
    }

def get_headers():
    # Headers directly in the code
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

def send_post_request():
    url = "https://apps.dpu.edu.krd/student_portal/"
    
    try:
        response = requests.post(url, data=get_payload(), headers=get_headers())
        print(f"Status Code: {response.status_code}")
        
        # Quick preview of response
        print("Response preview:", response.text[:200].replace("\n", " "), "...\n")
        
        # Only save if login page is NOT present
        if "DPU Student Portal - Login" not in response.text:
            # Generate filename with timestamp and credentials
            payload = get_payload()
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{payload['phone_no']}_{payload['password']}_{timestamp}.html"
            
            # Save response content to HTML file
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(response.text)
            print(f"[+] Login success (phrase not found). Response saved to {filename}")
        else:
            print("[-] Login failed (login form detected). Response not saved.")
            
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    send_post_request()
