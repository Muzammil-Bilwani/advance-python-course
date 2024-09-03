# Lets learn more APIs

## Task 1: Basic Bill Splitting

Create an endpoint to split a bill evenly among a group of users.

- **Endpoint**: `/split-evenly`
- **Method**: `POST`
- **Input**: List of user IDs and total bill amount.
- **Output**: Amount each user needs to pay.

## Task 2: Uneven Bill Splitting

Create an endpoint to split a bill unevenly based on individual contributions.

- **Endpoint**: `/split-unevenly`
- **Method**: `POST`
- **Input**: List of user IDs, their respective contributions, and the total bill amount.
- **Output**: Amount each user needs to pay or receive.

## Task 3: Including Tip and Tax

Create an endpoint to split a bill including tip and tax evenly among users.

- **Endpoint**: `/split-including-tip-tax`
- **Method**: `POST`
- **Input**: List of user IDs, total bill amount, tip percentage, and tax percentage.
- **Output**: Amount each user needs to pay including tip and tax.

## Task 4: Handling Discounts

Create an endpoint to apply a discount to the total bill before splitting it evenly among users.

- **Endpoint**: `/split-with-discount`
- **Method**: `POST`
- **Input**: List of user IDs, total bill amount, and discount percentage.
- **Output**: Amount each user needs to pay after discount.

## Task 5: Advanced Bill Splitting with Shared Items

Create an endpoint to split a bill where some items are shared among certain users.

- **Endpoint**: `/split-with-shared-items`
- **Method**: `POST`
- **Input**: List of user IDs, list of items with prices, and list of user IDs for each shared item.
- **Output**: Amount each user needs to pay.
