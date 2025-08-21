from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("VT_API_KEY")
print("VirusTotal API Key:", key)
