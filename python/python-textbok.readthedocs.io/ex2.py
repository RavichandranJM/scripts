#/usr/local/bin/python3.7

# Exceptions

class DuplicateUserError(Exception):
    pass

class InvalidAgeError(Exception):
    pass

class UnderAgeError(Exception):
    pass

class InvalidEmailError(Exception):
    pass

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email

exampleList = [
    ("jane", "jane@example.com", 21),
    ("bob", "bob@example", 19),
    ("jane", "jane2@example.com", 25),
    ("steve", "steve@somewhere", 15),
    ("joe", "joe", 23),
    ("anna", "anna@example.com", -3),
]
directory = {}

for name, email, age in exampleList:
    try:
        if name in directory:
            raise DuplicateUserError
        if age < 0:
            raise InvalidAgeError
        if age < 16:
            raise UnderAgeError
        emailParts = email.split("@")
        if len(emailParts) != 2 or not emailParts[0] or not emailParts[1]:
            raise InvalidEmailError
    except DuplicateUserError:
        print("User {} already exist".format(name))
    except InvalidAgeError:
        print("Invalid age: {}".format(age))
    except UnderAgeError:
        print("Under Age: {}".format(age))
    except InvalidEmailError:
        print("{} is not a valid email".format(email))
    else:
        directory[name] = User(name, email)

