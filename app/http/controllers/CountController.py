"""A CountController Module."""

from jinja2 import Markup
from masonite.controllers import Controller
from masonite.request import Request
from masonite.view import View

from .Component import Component


class CountController(Component):
    """Count Component"""

    money = 10

    def show(self):
        return self.render('base')

    def increment(self):
        self.money += 1

    def decrement(self):
        self.money -= 1
