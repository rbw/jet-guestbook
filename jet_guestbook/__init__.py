# -*- coding: utf-8 -*-

from jetfactory import Jetpack
from .app import controller, models, services

pkg = Jetpack(
    controller=controller,
    services=services,
    models=models,
    name='guestbook',
    description='Example guestbook package'
)
