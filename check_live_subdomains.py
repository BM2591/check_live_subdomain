import requests
import csv
import concurrent.futures
import time

def check_subdomain(subdomain, max_retries=3, timeout=5):
    session = requests.Session()
    live = False
    status_code = None
    url_used = ""

    for scheme in ['http', 'https']:
        url = f"{scheme}://{subdomain}"
        retries = 0

        while retries < max_retries:
            try:
                response = session.head(url, timeout=timeout, allow_redirects=True)
                status_code = response.status_code
                if status_code < 400:
                    live = True
                    url_used = url
                    return {"Subdomain": subdomain, "Status": "Live", "URL": url_used, "StatusCode": status_code}
                else:
                    break  # If 4xx or 5xx, no retry on that scheme
            except requests.exceptions.RequestException:
                retries += 1
                time.sleep(1)  # Wait 1 sec before retrying

    # If none succeeded
    return {"Subdomain": subdomain, "Status": "Not Live", "URL": "", "StatusCode": status_code if status_code else "N/A"}

def check_subdomains_concurrent(input_file, output_file, max_workers=10):
    with open(input_file, 'r') as file:
        subdomains = [line.strip() for line in file if line.strip()]

    print(f"Checking {len(subdomains)} subdomains with up to {max_workers} concurrent workers...")

    results = []
    live_hosts = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_subdomain = {executor.submit(check_subdomain, sd): sd for sd in subdomains}
        for future in concurrent.futures.as_completed(future_to_subdomain):
            result = future.result()
            results.append(result)
            if result["Status"] == "Live":
                live_hosts += 1
                print(f"[LIVE] {result['Subdomain']} ({result['URL']}) Status Code: {result['StatusCode']}")
            else:
                print(f"[DOWN] {result['Subdomain']}")

    # Write results to CSV
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['Subdomain', 'Status', 'URL', 'StatusCode']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\nScan complete. Total live hosts: {live_hosts}")
    print(f"Results saved to {output_file}")

if __name__ == "__main__":
    input_file = "subdomains.txt"
    output_file = "results.csv"
    check_subdomains_concurrent(input_file, output_file)