import random
import string

def random_string_gen(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def random_email(size=7, chars=string.ascii_lowercase):
    email = ''.join(random.choice(chars) for _ in range(size)) + '@gmail.com'
    return email
