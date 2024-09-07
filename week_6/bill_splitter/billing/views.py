from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from typing import TypeAlias
import json


# Create your views here.


''' ------ CODE STARTS HERE ----- '''


@csrf_exempt
def split_evenly(request):
    try:
        # Check if request method is POST
        if request.method == 'POST':

            # Define Types for Variables

            UserIds: TypeAlias = list[str]
            BillAmount: TypeAlias = float

            BillingDetails: TypeAlias = dict[str, UserIds | BillAmount]

            # Initializing Variables

            # Fetching Billing Details From The Request
            billing_details: BillingDetails = json.loads(request.body)

            # Fetching User Ids, Bill Amount From The Billing Details
            user_ids: UserIds = billing_details.get('user_ids')
            bill_amount: BillAmount = billing_details.get('bill_amount')

            # Splitting Bill Evenly
            splitted_bill = {user_id: bill_amount /
                             len(user_ids) for user_id in user_ids}

            # Returning Evenly Splitted Bill In Response
            return JsonResponse(splitted_bill, status=200)

        # Returning Error If Request Method Is Not POST
        return JsonResponse({f'Invalid request method {request.method}, only POST allowed'}, status=400)
    except Exception as e:
        # print error
        print(f"An error occurred:", e)
        # return error with status code 500
        return JsonResponse({'error': f'An error occurred: {e}'}, status=500)


@csrf_exempt
def split_unevenly(request):
    try:
        # Check if request method is POST
        if request.method == 'POST':

            # Define Types for Variables

            UserIds: TypeAlias = list[str]
            Contributions: TypeAlias = dict[str, float]
            BillAmount: TypeAlias = float

            BillingDetails: TypeAlias = dict[str,
                                             UserIds | Contributions | BillAmount]

            # Initializing Variables

            # Fetching Billing Details From The Request
            billing_details: BillingDetails = json.loads(request.body)

            # Fetching User Ids, Contributions, Bill Amount From The Billing Details
            user_ids: UserIds = billing_details.get('user_ids')
            contributions: Contributions = billing_details.get('contributions')
            bill_amount: BillAmount = billing_details.get('total_bill_amount')

            # Calculating the amount a user has to pay
            amount_per_user = bill_amount / user_ids.__len__()

            # Initializing Receipt and Payment Accounts For Each User
            receipt_and_payment_accounts = {user_id: 0 for user_id in user_ids}

            # Looping Through Each User to Calculate Receipt and Payment Accounts
            for user_id in user_ids:
                # Adding The Amount A User Has To Pay To The Receipt And Payment Accounts By Reducing Their Contribution With The Amount A User Has To Pay
                receipt_and_payment_accounts[user_id] += amount_per_user - \
                    contributions[user_id]

            # Formulating the Bill Splitted Unevenly According to the Contributions Each User Has Made With Their Corresponding Receipt And Payment Accounts, The Total Bill Amount, And The Amount A User Has To Pay & The Contributions
            splitted_bill = {
                "receipt_and_payment_accounts": receipt_and_payment_accounts,
                "total_bill_amount": bill_amount,
                "amount_per_user": amount_per_user,
                "contributions": contributions,
                "note": "Negative value (-) means receipt beacuse it's showing that the user has paid more than his bill so he has to receive the difference. Positive value (+) means payment because it's showing that the user has not paid or has paid less than his bill so he has to pay the difference & 0 means No receipt - No payment."
            }

            # Returning Unevenly Splitted Bill In Response With 200 Status Code
            return JsonResponse(splitted_bill, status=200)

        # Returning Error If Request Method Is Not POST
        return JsonResponse({f'Invalid request method {request.method}, only POST allowed'}, status=400)

    except Exception as e:
        # print error
        print(f"An error occurred:", e)
        # return error with status code 500
        return JsonResponse({'error': f'An error occurred: {e}'}, status=500)


