import re


class Email:
    def __init__(self, email):
        if self.validate(email):
            self.email = email
        else:
            raise Exception('email entered incorrectly')

    def validate(self, email):
        pattern = r"^[-\w\.]+@([-\w]+\.)+[-\w]{2,4}$"
        if re.match(pattern, email) is not None:
            return True
        else:
            return False


print(Email('shkarupa237@gmail.com').email)


