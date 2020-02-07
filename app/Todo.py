"""Todo Model."""

from config.database import Model


class Todo(Model):
    """Todo Model."""
    
    __fillable__ = ['name', 'description']