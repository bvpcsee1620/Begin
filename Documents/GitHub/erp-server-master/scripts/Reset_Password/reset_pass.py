import pandas as pd
import requests

users = pd.read_csv('users_alpha.csv')

for i in range(len(users)):
    # temp_pass = generate_temp_password()
    if users.loc[i, "Sendmail"] == 1 and users.loc[i, "Sendmail"] == 0:
	    payload = {
	        'email': users.loc[i, "email"]
	    }
	    r = requests.post('http://127.0.0.1:5000/emailreset', json=payload)
	    if r.status_code == requests.codes.ok:
	        print("Mail Sent to : ", payload['email'])
	        users.loc[i, "Sendmail"] = 1
	    else:
	        print("Unsuccessfull : ", r.status_code)

users.to_csv('users_alpha.csv', index=False)