## Week 3: Working with Sheety API, Google Sheets and Python for Automation Tasks

### Sheety: https://sheety.co/

- Visit Sheety website
- Setup Sheety API Credentials and Google Spreadsheet
- Create a new Google Spreadsheet
- Create project in Sheety and get the API key
- Use the API key to access the Google Spreadsheet

Sample Request:

```python
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/your_project_name/sheet_name"


response = requests.get(url=SHEETY_ENDPOINT)
data = response.json()
print(data)
```

### Automated Inventory Replenishment

Monitor inventory levels and automatically place orders for items that fall below a certain threshold. Track orders and update inventory upon receiving new stock.

#### Steps:

- Set up a Google Sheet with columns for item name, current stock, reorder threshold, and supplier email.
- Use Sheety to create an API for the Google Sheet.
- Write a Python script to monitor inventory levels and send order emails when necessary.
- Update inventory levels when new stock is received.

##### Code Example

```python
import requests
import smtplib

SHEETY_API_URL = "https://api.sheety.co/YOUR_SHEETY_PROJECT/inventory"

def fetch_inventory():
    response = requests.get(SHEETY_API_URL)
    if response.status_code == 200:
        return response.json().get('inventory', [])
    else:
        print("Failed to fetch inventory:", response.text)
        return []

def send_order_email(to_address, item):
    from_address = "your_email@example.com"
    password = "your_password"
    subject = f"Reorder Request for {item['name']}"
    body = f"Dear Supplier,\n\nPlease send more stock for the following item:\n\nItem: {item['name']}\nCurrent Stock: {item['current_stock']}\nReorder Quantity: 100"

    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_address, password)
        server.sendmail(from_address, to_address, message)
        print(f"Order email sent to {to_address} for {item['name']}")

def update_inventory(item_id, new_stock):
    url = f"{SHEETY_API_URL}/{item_id}"
    data = {
        "inventory": {
            "current_stock": new_stock
        }
    }
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print(f"Updated stock of item ID {item_id} to {new_stock}")
    else:
        print(f"Failed to update stock of item ID {item_id}:", response.text)

if __name__ == "__main__":
    inventory = fetch_inventory()
    for item in inventory:
        if item['current_stock'] <= item['reorder_threshold']:
            send_order_email(item['supplier_email'], item)
            # Assuming we received the new stock immediately for simplicity
            new_stock = item['current_stock'] + 100
            update_inventory(item['id'], new_stock)
```
