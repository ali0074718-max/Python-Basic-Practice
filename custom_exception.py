class InvalidAgeError(Exception):
     pass

try:
    age = int(input("Enter age! "))
    if age < 0:
        raise InvalidAgeError(f"Age cannot be negative! {age}")
except InvalidAgeError as e:
    print(e)

