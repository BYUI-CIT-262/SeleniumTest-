import requests

def delete_user(id, token):
    return requests.post(f"https://api.p59.dev/api/users/{id}/deleteTestUser", headers={
        "Authorization": f"bearer {token}"
    })


