"""Web Routes."""

from masonite.routes import Get, Post, Match

def ComponentRoute(component, controller):
    return Match(['Get', 'POST'], f'/livewire/props/{component}', f'{controller}@show')




ROUTES = [
    Get('/', 'WelcomeController@show'),
    ComponentRoute('props', 'LivewireController'),
    ComponentRoute('count', 'CountController'),
    ComponentRoute('name', 'NameController'),
    ComponentRoute('error', 'AlertController'),
    ComponentRoute('login', 'LoginComponentController'),
    ComponentRoute('todo', 'TodoComponentController'),








    # Match(['Get', 'POST'], '/livewire/money', 'CountController@show')
]









from masonite.auth import Auth 
ROUTES += Auth.routes()
