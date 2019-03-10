# -*- coding: utf-8 -*-

from jetfactory import Jetpack
from jet_guestbook import service
from .service import VisitService, VisitorService
from .model import VisitModel, VisitorModel
from .controller import Controller

__version__ = '0.1.0'

export = Jetpack(
    controller=Controller,
    services=[VisitService, VisitorService],
    models=[VisitModel, VisitorModel],
    name='guestbook',
    description='Example guestbook package'
)
