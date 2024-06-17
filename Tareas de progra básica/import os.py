import os 
import requests

def get_secret_message():
    url = os.environ["url"]
    response = requests
    print(f"El cifrado es: {response.text}")

if __name__ == "__main__":
    get_secret_message