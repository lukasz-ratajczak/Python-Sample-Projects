# Info App

# Setup
from random import choice, randint


# App
first_name = choice(fname_list)
last_name = choice(lname_list)
email = f"{first_name}.{last_name}@{choice(emails)}.{countries}"
phone_number = "".join([randint(0,9) for x in range(0,9)])


