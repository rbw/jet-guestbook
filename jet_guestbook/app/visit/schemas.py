# -*- coding: utf-8 -*-

from jetfactory.schema import fields, Schema
from ..visitor.schemas import Visitor


class Visit(Schema):
    id = fields.Integer()
    visitor = fields.Nested(Visitor)
    visited_on = fields.String(attribute='created_on')
    message = fields.String()
    name = fields.String()

    class Meta:
        dump_only = ['id', 'visitor', 'visited_on']
        load_only = ['visit_id', 'visitor_id']


class VisitNew(Schema):
    message = fields.String(required=True)
    name = fields.String(required=True)
