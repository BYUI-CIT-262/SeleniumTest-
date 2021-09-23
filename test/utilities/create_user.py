import requests

def create_user(user_dict):
    return requests.post(f"https://api.p59.dev/api/account/sign-up?otp_check=true", json=user_dict)
