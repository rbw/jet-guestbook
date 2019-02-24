# -*- coding: utf-8 -*-

from jetfactory import ServiceApiBase
from .visitor import svc_visitor, VisitorModel, VisitorService
from .visit import svc_visit, VisitModel, VisitService
from .controller import Controller


class ServiceApi(ServiceApiBase):
    visit = svc_visit
    visitor = svc_visitor


controller = Controller
models = [VisitorModel, VisitModel]
services = ServiceApi()

