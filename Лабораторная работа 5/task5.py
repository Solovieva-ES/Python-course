import string
import random

def get_random_password() -> str:
    alpfabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    alpfabet= list(alpfabet)
    password = random.sample(alpfabet, 8)
    return "".join(password)

print(get_random_password())
