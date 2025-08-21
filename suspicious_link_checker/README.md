# Suspicious Link Checker

This project is a Python application designed to check the safety of URLs using the VirusTotal API. It allows users to verify whether a specific domain is flagged as suspicious or malicious.

## Project Structure

```
suspicious_link_checker
├── suspicious_link_checker
│   ├── __init__.py
│   ├── main.py
│   └── test.py
├── requirements.txt
├── .env
└── README.md
```

## Installation

1. Clone the repository to your local machine:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd suspicious_link_checker
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your VirusTotal API key:
   ```
   VT_API_KEY=your_api_key_here
   ```

## Usage

To check a domain, you can run the `test.py` script. Make sure to replace `goog1e-secure-login.com` with the domain you want to check in the `test.py` file.

Run the script:
```
python suspicious_link_checker/test.py
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.