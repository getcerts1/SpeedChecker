import time
import core



#use the same credentials for creating account, token and inbox

if __name__ == "__main__":
    email = core.domain()
    password = core.generate_password()

    print(email)
    print(password)

    while core.create_account() != "success":
        core.create_account(email_=email, password_=password)
    time.sleep(3)

    auth_header = core.get_auth_header(email, password)
    core.inbox(auth_header)


