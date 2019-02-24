# -*- coding: utf-8 -*-

from jetfactory import Jetpack
from .app import controller, models, services

__version__ = '0.1.0'
__all__ = [
    '__version__',
    'pkg',
    'services'
]

pkg = Jetpack(
    controller=controller,
    services=services,
    models=models,
    name='guestbook',
    description='Example guestbook package'
)
