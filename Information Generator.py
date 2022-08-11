# Info App

"""
    Make an information generator
  - Make a program that will generate a: name, email, address, tel num, height, ethnicity, eye colour etc.
  -- Bonus points if you can store the generated person in a dictionary so that you can access information about
  -- them at any time
  """


# Setup
from random import choice, randint, uniform

fname_list = ["John","Eve","Juan","Louis"]
lname_list = ["Smith","Kovalsky","McDonald"]
emails = ["gmail",'yahoo']
countries = ["com","org"]

# App
first_name = choice(fname_list)
last_name = choice(lname_list)
email = f"{first_name}.{last_name}@{choice(emails)}.{choice(countries)}"
phone_number = "".join([str(randint(0,9)) for x in range(0,9)])
height = round(uniform(1, 2),2)

print(f" Hey {first_name} {last_name}. Your email is {email}, phone number is {phone_number} and your height is {height}m!")



