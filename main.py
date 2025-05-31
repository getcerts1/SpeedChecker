import time
import core



#use the same credentials for creating account, token and inbox

if __name__ == "__main__":
    #create account
    email = core.domain()
    password = core.generate_password()

    while core.create_account(email, password) != "success":
        core.create_account(email_=email, password_=password)
    time.sleep(3)

    auth_header = core.get_auth_header(email, password)

    #check inbox
    core.inbox(auth_header)


