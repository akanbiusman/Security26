import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("PAYSTACK_API_KEY")

headers = {
    'Authorization': f"Bearer {API_KEY}"
}


def create_new_customer(email, first_name, last_name, phone):
    new_customer = {
        "email": email,
        "first_name": first_name,
        "last_name": last_name,
        "phone": phone
    }

    response = requests.post(
        "https://api.paystack.co/customer", headers=headers, json=new_customer)

    data = response.json()

    return data


def get_customers():
    response = requests.get(
        "https://api.paystack.co/customer", headers=headers)

    data = response.json()

    return data


def get_customer_by_email(email):
    response = requests.get(
        f"https://api.paystack.co/customer/{email}", headers=headers)

    data = response.json()

    return data


def initialize_transaction(email, amount):
    cus_trans = {
        "email": email,
        "amount": amount
    }

    response = requests.post(
        "https://api.paystack.co/transaction/initialize", headers=headers, json=cus_trans)

    data = response.json()

    return data


def blacklist_customer(customer_code, risk_action):
    customer = {
        "customer": customer_code,
        "risk_action": risk_action
    }

    response = requests.post(
        f"https://api.paystack.co/customer/set_risk_action", headers=headers, json=customer)

    data = response.json()

    return data
