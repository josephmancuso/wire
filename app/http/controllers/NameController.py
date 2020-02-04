"""A NameController Module."""

from masonite.controllers import Controller
from masonite.request import Request
from masonite.view import View

from .Component import Component


class NameController(Component):
    """NameController Controller Class."""

    props = {
        "name": "Joe",
        "count": 1
    }

    def __init__(self):
        from wsgi import container
        container.resolve(super().__init__)

    def show(self):
        print('running show method')
        return self.render('livewire.name')

    def increment(self):
        print('props is', self.props)
        print('incrementing')

        self.props['count'] += 1
