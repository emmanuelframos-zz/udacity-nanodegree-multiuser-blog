import re
from entities.user import User

class SignInValidator():

    @staticmethod
    def user_data_are_valid(fullname, user, password, params):
        if not fullname or len(fullname) < 8:
            params['error_message'] = 'That\'''s not a valid name'
            return True

        if not SignInValidator.valid_username(user):
            params['error_message'] = 'That\'''s not a valid username'
            return True

        if not SignInValidator.valid_password(password):
            params['error_message'] = 'That\'''s not a valid password'
            return True

        if SignInValidator.user_name_exists(user):
            params['error_message'] = 'User already exists'
            return True

        return False

    @staticmethod
    def user_name_exists(username):
        return User.get_user(username)

    @staticmethod
    def valid_username(user):
        return user and len(user) >= 8 and re.compile(r'^[a-zA-Z0-9_-]{3,20}$').match(user)

    @staticmethod
    def valid_password(password):
        return password and len(password) >= 8 and re.compile(r'^.{3,20}$').match(password)
