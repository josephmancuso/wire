"""A LivewireController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller

from .Component import Component

class LivewireController(Component):
    """LivewireController Controller Class."""

    props = {
        'count': 10
    }
    
    def show(self):
        return self.render('livewire.count')

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1



    