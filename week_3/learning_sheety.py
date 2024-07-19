import requests

def fetch_orders():
    url = 'https://api.sheety.co/aade571b3b1ec122a324d95e3445bebe/learningSheety/marksheet'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        orders_lists = data.get('marksheet', [])
        return orders_lists
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    orders = fetch_orders()
    if orders:
        print(orders)
