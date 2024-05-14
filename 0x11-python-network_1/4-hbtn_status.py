#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("Usage: {} <URL>".format(sys.argv[0]))

    url = sys.argv[1]
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4XX and 5XX status codes
        print("Body response:")
        print("\t- type:", type(response.text))
        print("\t- content:", response.text)
    except requests.exceptions.HTTPError as err:
        print("HTTP Error:", err)
    except requests.exceptions.ConnectionError as err:
        print("Error Connecting:", err)
    except requests.exceptions.Timeout as err:
        print("Timeout Error:", err)
    except requests.exceptions.RequestException as err:
        print("Oops! Something went wrong:", err)
