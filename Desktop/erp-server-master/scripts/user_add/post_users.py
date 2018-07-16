from os import urandom
import pandas as pd
import requests

# def generate_temp_password(length=9):
#     chars = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789"
#     return "".join(chars[ord(c) % len(chars)] for c in urandom(length))


users = pd.read_csv('testresult.csv')

for i in range(len(users)):
    # temp_pass = generate_temp_password()
    payload = {
        'name': users.loc[i, "NAME"],
        'email': users.loc[i, "E-MAIL ID"],
        'number': int(users.loc[i, "CONTACT NUMBER"]),
        'profile_photo_url': users.loc[i, "profile_photo_url"],
        'profile_url': users.loc[i, "PROFILE LINK"],
        'department': users.loc[i, "DEPARTMENT"],
        'designation': users.loc[i, "DESIGNATION"],
        'role': users.loc[i, "ROLE"],
        'password': str(users.loc[i, "CONTACT NUMBER"])
    }
    r = requests.post('http://127.0.0.1:5000/users', json=payload)
    if r.status_code == requests.codes.ok:
        print("Created User : ", payload['email'])
    else:
        print("Unsuccessfull : ", payload['email'])