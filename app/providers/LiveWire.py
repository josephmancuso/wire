"""A LiveWire Service Provider."""

from masonite.provider import ServiceProvider


class LiveWire(ServiceProvider):
    """Provides Services To The Service Container."""

    wsgi = False

    def register(self):
        """Register objects into the Service Container."""
        pass

    def boot(self):
        """Boots services required by the container."""
        pass
