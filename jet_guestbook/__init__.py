# -*- coding: utf-8 -*-

from jetfactory import Jetpack
from .app import controller, models, services

__jetpack__ = Jetpack(
    controller=controller,
    services=services,
    models=models,
    meta={
        'name': 'guestbook',
        'description': 'Example Guestbook Package',
    }
)
