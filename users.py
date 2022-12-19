users = [
    {"username": "Ludvig", "level": 1},
    {"username": "Patric", "level": 2},
    {"username": "Katy", "level": 0},
    {"username": "Sam", "level": 1},
]

user_name = input("What is your name?  ")
language_level = input("What is your language level?")
new_user = {"username": user_name, "level": language_level}
users.append(new_user)


def user_out():
    for user in users:
        if user == new_user:
            break
    return user


user_out()

# user = {"username": "Ludvig", "level": 1}
