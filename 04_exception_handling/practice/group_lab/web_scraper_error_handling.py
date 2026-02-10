"""Team Lab Work: Build a Web Scraper Using Requests"""
import requests

while True: # Loop to allow multiple attempts
    # Program should prompt user for a URL
    url = input("Enter a URL: ").strip()
    # Ensure the URL starts with http:// or https://
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Make a GET request to the URL with error handling
    try:
        response = requests.get(url, timeout=10, allow_redirects=True)
        response.raise_for_status()

        print("Web page content:")
        print(response.text)

    except requests.exceptions.SSLError:
        print("SSL error occurred. Please check the URL and try again.")

    except requests.exceptions.Timeout:
        print("The request timed out. Please try again later.")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")

    except requests.exceptions.ConnectionError:
        print("Connection error occurred. Please check your internet connection and the URL.")

    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")

# Example outputs:

# Enter a URL: https://www.google.com
# Displays the HTML content of Google's homepage

# Enter a URL: www.google.com
# Same as above, prepends https://

# Enter a URL: google.com
# Same as above, prepends https://

# Enter a URL: google
# Connection error occurred. Please check your internet connection and the URL.

# SSL error example
# Enter a URL: https://expired.badssl.com/
# SSL error occurred. Please check the URL and try again.

# Timeout error example
# Enter a URL: https://httpbin.org/delay/15
# The request timed out. Please try again later.

# HTTP error example
# Enter a URL: https://httpbin.org/status/404
# HTTP error occurred: 404 Client Error: NOT FOUND for url: https://httpbin.org/status/404

# Connection error example
# Enter a URL: https://thiswebsitedoesnotexist123456.com
# Connection error occurred. Please check your internet connection and the URL.

# Invalid URL example
# Enter a URL: http://
# Request error occurred: Invalid URL 'http://': No host supplied
