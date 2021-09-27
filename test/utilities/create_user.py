import requests

args = {
        "firstName": 'test',
        "lastName": 'test',
        "isTesterUser": True,
        "contactNumber": '9999999485',
        "emailId": 'p59testa+1@gmail.com',
        "password": 'Love1111',
        "zipCode": '83440',
        "otpCode": 9865
    }


def create_user():
    return requests.post(f"https://api.p59.dev/api/account/sign-up?otp_check=true", json=args)
