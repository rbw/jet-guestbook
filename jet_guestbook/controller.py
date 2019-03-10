# -*- coding: utf-8 -*-

from jetfactory.controller import ControllerBase, Injector, route, input_load, output_dump
from jetfactory.schema import ParamsSchema, DeleteSchema, CountSchema
from jet_guestbook.schema import Visit, Visitor, VisitNew
from .service import VisitService, VisitorService


class Controller(ControllerBase):
    def __init__(self):
        self.visit = VisitService()
        self.visitor = VisitorService()
        self.log.debug('Guestbook opening')

    async def on_ready(self):
        self.log.debug(f'Guestbook opened at {self.pkg.path}')

    async def on_request(self, request):
        self.log.debug(f'Request received: {request}')

    @route('/', 'GET')
    @input_load(query=ParamsSchema)
    @output_dump(Visit, many=True)
    async def visits_get(self, query):
        return await self.visit.get_many(**query)

    @route('/visitors', 'GET')
    @input_load(query=ParamsSchema)
    @output_dump(Visitor, many=True)
    async def visitors_get(self, query):
        return await self.visitor.get_many(query)

    @route('/visitors/<visitor_id>', 'GET')
    @output_dump(Visitor)
    async def visitor_get(self, visitor_id):
        return await self.visitor.get_by_pk(visitor_id)

    @route('/visitors/<visitor_id>/visits', 'GET')
    @input_load(query=ParamsSchema)
    @output_dump(Visit)
    async def visitor_entries(self, visitor_id, query):
        query.update({'visitor': visitor_id})
        return await self.visit.get_many(**query)

    @route('/<visit_id>', 'GET')
    @output_dump(Visit)
    async def visit_get(self, visit_id):
        return await self.visit.get_by_pk(visit_id)

    @route('/<visit_id>', 'PUT', inject=[Injector.remote_addr])
    @input_load(body=Visit)
    @output_dump(Visit)
    async def visit_update(self, remote_addr, body, visit_id):
        return await self.visit.visit_update(remote_addr, visit_id, body)

    @route('/<visit_id>', 'DELETE', inject=[Injector.remote_addr])
    @output_dump(DeleteSchema)
    async def visit_delete(self, remote_addr, visit_id):
        return await self.visit.visit_delete(remote_addr, visit_id)

    @route('/count', 'GET')
    @output_dump(CountSchema)
    async def visit_count(self, query):
        return {'count': await self.visit.count(**query)}

    @route('/', 'POST', inject=[Injector.remote_addr])
    @input_load(body=VisitNew)
    @output_dump(Visit)
    async def visit_add(self, body, remote_addr):
        return await self.visit.visit_add(remote_addr, body)

