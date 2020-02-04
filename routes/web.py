"""Web Routes."""

from masonite.routes import Get, Post, Match

ROUTES = [
    Match(['Get', 'POST'], '/?any', 'LivewireController@show'),
    Match(['Get', 'POST'], '/livewire/money/?any', 'CountController@show')
]
