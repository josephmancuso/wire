"""A LoginComponentController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller
from .Component import Component
from masonite.auth import Auth
from masonite.validation import Validator
from app.User import User
from app.Todo import Todo


class TodoComponentController(Component):
    """LoginComponentController Controller Class."""

    attrs = ['name', 'description', 'todos']

    def mount(self):
        self.name = ''
        self.description = ''
        self.todos = Todo.all().serialize()

    def show(self, view: View):
        return self.render('livewire.todo')

    def create(self):
        """Login the user.

        Arguments:
            request {masonite.request.Request} -- The Masonite request class.
            auth {masonite.auth.auth} -- The Masonite auth class.
            validate {masonite.validator.Validator} -- The Masonite Validator class.

        Returns:
            masonite.request.Request -- The Masonite request class.
        """ 

        Todo.create({
            'name': self.name,
            'description': self.description
        })

        print('creating todo')
        self.mount()

    def delete(self, request: Request):
        """Login the user.

        Arguments:
            request {masonite.request.Request} -- The Masonite request class.
            auth {masonite.auth.auth} -- The Masonite auth class.
            validate {masonite.validator.Validator} -- The Masonite Validator class.

        Returns:
            masonite.request.Request -- The Masonite request class.
        """ 


        Todo.find(request.input('todo_id')).delete()
        self.mount()
