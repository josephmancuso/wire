"""A LoginComponentController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from .Component import Component
from masonite.auth import Auth
from masonite.validation import Validator
from app.User import User


class LoginComponentController(Component):
    """LoginComponentController Controller Class."""

    attrs = ['loggedIn', 'username', 'users', 'password', 'loggedInMessage', 'failed']

    def mount(self):
        self.loggedIn = False
        self.username = ''
        self.password = ''
        self.loggedInMessage = ''
        self.failed = False
        self.users = User.all().serialize()

    def show(self, view: View):
        return self.render('livewire.login')

    def store(self, request: Request, auth: Auth, validate: Validator):
        """Login the user.

        Arguments:
            request {masonite.request.Request} -- The Masonite request class.
            auth {masonite.auth.auth} -- The Masonite auth class.
            validate {masonite.validator.Validator} -- The Masonite Validator class.

        Returns:
            masonite.request.Request -- The Masonite request class.
        """
        # errors = request.validate(
        #     validate.required(['email', 'password']),
        #     validate.email('email'),
        # )

        if (auth.login(self.username, self.password)):
            self.loggedIn = True
            self.failed = False
            self.redirect('/home')
            return


        self.failed = True
        self.loggedIn = False
        return 'loggedin'

        # if errors:
        #     return request.back().with_errors(errors).with_input()

        # if auth.login(request.input('email'), request.input('password')):
        #     return request.redirect('/home')

        # return request.back().with_errors({
        #     'email': ["Email or password is incorrect"]
        # })
