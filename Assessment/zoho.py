# Example script to send bulk emails using Zoho Mail API

import requests
import csv

# Function to read recipients and messages from CSV file
def read_csv(file_path):
    recipients = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            recipients.append({'email': row[0], 'subject': row[1], 'message': row[2]})
    return recipients

# Function to send email using Zoho Mail API
def send_email(api_key, recipient):
    url = 'https://mail.zoho.com/api/accounts/{your_account_id}/messages'
    headers = {'Authorization': 'Zoho-authtoken ' + api_key}
    data = {
        'toAddress': recipient['email'],
        'subject': recipient['subject'],
        'content': recipient['message']
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Email sent to {recipient['email']}")
    else:
        print(f"Failed to send email to {recipient['email']}. Error: {response.text}")

# Main function
def main():
    api_key = 'your_zoho_api_key'
    input_file = 'recipients.csv'
    recipients = read_csv(input_file)
    for recipient in recipients:
        send_email(api_key, recipient)

if __name__ == "__main__":
    main()
