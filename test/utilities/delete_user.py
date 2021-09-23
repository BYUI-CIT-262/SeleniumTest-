import requests

def delete_user(user_id, token):
    return requests.post(f"https://api.p59.dev/api/users/{user_id}/deleteTestUser", headers={
        "Authorization": f"bearer {token}"
    })
