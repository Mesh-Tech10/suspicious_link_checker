import requests
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("VT_API_KEY")
domain = "goog1e-secure-login.com"
headers = {"x-apikey": key}
r = requests.get(f"https://www.virustotal.com/api/v3/domains/{domain}", headers=headers)
print(r.status_code)
print(r.json())
