from validator_collection import validators
address = input("What's your email address? ")
try:
    email = validators.email(address)
    print("Valid")
except ValueError:
    print("Invalid")
