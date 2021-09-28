def create_user():
    import requests
    user_email = 'pitch59testa+3@gmail.com'

    args = {
            "firstName": 'test',
            "lastName": 'test',
            "isTesterUser": True,
            "contactNumber": '9999999486',
            "emailId": user_email,
            "password": 'Love1111',
            "zipCode": '83440',
            "otpCode": 1234
            }

    signupURL = "api/account/sign-up?otp_check=true"

    # set a variable to equal the URL
    pitch59_URL = f"https://api.p59.dev/{signupURL}"

    response = requests.post(pitch59_URL, json=args)
    # check for successful request
    if response.status_code == 200:
        #convert data to a python dictionary
        print(response.status_code, "- Create User Success!", "\n")
        data_dict = response.json()["data"]
        userId = data_dict["userId"]
        userToken = data_dict["token"]
    else:
        #The request failed- print the status code:
        print("Failure with status code:", response.status_code)
        print(response.json())

    return userId, userToken, user_email
