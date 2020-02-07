"""A CountController Module."""

from jinja2 import Markup
from masonite.controllers import Controller
from masonite.request import Request
from masonite.view import View

from .Component import Component


class AlertController(Component):
    """Count Component"""

    attrs = ['message']


    def __init__(self):
        from wsgi import container
        self.message = 'This is a message'
        container.resolve(super().__init__)

    def show(self):
        return self.render('livewire.error')

