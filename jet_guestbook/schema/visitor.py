# -*- coding: utf-8 -*-

from jetfactory.schema import fields, Schema


class Visitor(Schema):
    id = fields.Integer()
    name = fields.String()
    location = fields.String()
