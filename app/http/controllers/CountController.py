"""A CountController Module."""

from jinja2 import Markup
from masonite.controllers import Controller
from masonite.request import Request
from masonite.view import View

from .Component import Component


class CountController(Component):
    """Count Component"""

    attrs = ['count']

    def mount(self):
        self.count = 20

    def show(self):
        return self.render('livewire.count')

    def increment(self):
        self.count = int(self.count) + 1

    def decrement(self):
        self.count = int(self.count) - 1
