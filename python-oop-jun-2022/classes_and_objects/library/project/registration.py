from project.library import Library
from project.user import User


class Registration:
    def __init__(self):
        pass

    def add_user(self, user: User, library: Library):
        if user in library.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        library.user_records.append(user)

    def remove_user(self, user: User, library: Library):
        if user not in library.user_records:
            return "We could not find such user to remove!"
        library.user_records.remove(user)

    def change_username(self, user_id, new_username, library: Library):
        for user in library.user_records:
            if user.user_id == user_id:
                if user.username != new_username:
                    old_name = user.username
                    user.username = new_username
                    for usr in library.rented_books:
                        if usr == old_name:
                            usr = new_username
                    return f"Username successfully changed to: {new_username} for user id: {user_id}"
                return "Please check again the provided username - " \
                       "it should be different than the username used so far!"
            return f"There is no user with id = {user_id}!"
