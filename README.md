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

Install dependencies with:

```bash
pip install requests
```

## Usage

1. Prepare a text file containing a list of subdomains (one per line), e.g., `subdomains.txt`.

2. Run the script:

```bash
python check_subdomains.py
```

3. Results will be saved in `results.csv` with the following columns:

- **Subdomain** — the subdomain tested  
- **Status** — `Live` or `Not Live`  
- **URL** — working URL if live (http or https)  
- **StatusCode** — HTTP response status code or `N/A`

## Customize

- Change the input/output file names by modifying the variables inside the script.  
- Adjust concurrency by changing `max_workers` in the script’s `ThreadPoolExecutor`.  
- Modify retry count or timeout inside the `check_subdomain` function parameters.

## Example

Run the script:

```bash
python check_subdomains.py
```

Sample output in `results.csv`:

| Subdomain         | Status   | URL                | StatusCode |
|-------------------|----------|--------------------|------------|
| example.com       | Live     | https://example.com | 200        |
| test.example.com  | Not Live |                    | N/A        |

## License

MIT License © 2025 BM2591

Permission is hereby granted, free of charge, to any person obtaining a copy  
of this software and associated documentation files (the "Software"), to deal  
in the Software without restriction, including without limitation the rights  
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell  
copies of the Software, and to permit persons to whom the Software is  
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all  
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,  
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE  
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,  
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE  
SOFTWARE.
