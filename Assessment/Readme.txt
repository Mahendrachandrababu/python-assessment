Bulk Email Sending Using Zoho Mail API
Overview
This script allows you to send bulk emails using the Zoho Mail API. You can customize the subjects and messages for each recipient by providing the details in a CSV file.

Requirements
Python 3.x
requests library
Setup
Install Dependencies: If you haven't already, install the requests library using pip:


pip install requests
Obtain Zoho Mail API Key: Replace 'your_zoho_api_key' in the script with your actual Zoho Mail API key.

Prepare CSV File: Create a CSV file named recipients.csv in the same directory as the script. The CSV file should have three columns: email, subject, and message, containing the details of recipients and their corresponding personalized subjects and messages.

Usage
Run the script by executing the following command in your terminal or command prompt:


python script_name.py
Replace script_name.py with the actual name of the Python script file.

The script will read the CSV file, send emails to each recipient using the Zoho Mail API, and print status messages indicating whether each email was successfully sent or if there was an error.

Notes
Ensure that your Zoho Mail API key is valid and that you have permissions to send emails from the specified Zoho account.
Make sure that the recipients' email addresses in the CSV file are correct and properly formatted.
