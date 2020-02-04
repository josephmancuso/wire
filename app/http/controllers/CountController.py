"""A CountController Module."""

from masonite.request import Request
from masonite.view import View
from masonite.controllers import Controller

class Component:

    def __init__(self, request: Request, view: View):
        """LivewireController Initializer

        Arguments:
            request {masonite.request.Request} -- The Masonite Request class.
        """
        self.request = request
        print('values', self.request.all())
        self.properties = self.request.input('data', {})
        self.view = view
    
    def render(self, template):
        self.set_properties()
        if hasattr(self, self.request.input('method', '')):
            getattr(self, self.request.input('method'))()

        return self.view.render(template, self.get_livewire_properties())

    def set_properties(self):
        self.__dict__.update(self.request.input('data', {}))

    def get_livewire_properties(self):
        new_dict = {}
        for attribute, value in self.properties.items():
            new_dict.update({attribute: self.__dict__.get(attribute)})
        return new_dict


class CountController(Component):
    """CountController Controller Class."""

    def show(self):
        return self.render('base')

    def increment(self):
        self.money += 1

    def decrement(self):
        self.money -= 1
