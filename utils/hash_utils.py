import hashlib
import uuid

class HashUtils():

    @staticmethod
    def gen_salt():
        return uuid.uuid4().hex

    @staticmethod
    def crypt(password, salt):
        return hashlib.sha512(password+salt).hexdigest()

    @staticmethod
    def hasPermission(password, salt, hash):
        return hashlib.sha512(password+salt).hexdigest() == hash