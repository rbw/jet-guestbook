# -*- coding: utf-8 -*-

from jetfactory.controller import BaseController, Injector, route, input_load, output_dump
from jetfactory.schema import ParamsSchema

from jet_guestbook.service import VisitService, VisitorService
from jet_guestbook.schema import Visit, Visitor, VisitNew


class Controller(BaseController):
    def __init__(self):
        self.visit = VisitService()
        self.visitor = VisitorService()
        self.log.debug('Guestbook opening')

    def on_ready(self):
        self.log.debug(f'Guestbook opened at {self.pkg.path}')

    async def on_request(self, request):
        self.log.debug(f'Request received: {request}')

    @route('/', 'GET', 'List of entries')
    @input_load(query=ParamsSchema)
    @output_dump(Visit, many=True)
    async def visits_get(self, query):
        return await self.visit.get_many(**query)

    @route('/visitors', 'GET', 'List of visitors')
    @input_load(query=ParamsSchema)
    @output_dump(Visitor, many=True)
    async def visitors_get(self, query):
        return await self.visitor.get_many(query)

    @route('/visitors/<visitor_id>', 'GET', 'Visitor details')
    @output_dump(Visitor)
    async def visitor_get(self, visitor_id):
        return await self.visitor.get_by_pk(visitor_id)

    @route('/visitors/<visitor_id>/visits', 'GET', 'Visits by visitor')
    @input_load(query=ParamsSchema)
    @output_dump(Visit)
    async def visitor_entries(self, visitor_id, query):
        query.update({'visitor': visitor_id})
        return await self.visit.get_many(**query)

    @route('/<visit_id>', 'GET', 'Visit details')
    @output_dump(Visit)
    async def visit_get(self, visit_id):
        return await self.visit.get_by_pk(visit_id)

    @route('/<visit_id>', 'PUT', 'Update entry', inject=[Injector.remote_addr])
    @input_load(body=Visit)
    @output_dump(Visit)
    async def visit_update(self, remote_addr, body, visit_id):
        return await self.visit.visit_update(remote_addr, visit_id, body)

    @route('/<visit_id>', 'DELETE', 'Delete entry', inject=[Injector.remote_addr])
    @output_dump(Visit)
    async def visit_delete(self, remote_addr, visit_id):
        return await self.visit.visit_delete(remote_addr, visit_id)

    @route('/count', 'GET', 'Entry count')
    @output_dump(Visit)
    async def visit_count(self, query):
        return {'count': await self.visit.count(**query)}

    @route('/', 'POST', 'Create entry', inject=[Injector.remote_addr])
    @input_load(body=VisitNew)
    @output_dump(Visit)
    async def visit_add(self, body, remote_addr):
        return await self.visit.visit_add(remote_addr, body)

