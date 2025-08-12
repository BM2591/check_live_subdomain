# Subdomain Checker

A Python script to check if subdomains are live by sending HTTP HEAD requests concurrently with retries and logging HTTP status codes.

## Features

- Checks both HTTP and HTTPS for each subdomain  
- Uses concurrency for faster scanning  
- Retries on intermittent failures  
- Logs HTTP status codes for better insight  
- Saves results to a CSV file  

## Requirements

- Python 3.6+  
- `requests` library  
- Optional: Install dependencies with  
  ```bash
  pip install requests
