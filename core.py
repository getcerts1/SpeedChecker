import requests
import subprocess
import string
import random
import time
TEMP_MAIL_BASE = "https://api.mail.tm"





""" --- CREATE EMAIL AND PASSWORD --- """

def domain():
    domain_req = requests.get(f"{TEMP_MAIL_BASE}/domains")
    domain = domain_req.json()["hydra:member"][0]["domain"]
    subdomain =  ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"{subdomain}@{domain}"

def generate_password():
    output = subprocess.check_output(["openssl", "rand", "-base64", "12"])
    return output.decode().strip()



""" --- CREATE ACCOUNT --- """
def create_account(email_, password_):
    data = {"address": email_,
            "password": password_}

    response = requests.post(f"{TEMP_MAIL_BASE}/accounts", json=data)
    if response.status_code == 201:
        print("success")
    elif response.status_code == 422:
        print("Account already exists")
    else:
        print("Failed to create account:", response.text)


""" --- RETRIEVE TOKEN --- """

def get_auth_header(email, password):
    data = {
        "address": email,
        "password": password
    }
    response = requests.post(f"{TEMP_MAIL_BASE}/token", json=data)
    if response.ok:
        token = response.json()["token"]
        header = {"Authorization": f"Bearer {token}"}
        return header
    return None


""" --- GET INBOX --- """

def inbox(header):
    for _ in range(10):
        response = requests.get(f"{TEMP_MAIL_BASE}/messages", headers=header) #token header
        messages = response.json().get("hydra:member", [])

        if messages:
            msg_id = messages[0]["id"]
            print(f"📨 New email: {messages[0]['subject']}")


            msg_detail = requests.get(f"{TEMP_MAIL_BASE}/messages/{msg_id}", headers=header).json()
            print("📖 Message:", msg_detail["text"])
            break
        else:
            time.sleep(5)
    else:
        print("⌛ No messages after 50 seconds.")