"""A NameController Module."""

from masonite.controllers import Controller
from masonite.request import Request
from masonite.view import View

from .Component import Component


class NameController(Component):
    """NameController Controller Class."""

    attrs = ['name', 'count']

    def __init__(self):
        from wsgi import container
        self.name = "Joe"
        self.count = 10
        container.resolve(super().__init__)

    def show(self):
        return self.render('livewire.name')

    def increment(self):

        self.count += 1
