import csv
import requests

endpoint = 'http://127.0.0.1:8000/api/device/'

response = requests.get(endpoint)
if response.status_code == 200:
    data = response.json()
    csv_data = [['Name', 'Description', 'Is Active']]  # Header row

    for entry in data:
        row = [entry['name'], entry['description'], entry['is_active']]
        csv_data.append(row)

    with open('get_device.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
    print('CSV file created successfully.')
else:
    print('Error: Failed to retrieve API data.')
