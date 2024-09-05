from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from typing import TypeAlias
import json


# Example Input:
'''
{
    "user_ids": ['1:', '2:', '3'],
    "items": [
        {"name": "Item A", "price": 30, "shared_user_ids": [1, 2]},
        {"name": "Item B", "price": 45, "shared_user_ids": [2, 3]},
        {"name": "Item C", "price": 60, "shared_user_ids": [1, 2, 3]}
    ],
    "tip_percentage": 15,  # Tip percentage
    "tax_percentage": 8    # Tax percentage,
    "discount_percentage": 5
}
'''

# Example Output:
'''
{
  "expense_per_user": {
    "1": 55.7,
    "2": 88.55000000000001,
    "3": 63.2
  },
  "per_item_user_expense": {
    "1": [
      {
        "item_name": "Item A",
        "item_price": 15.0
      },
      {
        "item_name": "Item C",
        "item_price": 20.0
      }
    ],
    "2": [
      {
        "item_name": "Item A",
        "item_price": 15.0
      },
      {
        "item_name": "Item B",
        "item_price": 22.5
      },
      {
        "item_name": "Item C",
        "item_price": 20.0
      }
    ],
    "3": [
      {
        "item_name": "Item B",
        "item_price": 22.5
      },
      {
        "item_name": "Item C",
        "item_price": 20.0
      }
    ],
    "total_price": 135
  },
  "tip_amount": 20.25,
  "tax_amount": 10.8,
  "total_expense_with_tips_and_tax": 166.05
}
'''


# Create your views here.


@csrf_exempt
def splitWIthSharedItems(request):
    # Code goes here
    try:
        # Check if request method is POST
        if request.method == 'POST':

            # Define the types

            BillingDetails: TypeAlias = dict[str,
                                             int | str | list[dict[str, int | str]]]
            Items: TypeAlias = list[dict[str, str | float, list[str]]]
            UserIds: TypeAlias = list[str]

            # Getting billing details from request
            billing_details: BillingDetails = json.loads(request.body)

            # Unpacking billing details
            user_ids: UserIds = billing_details['user_ids']
            items: Items = billing_details['items']
            tip_percentage = billing_details['tip_percentage']
            tax_percentage = billing_details['tax_percentage']
            discount_percentage = billing_details['discount_percentage']

            # Calculating number of user
            num_of_user = len(user_ids)

            # Initializing dictionary to store expense per user
            expense_per_user = {user_id: 0 for user_id in user_ids}
            # Initializing dictionary to store expense per item a user is sharing
            per_item_user_expense = {user_id: [] for user_id in user_ids}

            # Converting percentages to decimal
            tip_percentage_decimal = tip_percentage / 100
            tax_percentage_decimal = tax_percentage / 100
            discount_percentage_decimal = discount_percentage / 100

            # It will 1st collect all items price in a list and then we total them by sum()
            total_price = sum([item['price'] for item in items])

            ''' ----- Formula to calculate portion amount ------ '''

            # portion_amount = total_amount * decimal value of percentage
            # portion_amount = total_amount * (percentage / 100)

            ''' ----- Formula Ends ------ '''

            # tax_amount -or- tax's portion in total price amount = (total_price * tax_percentage's decimal value)
            tax_amount = total_price * tax_percentage_decimal
            # Distributing tax amount among all users
            tax_per_user = tax_amount/num_of_user

            # tip_amount -or- tip's portion in total price amount = (total_price * tip_percentage's decimal value)
            tip_amount = total_price * tip_percentage_decimal
            # Distributing tip amount among all users
            tip_per_user = tip_amount/num_of_user

            # discount_amount -or- discount's portion in total price amount = (total_price * discount_percentage's decimal value)
            discount_amount = total_price * discount_percentage_decimal
            # Distributing tip amount among all users
            discount_per_user = discount_amount/num_of_user

            # Calculating total expense by adding tips and tax amount in total price
            total_expense = (total_price-discount_amount) + \
                (tip_amount+tax_amount)

            # Looping through all items to calculate expense per user and per item user expense
            for item in items:
                # Calculating number of shared users on the item
                num_of_shared_users = len(item['shared_user_ids'])
                # Calculating item price per shared user
                item_price_per_user = (item['price'] / num_of_shared_users)

                # Looping through all shared users
                for user_id in item['shared_user_ids']:
                    # Collecting expense per user by adding item price per user and tips and tax amount per user
                    expense_per_user[user_id] += (item_price_per_user - discount_per_user) + (
                        tip_per_user + tax_per_user)

                # Collecting item details containing item name and item price per user
                    item_details = {
                        "item_name": item['name'], 'item_price': item_price_per_user}
                    # appending item details in per_item_user_expense
                    per_item_user_expense[user_id].append(item_details)

            # Putting total price in per_item_user_expense
            per_item_user_expense['total_price'] = total_price

            # Returning splitted bill with all details including, expense per user, per item user expense, tip amount, tax amount, total expense
            splitted_bill = {
                'expense_per_user': expense_per_user,
                'per_item_user_expense': per_item_user_expense,
                'discount_amount': discount_amount,
                'tip_amount': tip_amount,
                'tax_amount': tax_amount,
                'total_expense_with_discount_and_tip_and_tax_amount': total_expense,
            }

            # Returning json-response with splitted bill and status code 200
            return JsonResponse(splitted_bill, status=200)

        # If request method is not POST, Return error with status code 400
        return JsonResponse({"error": f"Invalid request method, {request.method}. Expected: POST"}, status=400)
    except Exception as e:
        # print error
        print(f"An error occurred:", e)
        # return error with status code 500
        return JsonResponse({'error': f'An error occurred: {e}'}, status=500)
