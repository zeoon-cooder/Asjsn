import requests
import time

# Function to read tokens from datas.txt
def read_tokens(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Function to send clicks
def send_clicks(auth_token):
    url = 'https://crystalton.ru/api/clicks'
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {auth_token}',
        'User-Agent': 'Mozilla/5.0'
    }
    data = {"clicks": 100}
    response = requests.post(url, headers=headers, json=data)
    print(f"Clicks Response: {response.status_code} - {response.text}")

# Function to send ads
def send_ad(auth_token):
    url = 'https://crystalton.ru/api/ads'
    headers = {
        'Accept': 'application/json',
        'Authorization': f'Bearer {auth_token}',
        'User-Agent': 'Mozilla/5.0'
    }
    # Using GET method as POST is not supported
    response = requests.get(url, headers=headers)
    print(f"Ad Response: {response.status_code} - {response.text}")

# Main execution loop
def main():
    tokens = read_tokens("datas.txt")
    if not tokens:
        print("No tokens found in datas.txt")
        return

    while True:
        for token in tokens:
            print("Sending clicks...")
            send_clicks(token)
            time.sleep(2)

            print("Sending ad...")
            send_ad(token)
            time.sleep(2)

        # Optional delay between token cycles
        time.sleep(360)  # 6 minutes

if __name__ == "__main__":
    main()
