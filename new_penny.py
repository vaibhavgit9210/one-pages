import requests
import json
import time

# Set your key ID and secret
key_id = 'rzp_live_5enyDt1VeMy4S8'
key_secret = 'Qqjy7QEVBPv0kucozsubQJqy'
ifsc = 'BARB0KHASUR'
acc_num = '7390100024926'

# Set the endpoint URLs
fund_accounts_url = 'https://api.razorpay.com/v1/fund_accounts'
validations_url = 'https://api.razorpay.com/v1/fund_accounts/validations'

# Set the request headers
headers = {
    'Content-Type': 'application/json'
}

# Set the request body for creating a fund account
fund_account_body = {
    'contact_id': 'cont_LQfkVWBojNlVIf',
    'account_type': 'bank_account',
    'bank_account': {
        'name': 'RZP',
        'ifsc': ifsc,
        'account_number': acc_num
    }
}

# Make the POST request to create a fund account
response = requests.post(
    fund_accounts_url,
    headers=headers,
    auth=(key_id, key_secret),
    json=fund_account_body
)

# Get the ID of the created fund account from the response
fund_account_id = response.json()['id']

# Set the request body for validating the fund account
validation_body = {
    'account_number': '4564563319243921',
    'fund_account': {
        'id': fund_account_id
    },
    'amount': 100,
    'currency': 'INR',
    'notes': {
        'random_key_1': 'Make it so.',
        'random_key_2': 'Tea. Earl Grey. Hot.'
    }
}

# Make the POST request to validate the fund account
response = requests.post(
    validations_url,
    headers=headers,
    auth=(key_id, key_secret),
    json=validation_body
)

# Adding buffer
time.sleep(15)

validated_account_id = response.json()['id']

print(response.json()['id'])

response = requests.get(
    validations_url + '/' + validated_account_id,
    auth=(key_id, key_secret)
)

data = json.dumps(response.json(), indent=2)

print(data)

