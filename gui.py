import tkinter as tk
from tkinter import messagebox
from dotenv import load_dotenv

from main import analyze_url

def run_gui():
    load_dotenv()
    root = tk.Tk()
    root.title("Suspicious Link Checker")

    tk.Label(root, text="Enter URL:").pack(padx=10, pady=6)
    url_entry = tk.Entry(root, width=60)
    url_entry.pack(padx=10, pady=6)

    def check_link():
        url = url_entry.get().strip()
        if not url:
            messagebox.showwarning("Input required", "Please enter a URL.")
            return
        status, score, details = analyze_url(url, vt_enabled=True)
        vt = details.get("vt", {})
        vt_points = vt.get("penalty", vt.get("points", 0))
        vt_status = "N/A" if not vt.get("enabled") else f"Malicious: {vt.get('malicious',0)}, Suspicious: {vt.get('suspicious',0)}"

        msg = (
            f"Status: {status}\n"
            f"Score: {score}\n"
            f"Domain: {details.get('domain','')}\n"
            f"VT Points: {vt_points} ({vt_status})"
        )
        messagebox.showinfo("Result", msg)

    tk.Button(root, text="Check Link", command=check_link).pack(padx=10, pady=10)
    root.mainloop()

if __name__ == "__main__":
    run_gui()
