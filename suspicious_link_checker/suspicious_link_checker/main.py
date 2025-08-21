# filepath: c:\Users\meshw\Desktop\My-Projects\06-suspicious_link_checker\suspicious_link_checker\main.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("VT_API_KEY")

def check_link(domain):
    headers = {"x-apikey": key}
    response = requests.get(f"https://www.virustotal.com/api/v3/domains/{domain}", headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Unable to check the link", "status_code": response.status_code}

if __name__ == "__main__":
    domain_to_check = input("Enter the domain to check: ")
    result = check_link(domain_to_check)
    print(result)