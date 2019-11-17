from pytonik import Web

from pytonik import Web


class Users:

    def __getattr__(self, item):
        return item

    def __init__(self):
        self.db = Web.Model().db

    def list(self):

        # database query here

        return ""