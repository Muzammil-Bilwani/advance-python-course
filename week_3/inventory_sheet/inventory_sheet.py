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

if __name__ == "__main__":
    inventory = fetch_inventory()
    for item in inventory:
        if item['current_stock'] <= item['reorder_threshold']:
            send_order_email(item['supplier_email'], item)
            # Assuming we received the new stock immediately for simplicity
            # new_stock = item['current_stock'] + 100
            # update_inventory(item['id'], new_stock)
