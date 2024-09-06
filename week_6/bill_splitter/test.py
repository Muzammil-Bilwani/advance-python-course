sharing_details = {
    "Item_A": {
        "user_ids": ['1', 2]
    },
    "Item_B": {
        "user_ids": ['2', '3']
    },
    "Item_C": {
        "user_ids": ['1', '2', '3']
    }
}

for shared_item in sharing_details:
    print(shared_item)

# print(sharing_details['i_1'])
print(sharing_details.get('i_1'))

items_with_prices = [
    {"Item A": 30},
    {"Item B": 45},
    {"Item C": 60},
]

total_price = [price_to_item[item]
               for price_to_item in items_with_prices for item in price_to_item]
print(total_price)