@csrf_exempt
def split_including_tip_tax(request):
    try:
        # Check if request method is POST
        if request.method == 'POST':

            # Define Types for Variables

            UserIds: TypeAlias = list[str]
            BillAmount: TypeAlias = float
            TipPercentage: TypeAlias = float
            TaxPercentage: TypeAlias = float

            BillingDetails: TypeAlias = dict[str,
                                             UserIds | BillAmount | TipPercentage | TaxPercentage]

            # Initializing Variables

            # Fetching Billing Details From The Request
            billing_details: BillingDetails = json.loads(request.body)

            # Fetching User Ids, Bill Amount, TipPercentage Percentage, and TaxPercentage Percentage From The Billing Details
            user_ids: UserIds = billing_details.get('user_ids')
            bill_amount: BillAmount = billing_details.get('total_bill_amount')
            tip_percentage: TipPercentage = billing_details.get(
                'tip_percentage')
            tax_percentage: TaxPercentage = billing_details.get(
                'tax_percentage')

            # Calculating The Number Of Users
            num_of_users = len(user_ids)

            # Converting Percentage To Decimal
            tip_percentage = tip_percentage / 100
            tax_percentage = tax_percentage / 100

            # Calculating The Tip & Tax Amount Each User Has To Pay With Their Corresponding Bill Amount By Multiplying Their Bill Amount With The Tip & Tax Percentage
            tip_amount = bill_amount * tip_percentage
            tax_amount = bill_amount * tax_percentage

            # Calculating The Bill Amount Including Tip & Tax
            bill_amount_including_tip_and_tax = bill_amount + tip_amount + tax_amount

            # Calculating The Amount A User Has To Pay
            amount_per_user_incliding_tip_and_tax = bill_amount_including_tip_and_tax / num_of_users

            return JsonResponse({
                'amount_per_user_incliding_tip_and_tax': amount_per_user_incliding_tip_and_tax
            }, status=200)

        # Returning Error If Request Method Is Not POST
        return JsonResponse({f'Invalid request method {request.method}, only POST allowed'}, status=400)
    except Exception as e:
        # print error
        print(f"An error occurred:", e)
        # return error with status code 500
        return JsonResponse({'error': f'An error occurred: {e}'}, status=500)


@csrf_exempt
def split_with_discount(request):
    '''
    Input: List of user IDs, total bill amount, and discount percentage.
    Example: {
        "user_ids": ["user1", "user2", "user3"],
        "total_bill_amount": 100,
        "discount_percentage": 10
    }
    '''
    try:
        # Check if request method is POST
        if request.method == 'POST':

            # Define Types for Variables

            UserIds: TypeAlias = list[str]
            print(f"UserIds: {UserIds}")

            BillAmount: TypeAlias = float
            print(f"BillAmount: {BillAmount}")

            DiscountPercentage: TypeAlias = float
            print(f"DiscountPercentage: {DiscountPercentage}")

            BillingDetails: TypeAlias = dict[str,
                                             UserIds | BillAmount | DiscountPercentage]
            print(f"BillingDetails: {BillingDetails}")

            # Initializing Variables

            # Fetching Billing Details From The Request
            billing_details: BillingDetails = json.loads(request.body)

            # Fetching User Ids, Bill Amount, and Discount Percentage From The Billing Details
            user_ids: UserIds = billing_details.get('user_ids')
            print(f"user_ids: {user_ids}")

            bill_amount: BillAmount = billing_details.get('total_bill_amount')
            print(f"bill_amount: {bill_amount}")

            discount_percentage: DiscountPercentage = billing_details.get(
                'discount_percentage')
            print(f"discount_percentage: {discount_percentage}")

            # Calculating The Number Of Users
            num_of_users = len(user_ids)
            print(f"num_of_users: {num_of_users}")

            # Converting Percentage To Decimal
            discount_percentage_decimal = discount_percentage / 100
            print(f"discount_percentage_decimal: {
                  discount_percentage_decimal}")

            # Calculating The Discount Amount From The Bill Amount
            discount_amount = bill_amount * discount_percentage_decimal
            print(f"discount_amount: {discount_amount}")

            # Applying The Discount To The Bill Amount
            bill_amount_after_discount = bill_amount-discount_amount
            print(f"bill_amount_after_discount: {bill_amount_after_discount}")

            # Calculating The Amount A User Has To Pay After Applying The Discount
            amount_per_user_after_discount = bill_amount_after_discount / num_of_users
            print(f"amount_per_user_after_discount: {
                  amount_per_user_after_discount}")

            # Returning The Response With The Amount A User Has To Pay After Applying The Discount
            return JsonResponse({
                'amount_per_user_after_discount': amount_per_user_after_discount
            }, status=200)

        # Returning Error If Request Method Is Not POST
        return JsonResponse({f'Invalid request method {request.method}, only POST allowed'}, status=400)

    except Exception as e:
        # print error
        print(f"An error occurred:", e)
        # return error with status code 500
        return JsonResponse({'error': f'An error occurred: {e}'}, status=500)


