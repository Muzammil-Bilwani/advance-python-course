from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from typing import TypeAlias
import json


# Create your views here.


'''
# Example Input:

  {
    "user_ids": ['1:', '2:', '3'],
    "items_with_prices": [
        {"Item A": 30},
        {"Item B": 45},
        {"Item C": 60},
    ]
    "sharing_details": {
      "Item_A": ['1', 2]
      },
      "Item_B": ['2', '3']
      },
      "Item_C": ['1', '2', '3']
      },
    },
    "tip_percentage": 15,  # Tip percentage
    "tax_percentage": 8    # Tax percentage,
    "discount_percentage": 5 # Discount percentage
  }
'''


@csrf_exempt
def splitWIthSharedItems(request):
    # Code goes here
    try:
        # Define Types for Variables

        UserIds: TypeAlias = list[str]
        ItemsWithPrices: TypeAlias = list[dict[str, float]]
        Sharing_Details: TypeAlias = dict[str, dict[str, list[str]]]
        Tip: TypeAlias = float
        Tax: TypeAlias = float
        Discount: TypeAlias = float

        ExpensePerUser: TypeAlias = dict[str, float]
        ExpensePerUserDetails: TypeAlias = dict[str,
                                                list[dict[str, str | float]]]

        BillingDetails: TypeAlias = dict[str, UserIds |
                                         ItemsWithPrices | Sharing_Details | Tip | Tax | Discount]

        # Check if request method is POST
        if request.method == 'POST':
            # Fetching Billing Details From The Request
            billing_details: BillingDetails = json.loads(request.body)

            # getting Deatils From Billing Details
            user_ids: UserIds = billing_details.get('user_ids')
            items_with_prices: ItemsWithPrices = billing_details.get(
                'items_with_prices')
            sharing_details: Sharing_Details = billing_details.get(
                'sharing_details')
            tip_percentage: Tip = billing_details.get('tip_percentage')
            tax_percentage: Tax = billing_details.get('tax_percentage')
            discount_percentage: Discount = billing_details.get(
                'discount_percentage')

            num_of_users = len(user_ids)
            num_of_items = len(items_with_prices)

            # Converting Tip, Tax & Discount to Decimal
            tip_percentage_decimal = tip_percentage / 100
            tax_percentage_decimal = tax_percentage / 100
            discount_percentage_decimal = discount_percentage / 100

            # Calculating Total Price Of All Items In The Bill By 1st Collecting Price Of Each Item In A List & Summing Up The Price Of All Items In The List Through sum()
            total_price = sum(
                [
                    price_to_item[item]
                    for price_to_item in items_with_prices
                    for item in price_to_item
                ]
            )

            '''
            Formula For Calculating a Portion Amount From Total Amount According To Percentage:
            portion amount = total amount * percentage/100
            ----OR----
            portion amount = total amount * percentage's decimal value
            '''

            # Calculating the Tip, Tax & Discount Amount From Total Price & Calculating The Amount For Each User By Dividing These Amounts By Number Of Users
            tip_amount = total_price * tip_percentage_decimal
            tip_per_user = tip_amount / num_of_users

            tax_amount = total_price * tax_percentage_decimal
            tax_per_user = tax_amount / num_of_users

            discount_amount = total_price * discount_percentage_decimal
            discount_per_item = discount_amount / num_of_items

            # Initializing Expense / User with 0
            expense_per_user: ExpensePerUser = {
                user_id: 0 for user_id in user_ids}

            # Initializing Expense / User Details with []
            expense_per_user_details: ExpensePerUserDetails = {
                user_id: [] for user_id in user_ids}

            # Loop Through Sharing Details to Calculate Expense Per User & Add Details To expense_per_user_details
            for shared_item in sharing_details:
                # Get Shared User Ids
                shared_user_ids = sharing_details[shared_item]
                # Initialize Item Price
                item_price = 0

                # Loop Through Items With Prices to Fetch Item Price & Reduce Item Price By Discount
                for price_to_item in items_with_prices:
                    # Check If Item Is Shared
                    if price_to_item.get(shared_item) != None:
                        # Update Item Price
                        item_price = price_to_item[shared_item] - \
                            discount_per_item
                        # Break Loop Because The Item Price Is Fetched & Updated
                        break

                # Calculate Price Per User By Dividing Item Price By Number Of Shared Users
                price_per_user = item_price / len(shared_user_ids)

                # Loop Through Shared User Ids To Update Expense Per User & Add Details To expense_per_user_details
                for user_id in shared_user_ids:
                    # Calculating Expense Per User By Adding Tip & Tax Per User to Price Per User
                    expense_per_user[user_id] += price_per_user + \
                        (tip_per_user + tax_per_user)

                    # Add Details To expense_per_user_details
                    expense_per_user_details[user_id].append(
                        {
                            "item_name": shared_item,
                            "item_price": item_price + discount_per_item,
                        }
                    )

                expense_per_user_details["discount_per_item"] = discount_per_item
                expense_per_user_details["tip_per_user"] = tip_per_user
                expense_per_user_details["tax_per_user"] = tax_per_user

            # Formulating Bill with details, including each user's expense expense_per_user, breakdown of expenses per user expense_per_user_details, total price total_price, discount amount discount_amount, tip amount tip_amount, tax amount tax_amount, and the final total total_expense_with_tip_&_tax_amount_after_discount after applying discounts, tips, and taxes.
            splitted_bill = {
                "expense_per_user": expense_per_user,
                "expense_per_user_details": expense_per_user_details,
                "total_price": total_price,
                "discount_amount": discount_amount,
                "tip_amount": tip_amount,
                "tax_amount": tax_amount,
                "total_expense_with_tip_&_tax_amount_after_discount": (total_price - discount_amount) + (tip_amount + tax_amount)
            }

            # Return splitted bill with status code 200
            return JsonResponse(splitted_bill, status=200)

        # If request method is not POST, Return error with status code 400
        return JsonResponse({"error": f"Invalid request method, {request.method}. Expected: POST"}, status=400)
    except Exception as e:
        # print error
        print(f"An error occurred:", e)
        # return error with status code 500
        return JsonResponse({'error': f'An error occurred: {e}'}, status=500)


# Example Output:
'''
{
  "expense_per_user": {
    "1": 55.7,
    "2": 88.55000000000001,
    "3": 63.2
  },
  "expense_per_user_details": {
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
  "total_expense_with_tips_&_tax": 166.05
}
'''
