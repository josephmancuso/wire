"""A NameController Module."""

from masonite.controllers import Controller
from masonite.request import Request
from masonite.view import View
from masonite.auth import Auth

from .Component import Component


class NameController(Component):
    """NameController Controller Class."""

    attrs = ['name', 'count', 'see', 'username', 'failed', 'password', 'success', 'loggedin']

    def __init__(self, auth: Auth):

        self.name = "Joe"
        self.count = 10
        self.see = False
        self.loggedin = False
        self.failed = False
        resolve(super().__init__)

    def show(self):
        return self.render('livewire.name')

    def increment(self):

        self.count += 1

    def visible(self):
        self.see = True

    def login(self):
        from wsgi import container
        auth = container.make(Auth)

        if (auth.login(self.username, self.password or '')):
            self.failed = False
            self.loggedin = True
            return

        self.failed = True
        self.loggedin = False