@csrf_exempt
def split_with_shared_items(request):
    try:
        # Check if request method is POST
        if request.method == 'POST':

            # Define Types for Variables

            UserIds: TypeAlias = list[str]
            ItemsWithPrices: TypeAlias = list[dict[str, float]]
            Sharing_Details: TypeAlias = dict[str, dict[str, list[str]]]
            TipPercentage: TypeAlias = float
            TaxPercentage: TypeAlias = float
            DiscountPercentage: TypeAlias = float

            ExpensePerUser: TypeAlias = dict[str, float]
            ExpensePerUserDetails: TypeAlias = dict[str,
                                                    list[dict[str, str | float]]]

            BillingDetails: TypeAlias = dict[str, UserIds |
                                             ItemsWithPrices | Sharing_Details | TipPercentage | TaxPercentage | DiscountPercentage]

            # Initializing Variables

            # Fetching Billing Details From The Request
            billing_details: BillingDetails = json.loads(request.body)

            # Fetching User Ids, Bill Amount From The Billing Details
            user_ids: UserIds = billing_details.get('user_ids')
            items_with_prices: ItemsWithPrices = billing_details.get(
                'items_with_prices')
            sharing_details: Sharing_Details = billing_details.get(
                'sharing_details')
            tip_percentage: TipPercentage = billing_details.get(
                'tip_percentage')
            tax_percentage: TaxPercentage = billing_details.get(
                'tax_percentage')
            discount_percentage: DiscountPercentage = billing_details.get(
                'discount_percentage')

            num_of_users = len(user_ids)
            num_of_items = len(items_with_prices)

            # Converting TipPercentage, TaxPercentage & Discount to Decimal
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

            # Calculating the Tip, Tax & Discount Amount By Dividing Their Percentage Values From Total Price & Calculating The Tip & Tax For Each User By Dividing These Amounts By Number Of Users & Discount Amount By Number Of Items
            tip_amount = total_price * tip_percentage_decimal
            tip_per_user = tip_amount / num_of_users

            tax_amount = total_price * tax_percentage_decimal
            tax_per_user = tax_amount / num_of_users

            discount_amount = total_price * discount_percentage_decimal
            discount_per_item = discount_amount / num_of_items

            # Initializing Expense / User with 0
            expense_per_user: ExpensePerUser = {
                user_id: 0 for user_id in user_ids
            }

            # Initializing Expense / User Details with []
            expense_per_user_details: ExpensePerUserDetails = {
                user_id: [] for user_id in user_ids
            }

            # Loop Through Sharing Details to Calculate Expense Per User & Add Details To expense_per_user_details
            for shared_item in sharing_details:
                # Get Shared User Ids
                shared_user_ids = sharing_details[shared_item]
                # Calculate Number Of Shared Users
                num_of_shared_users = len(shared_user_ids)
                # Initialize Item Price
                item_price = 0

                # Loop Through Items With Prices to Fetch Item Price & Reduce Item Price By Discount
                for price_to_item in items_with_prices:
                    # Check If Item Is Shared
                    if price_to_item.get(shared_item) is not None:
                        # Update Item Price
                        item_price = price_to_item[shared_item] - \
                            discount_per_item
                        # Break Loop Because The Item Price Is Fetched & Updated
                        break

                # Calculate Price Per User By Dividing Item Price By Number Of Shared Users
                price_per_user = item_price / num_of_shared_users

                # Loop Through Shared User Ids To Update Expense Per User & Add Details To expense_per_user_details
                for user_id in shared_user_ids:
                    # Calculating Expense Per User By Adding Tip & Tax portions To Price Per User to Price Per User
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

            # Formulating Bill with details, including each user's expense expense_per_user, breakdown of expenses per user expense_per_user_details, total price total_price, discount amount discount_amount, tip amount tip_amount, tax amount tax_amount, and the final total total_expense_with_tip_and_tax_after_discount after applying discounts, tips, and taxes.
            bill_splitted_with_shared_items = {
                "expense_per_user": expense_per_user,
                "expense_per_user_details": expense_per_user_details,
                "total_price": total_price,
                "discount_amount": discount_amount,
                "tip_amount": tip_amount,
                "tax_amount": tax_amount,
                "total_expense_with_tip_&_tax_amount_after_discount": (total_price - discount_amount) + (tip_amount + tax_amount)
            }

            # Return splitted bill with status code 200
            return JsonResponse(bill_splitted_with_shared_items, status=200)

        # If request method is not POST, Return error with status code 400
        return JsonResponse({"error": f"Invalid request method, {request.method}. Expected: POST"}, status=400)

    except Exception as e:
        # print error
        print(f"An error occurred:", e)
        # return error with status code 500
        return JsonResponse({'error': f'An error occurred: {e}'}, status=500)


''' ------ END OF CODE ----- '''
