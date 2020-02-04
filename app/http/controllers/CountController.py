"""A CountController Module."""

from jinja2 import Markup
from masonite.controllers import Controller
from masonite.request import Request
from masonite.view import View

from .Component import Component


class CountController(Component):
    """Count Component"""

    attrs = ['count']


    def __init__(self):
        from wsgi import container
        self.count = 20
        # self.count = 10
        container.resolve(super().__init__)

    def show(self):
        return self.render('livewire.count')

    def increment(self):
        print('running count increment','count is', self.count)
        self.count += 1
        print('running count increment','count is', self.count)

    def decrement(self):
        self.count -= 1
