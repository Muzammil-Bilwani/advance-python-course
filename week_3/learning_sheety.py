import requests

def fetch_orders():
    url = 'https://api.sheety.co/aade571b3b1ec122a324d95e3445bebe/marksheet/marksheet'
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        orders_lists = data.get('marksheet', [])
        return orders_lists
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None



if __name__ == "__main__":
    # orders = fetch_orders()
    # if orders:
        # print(orders)
    url = "https://api.sheety.co/aade571b3b1ec122a324d95e3445bebe/marksheet/marksheet"

    response = requests.post(url, json={
        "marksheet":{
        "name":"Shayaan",
        "class":1,
        "math":20,
        "english":20,
        "urdu":20,
        "total":60,
        }
    },
    headers={
        "Content-Type": "application/json"
    }
    )
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Failed to fetch data. Status code: {response.json()}")

